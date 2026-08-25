import pytest
from agency.memory.store import MemoryStore, MemoryEntry
from agency.approval.core import ApprovalManager, ApprovalToken

def test_project_memory_persists_and_recovers(tmp_path):
    p=tmp_path/"memory.json"; s=MemoryStore(str(p)); s.write(MemoryEntry(key="builder.permission",value="P2_SCOPED",scope="PROJECT",status="APPROVED",evidence_level="E4",approved_by="human")); r=MemoryStore(str(p)); e,status=r.resolve_key("builder.permission","PROJECT"); assert status=="RESOLVED" and e.value=="P2_SCOPED"

def test_conflicting_memory_is_detected():
    s=MemoryStore(); s.write(MemoryEntry(key="k",value="A",scope="PROJECT",status="APPROVED",evidence_level="E4")); s.write(MemoryEntry(key="k",value="B",scope="PROJECT",status="APPROVED",evidence_level="E4")); e,status=s.resolve_key("k","PROJECT"); assert e is None and status=="MEMORY_CONFLICT"

def test_approval_replay_is_blocked():
    m=ApprovalManager(); t=ApprovalToken(action="DEPLOY",target="production/api",change_id="chg-2",state_version=1); m.approve(t); assert m.reserve(t,"exec-1")[0]; assert not m.reserve(t,"exec-2")[0]; assert m.consume(t,"exec-1")[0]; assert t.status=="USED"
