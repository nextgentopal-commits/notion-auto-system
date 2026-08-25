from agency.agents.orchestrator import Orchestrator
from agency.agents.builder import BuildScope, PlannedChange
FACTS={"findings":[("uses Pydantic type-safe tools","github:readme","E4","R3",0.98),("supports directional communication flows","github:readme","E4","R3",0.97),("supports state persistence","github:readme","E4","R2",0.95)],"confidence":0.96}

def test_full_chain_research_analyst_builder_qa(tmp_path):
    out=Orchestrator().run("Prüfe VRSEN/agency-swarm und integriere geeignete Funktionen",FACTS,workspace=str(tmp_path),build_changes=[PlannedChange("CREATE","generated/output.txt","agency-v1")],build_scope=BuildScope(allowed_create=["generated/output.txt"]))
    assert out["build_result"]["status"]=="COMPLETED" and out["qa_result"]["status"]=="PASS"

def test_scope_violation_is_blocked_and_qa_rejects(tmp_path):
    out=Orchestrator().run("Prüfe VRSEN/agency-swarm und integriere geeignete Funktionen",FACTS,workspace=str(tmp_path),build_changes=[PlannedChange("CREATE","outside.txt","blocked")],build_scope=BuildScope(allowed_create=["safe.txt"]))
    assert out["build_result"]["status"]=="BLOCKED" and out["qa_result"]["status"]=="REJECT"
