from agency.agents.orchestrator import Orchestrator
from agency.agents.builder import BuildScope, PlannedChange
FACTS={"findings":[("uses Pydantic type-safe tools","github:readme","E4","R3",0.98),("supports directional communication flows","github:readme","E4","R3",0.97),("supports state persistence","github:readme","E4","R2",0.95)],"confidence":0.96}

def test_full_nonprod_e2e_with_state_metrics_memory(tmp_path):
    state_path=tmp_path/"run-state.json"
    out=Orchestrator().run("Prüfe VRSEN/agency-swarm und integriere geeignete Funktionen",FACTS,workspace=str(tmp_path),build_changes=[PlannedChange("CREATE","artifact.txt","ok")],build_scope=BuildScope(allowed_create=["artifact.txt"]),run_state_path=str(state_path))
    assert out["status"]=="COMPLETED" and out["qa_result"]["status"]=="PASS" and out["version_result"]["status"]=="STABLE" and out["memory_result"]["status"]=="APPROVED" and out["run_state"]["status"]=="COMPLETED" and out["health"]["status"]=="HEALTHY"
