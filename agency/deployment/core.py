from dataclasses import dataclass, field
from typing import List

ALLOWED_TRANSITIONS = {
    "DEVELOPMENT": {"TEST"},
    "TEST": {"STAGING"},
    "STAGING": {"PRODUCTION"},
    "PRODUCTION": set(),
}

@dataclass
class DeploymentGate:
    source_environment: str
    target_environment: str
    version_id: str
    change_id: str
    build_completed: bool
    validation_passed: bool
    qa_status: str
    regression_passed: bool
    policies_valid: bool
    rollback_ready: bool
    trace_enabled: bool
    human_approval_required: bool = False
    approval_valid: bool = False

@dataclass
class DeploymentState:
    version_id: str
    current_environment: str = "DEVELOPMENT"
    promotion_history: List[dict] = field(default_factory=list)

def validate_environment_gate(gate: DeploymentGate, *, version_status: str, open_high_defects: int = 0, open_critical_defects: int = 0):
    blockers = []
    if gate.target_environment not in ALLOWED_TRANSITIONS.get(gate.source_environment, set()):
        blockers.append("INVALID_ENVIRONMENT_TRANSITION")
    if not gate.build_completed:
        blockers.append("BUILD_INCOMPLETE")
    if not gate.validation_passed:
        blockers.append("VALIDATION_NOT_PASSED")
    if gate.qa_status not in {"PASS", "PASS_WITH_WARNINGS"}:
        blockers.append("QA_NOT_APPROVED")
    if not gate.regression_passed:
        blockers.append("REGRESSION_NOT_PASSED")
    if not gate.policies_valid:
        blockers.append("POLICY_CHECK_FAILED")
    if open_high_defects:
        blockers.append("OPEN_HIGH_DEFECTS")
    if open_critical_defects:
        blockers.append("OPEN_CRITICAL_DEFECTS")
    if gate.target_environment == "PRODUCTION":
        if version_status != "STABLE":
            blockers.append("VERSION_NOT_STABLE")
        if not gate.rollback_ready:
            blockers.append("ROLLBACK_NOT_READY")
        if not gate.trace_enabled:
            blockers.append("OBSERVABILITY_NOT_ACTIVE")
        if gate.human_approval_required and not gate.approval_valid:
            blockers.append("PRODUCTION_APPROVAL_MISSING")
    return len(blockers) == 0, blockers

def promote_environment(state: DeploymentState, gate: DeploymentGate, gate_allowed: bool, blockers: list[str]):
    if not gate_allowed:
        return {"status": "BLOCKED", "blockers": blockers, "current_environment": state.current_environment}
    record = {"from": state.current_environment, "to": gate.target_environment, "version_id": gate.version_id, "change_id": gate.change_id, "status": "COMPLETED"}
    state.current_environment = gate.target_environment
    state.promotion_history.append(record)
    return {"status": "COMPLETED", "current_environment": state.current_environment, "record": record}
