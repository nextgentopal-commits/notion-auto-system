import pytest
from pydantic import ValidationError
from agency.agents.orchestrator import Orchestrator
from agency.runtime.guard import RuntimeGuard, RuntimeBudget
from agency.validation.schemas import ResearchFinding, FeatureAssessment, FeatureScoring
from agency.validation.semantic_rules import validate_feature_assessment, SemanticValidationError
from agency.agents.qa import QAAgent

FACTS={"findings":[("uses Pydantic type-safe tools","github:readme","E4","R3",0.98),("supports directional communication flows","github:readme","E4","R3",0.97),("supports state persistence","github:readme","E4","R2",0.95)],"confidence":0.96}

def test_valid_end_to_end():
    out=Orchestrator().run("Prüfe VRSEN/agency-swarm",FACTS)
    assert out["status"]=="COMPLETED" and out["analysis_result"]["overall_decision"]=="A"

def test_invalid_evidence_enum_rejected():
    with pytest.raises(ValidationError): ResearchFinding(claim="x",source="s",evidence_level="E9",relevance="R3",confidence=0.9)

def test_weak_evidence_cannot_be_a():
    a=FeatureAssessment(feature_id="x",feature_name="x",source_refs=["s"],evidence_level="E1",confidence=0.5,scoring=FeatureScoring(benefit=5,integration_effort=1,risk=1,redundancy=0,system_fit=5,raw_score=18),score_decision="A",final_decision="A",rationale="test")
    with pytest.raises(SemanticValidationError): validate_feature_assessment(a)

def test_runtime_agent_limit():
    g=RuntimeGuard(RuntimeBudget(max_agent_calls=1)); assert g.before_agent("research","x","1")[0]
    assert g.before_agent("analyst","y","2")[1]=="AGENT_CALL_LIMIT"

def test_loop_detection():
    g=RuntimeGuard(RuntimeBudget(max_agent_calls=10),loop_threshold=3)
    g.before_agent("research","same","x","s"); g.before_agent("research","same","x","s")
    assert g.before_agent("research","same","x","s")[1]=="LOOP_DETECTED"

def test_qa_scope_violation_rejects():
    q=QAAgent().review(build_status="COMPLETED",scope_respected=False); assert q.status=="REJECT"
