from agency.agents.builder import BuildScope, PlannedChange, ControlledWriter, BuilderAgent, content_hash
from agency.agents.orchestrator import Orchestrator
FACTS={"findings":[("uses Pydantic type-safe tools","github:readme","E4","R3",0.98),("supports directional communication flows","github:readme","E4","R3",0.97)],"confidence":0.95}

def test_atomic_transaction_rolls_back_first_write(tmp_path):
    a=tmp_path/"a.txt"; b=tmp_path/"b.txt"; a.write_text("A0"); b.write_text("B0")
    r=BuilderAgent(ControlledWriter(str(tmp_path))).execute([PlannedChange("MODIFY","a.txt","A1",expected_hash=content_hash("A0")),PlannedChange("MODIFY","b.txt","B1",expected_hash="stale")],BuildScope(allowed_modify=["a.txt","b.txt"]))
    assert r.status=="FAILED" and r.rolled_back and a.read_text()=="A0" and b.read_text()=="B0"

def test_full_chain_promotes_version_to_stable(tmp_path):
    out=Orchestrator().run("Prüfe VRSEN/agency-swarm und integriere geeignete Funktionen",FACTS,workspace=str(tmp_path),build_changes=[PlannedChange("CREATE","generated.txt","ok")],build_scope=BuildScope(allowed_create=["generated.txt"]))
    assert out["qa_result"]["status"]=="PASS" and out["version_result"]["status"]=="STABLE"
