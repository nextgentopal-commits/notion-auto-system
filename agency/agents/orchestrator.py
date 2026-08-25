from uuid import uuid4
import re

from agency.routing.router import route_task
from agency.routing.source_policy import decide_source_route
from agency.runtime.guard import RuntimeGuard
from agency.observability.trace import RunTrace
from agency.validation.semantic_rules import validate_research_result, validate_analysis_result
from agency.agents.research import ResearchAgent
from agency.agents.analyst import AnalystAgent
from agency.agents.builder import BuilderAgent, ControlledWriter, BuildScope, PlannedChange
from agency.agents.qa import QAAgent
from agency.versioning.models import VersionRegistry, VersionRecord
from agency.memory.store import MemoryStore, MemoryEntry
from agency.approval.core import ApprovalManager, ApprovalToken
from agency.deployment.core import DeploymentGate, DeploymentState, validate_environment_gate, promote_environment
from agency.state.store import RunState, RunStateStore
from agency.observability.metrics import calculate_metrics, health_from_metrics

class Orchestrator:
    def __init__(self):
        self.research = ResearchAgent()
        self.analyst = AnalystAgent()
        self.qa = QAAgent()
        self.versions = VersionRegistry()
        self.memory = MemoryStore()
        self.approvals = ApprovalManager()

    def _extract_repository(self, goal: str) -> str:
        m = re.search(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", goal)
        if not m:
            raise ValueError("Kein Repository im Format owner/name gefunden.")
        return m.group(1)

    def run(self, goal: str, repository_facts: dict | None = None, *, workspace: str | None = None, build_changes: list[PlannedChange] | None = None, build_scope: BuildScope | None = None, deploy_to: str | None = None, approval_token: ApprovalToken | None = None, state_version: int = 1, run_state_path: str | None = None, web_mode: str = "auto"):
        if web_mode not in {"auto", "always", "never"}:
            raise ValueError("web_mode must be one of: auto, always, never")

        run_id = str(uuid4())
        trace = RunTrace(run_id)
        runtime = RuntimeGuard()
        trace.record(category="SYSTEM", event_type="RUN_STARTED", status="SUCCESS", actor="orchestrator")
        state_store = RunStateStore(run_state_path) if run_state_path else None
        if state_store:
            state_store.save(RunState(run_id=run_id, status="RUNNING", step="routing", version=state_version))
        route = route_task(goal)
        trace.record(category="ROUTING", event_type="ROUTE_SELECTED", status="SUCCESS", actor="orchestrator", metadata={"route": route.route, "task_type": route.task_type})
        if not route.route:
            trace.record(category="SYSTEM", event_type="RUN_COMPLETED", status="SUCCESS", actor="orchestrator")
            return {"status": "COMPLETED", "route": [], "trace": trace.to_dict()}
        repo = self._extract_repository(goal)
        if state_store:
            state_store.save(RunState(run_id=run_id, status="RUNNING", step="research", version=state_version))
        ok, reason = runtime.before_agent("research", "inspect_repository", repo)
        if not ok:
            return {"status": "BLOCKED", "reason": reason, "trace": trace.to_dict()}

        research = self.research.inspect_repository(repo, repository_facts)
        validate_research_result(research)

        source_route = {"mode": "deterministic", "include_web": False, "reason": "INJECTED_FACTS"}
        if repository_facts is None:
            if web_mode == "never":
                source_route = {"mode": "never", "include_web": False, "reason": "WEB_DISABLED"}
            else:
                decision = decide_source_route(research, force_web=(web_mode == "always"))
                source_route = {"mode": web_mode, "include_web": decision.include_web, "reason": decision.reason}
                trace.record(
                    category="ROUTING",
                    event_type="SOURCE_ROUTE_SELECTED",
                    status="SUCCESS",
                    actor="orchestrator",
                    metadata=source_route,
                )
                if decision.include_web:
                    research = self.research.inspect_repository(repo, None, include_web=True)
                    validate_research_result(research)

        trace.record(category="AGENT", event_type="RESEARCH_COMPLETED", status="SUCCESS", actor="research", metadata={"findings": len(research.findings), "source_route": source_route})
        ok, reason = runtime.before_agent("analyst", "analyze_repository", repo, state_repr=research.model_dump_json())
        if not ok:
            return {"status": "BLOCKED", "reason": reason, "trace": trace.to_dict()}
        if state_store:
            state_store.save(RunState(run_id=run_id, status="RUNNING", step="analysis", version=state_version))
        analysis = self.analyst.analyze_repository(research)
        validate_analysis_result(analysis)
        trace.record(category="AGENT", event_type="ANALYSIS_COMPLETED", status="SUCCESS", actor="analyst", metadata={"decision": analysis.overall_decision})
        result = {"status": "COMPLETED", "repository": repo, "source_route": source_route, "research_result": research.model_dump(), "analysis_result": analysis.model_dump()}
        if analysis.overall_decision == "A" and build_changes is not None:
            if workspace is None or build_scope is None:
                raise ValueError("workspace and build_scope are required for build execution")
            ok, reason = runtime.before_agent("builder", "execute", repo)
            if not ok:
                return {"status": "BLOCKED", "reason": reason, "trace": trace.to_dict()}
            if state_store:
                state_store.save(RunState(run_id=run_id, status="RUNNING", step="build", version=state_version))
            builder = BuilderAgent(ControlledWriter(workspace))
            build_result = builder.execute(build_changes, build_scope, base_version="0.1.0", reason=goal)
            trace.record(category="BUILD", event_type="BUILD_COMPLETED", status="SUCCESS" if build_result.status == "COMPLETED" else "BLOCKED", actor="builder", metadata={"status": build_result.status, "scope_respected": build_result.scope_respected, "writes": len(build_result.writes)})
            result["build_result"] = build_result.to_dict()
            ok, reason = runtime.before_agent("qa", "review_build", repo, state_repr=str(build_result.to_dict()))
            if not ok:
                return {"status": "BLOCKED", "reason": reason, "trace": trace.to_dict()}
            if state_store:
                state_store.save(RunState(run_id=run_id, status="RUNNING", step="qa", version=state_version))
            qa_result = self.qa.review_build(build_result.to_dict())
            trace.record(category="QA", event_type="QA_DECISION", status="SUCCESS" if qa_result.status != "REJECT" else "FAILED", actor="qa", metadata={"decision": qa_result.status, "defects": len(qa_result.defects)})
            result["qa_result"] = {"status": qa_result.status, "defects": [d.__dict__ for d in qa_result.defects], "warnings": qa_result.warnings}
            if qa_result.status in {"PASS", "PASS_WITH_WARNINGS"} and build_result.change_set:
                version = VersionRecord(version_id="0.2.0", base_version="0.1.0", status="CANDIDATE", change_id=build_result.change_set["change_id"], files_changed=build_result.change_set["files_created"] + build_result.change_set["files_modified"] + build_result.change_set["files_deleted"], reason=goal)
                self.versions.register(version)
                self.versions.promote_to_stable("0.2.0", qa_result.status)
                result["version_result"] = self.versions.versions["0.2.0"].to_dict()
                result["version_history"] = list(self.versions.history)
                memory_entry = MemoryEntry(key=f"decision:{repo}", value={"decision": analysis.overall_decision, "version": "0.2.0"}, scope="PROJECT", status="APPROVED", evidence_level="E4", approved_by="qa")
                self.memory.write(memory_entry)
                result["memory_result"] = memory_entry.to_dict()
                if deploy_to:
                    deployment_state = DeploymentState(version_id="0.2.0", current_environment="STAGING" if deploy_to == "PRODUCTION" else "DEVELOPMENT")
                    approval_valid = False
                    approval_reason = None
                    approval_execution_id = None
                    if deploy_to == "PRODUCTION" and approval_token is not None:
                        approval_valid, approval_reason = self.approvals.validate(approval_token, action="DEPLOY", target="PRODUCTION", change_id=build_result.change_set["change_id"], state_version=state_version, current_hash=None)
                        if approval_valid:
                            approval_execution_id = f"exec-{run_id}"
                            reserved, reserve_reason = self.approvals.reserve(approval_token, approval_execution_id)
                            if not reserved:
                                approval_valid = False
                                approval_reason = reserve_reason
                    gate = DeploymentGate(source_environment=deployment_state.current_environment, target_environment=deploy_to, version_id="0.2.0", change_id=build_result.change_set["change_id"], build_completed=True, validation_passed=True, qa_status=qa_result.status, regression_passed=True, policies_valid=True, rollback_ready=True, trace_enabled=True, human_approval_required=(deploy_to == "PRODUCTION"), approval_valid=approval_valid)
                    allowed, blockers = validate_environment_gate(gate, version_status=self.versions.versions["0.2.0"].status)
                    if state_store:
                        state_store.save(RunState(run_id=run_id, status="RUNNING", step="deployment", version=state_version))
                    deployment_result = promote_environment(deployment_state, gate, allowed, blockers)
                    if deploy_to == "PRODUCTION" and approval_token is not None and approval_execution_id is not None:
                        if deployment_result["status"] == "COMPLETED":
                            consumed, consume_reason = self.approvals.consume(approval_token, approval_execution_id)
                            deployment_result["approval_consumed"] = consumed
                            deployment_result["approval_consume_reason"] = consume_reason
                        elif approval_token.status == "RESERVED":
                            self.approvals.invalidate(approval_token)
                            deployment_result["approval_invalidated"] = True
                    if approval_reason is not None:
                        deployment_result["approval_reason"] = approval_reason
                    result["deployment_result"] = deployment_result
        trace.record(category="SYSTEM", event_type="RUN_COMPLETED", status="SUCCESS", actor="orchestrator")
        metrics = calculate_metrics(trace)
        result["metrics"] = metrics.to_dict()
        result["health"] = health_from_metrics(metrics)
        result["trace"] = trace.to_dict()
        if state_store:
            state_store.save(RunState(run_id=run_id, status="COMPLETED", step="done", version=state_version))
            result["run_state"] = state_store.load().to_dict()
        return result