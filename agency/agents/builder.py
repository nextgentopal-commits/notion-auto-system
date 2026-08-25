from dataclasses import dataclass, field, asdict
from hashlib import sha256
from pathlib import Path
from typing import List, Optional
from agency.versioning.models import ChangeSet

def content_hash(content: str) -> str:
    return sha256(content.encode("utf-8")).hexdigest()

@dataclass
class BuildScope:
    allowed_create: List[str] = field(default_factory=list)
    allowed_modify: List[str] = field(default_factory=list)
    forbidden: List[str] = field(default_factory=list)
    allow_file_deletion: bool = False

@dataclass
class PlannedChange:
    action: str
    target: str
    content: str
    reason: str = ""
    expected_hash: Optional[str] = None

@dataclass
class WriteResult:
    status: str
    target: str
    before_hash: Optional[str] = None
    after_hash: Optional[str] = None
    changed: bool = False
    error: Optional[str] = None

@dataclass
class BuildResult:
    status: str
    summary: str
    writes: List[WriteResult] = field(default_factory=list)
    scope_respected: bool = True
    scope_violations: List[str] = field(default_factory=list)
    qa_ready: bool = False
    transaction_status: Optional[str] = None
    rolled_back: bool = False
    rollback_errors: List[str] = field(default_factory=list)
    change_set: Optional[dict] = None
    error: Optional[str] = None

    def to_dict(self):
        return asdict(self)

class ControlledWriter:
    def __init__(self, workspace: str):
        self.workspace = Path(workspace).resolve()

    def _resolve(self, target: str) -> Path:
        path = (self.workspace / target).resolve()
        if self.workspace not in path.parents and path != self.workspace:
            raise ValueError("PATH_ESCAPE")
        return path

    def read_current(self, target: str) -> Optional[str]:
        path = self._resolve(target)
        if not path.exists():
            return None
        return path.read_text(encoding="utf-8")

    def write(self, target: str, new_content: str, expected_hash: Optional[str] = None) -> WriteResult:
        path = self._resolve(target)
        before = self.read_current(target)
        before_hash = content_hash(before) if before is not None else None
        if expected_hash is not None and before_hash != expected_hash:
            return WriteResult("BLOCKED", target, before_hash=before_hash, error="STALE_VERSION")
        if before == new_content:
            return WriteResult("NO_CHANGE", target, before_hash, before_hash, False)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(new_content, encoding="utf-8")
        after = path.read_text(encoding="utf-8")
        after_hash = content_hash(after)
        if after != new_content:
            return WriteResult("FAILED", target, before_hash, after_hash, False, "POST_WRITE_VERIFICATION_FAILED")
        return WriteResult("COMPLETED", target, before_hash, after_hash, True)

class BuilderAgent:
    PROTECTED_TARGETS = {"policies/core_policy.yaml", "policies/permissions.yaml"}

    def __init__(self, writer: ControlledWriter):
        self.writer = writer

    def _validate_change(self, change: PlannedChange, scope: BuildScope) -> Optional[str]:
        if change.target in self.PROTECTED_TARGETS:
            return f"PROTECTED_TARGET:{change.target}"
        if change.target in scope.forbidden:
            return f"FORBIDDEN_TARGET:{change.target}"
        if change.action == "CREATE" and change.target not in scope.allowed_create:
            return f"CREATE_OUTSIDE_SCOPE:{change.target}"
        if change.action == "MODIFY" and change.target not in scope.allowed_modify:
            return f"MODIFY_OUTSIDE_SCOPE:{change.target}"
        if change.action == "DELETE" and not scope.allow_file_deletion:
            return f"DELETE_NOT_ALLOWED:{change.target}"
        if change.action not in {"CREATE", "MODIFY", "DELETE"}:
            return f"UNSUPPORTED_ACTION:{change.action}"
        return None

    def execute(self, changes: List[PlannedChange], scope: BuildScope, *, base_version: str = "0.1.0", reason: str = "") -> BuildResult:
        violations = [v for c in changes if (v := self._validate_change(c, scope)) is not None]
        if violations:
            return BuildResult(status="BLOCKED", summary="Build blocked by scope/policy checks.", scope_respected=False, scope_violations=violations, qa_ready=False, error="SCOPE_OR_POLICY_VIOLATION")
        from agency.agents.transaction import BuildTransaction
        tx = BuildTransaction(self.writer).execute(changes)
        if tx.status != "COMPLETED":
            return BuildResult(status="FAILED", summary="Atomic transaction failed.", writes=tx.writes, scope_respected=True, qa_ready=False, transaction_status=tx.status, rolled_back=tx.rolled_back, rollback_errors=tx.rollback_errors, error=tx.error)
        cs = ChangeSet(base_version=base_version, reason=reason)
        for change, write in zip(changes, tx.writes):
            if write.status == "NO_CHANGE":
                continue
            if change.action == "CREATE": cs.files_created.append(change.target)
            elif change.action == "MODIFY": cs.files_modified.append(change.target)
            elif change.action == "DELETE": cs.files_deleted.append(change.target)
        return BuildResult(status="COMPLETED", summary="Atomic build completed within approved scope.", writes=tx.writes, scope_respected=True, qa_ready=True, transaction_status="COMPLETED", rolled_back=False, change_set=cs.to_dict())
