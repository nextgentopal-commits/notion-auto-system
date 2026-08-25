from dataclasses import dataclass, field
from typing import Dict, List, Optional
from agency.agents.builder import ControlledWriter, PlannedChange, WriteResult

@dataclass
class FileSnapshot:
    target: str
    existed: bool
    content: Optional[str]

@dataclass
class TransactionResult:
    status: str
    writes: List[WriteResult] = field(default_factory=list)
    rolled_back: bool = False
    rollback_errors: List[str] = field(default_factory=list)
    error: Optional[str] = None

class BuildTransaction:
    def __init__(self, writer: ControlledWriter):
        self.writer = writer

    def _snapshot(self, targets: List[str]) -> Dict[str, FileSnapshot]:
        snaps = {}
        for target in targets:
            content = self.writer.read_current(target)
            snaps[target] = FileSnapshot(target, content is not None, content)
        return snaps

    def _restore_direct(self, snapshot: FileSnapshot) -> None:
        path = self.writer._resolve(snapshot.target)
        if snapshot.existed:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(snapshot.content or "", encoding="utf-8")
        elif path.exists():
            path.unlink()

    def rollback(self, snapshots: Dict[str, FileSnapshot], completed: List[WriteResult]) -> List[str]:
        errors = []
        for result in reversed(completed):
            if not result.changed:
                continue
            try:
                self._restore_direct(snapshots[result.target])
            except Exception as exc:
                errors.append(f"{result.target}: {exc}")
        return errors

    def execute(self, changes: List[PlannedChange]) -> TransactionResult:
        snapshots = self._snapshot([c.target for c in changes])
        completed: List[WriteResult] = []
        for change in changes:
            if change.action == "DELETE":
                rb_errors = self.rollback(snapshots, completed)
                return TransactionResult(status="FAILED", writes=completed, rolled_back=not rb_errors, rollback_errors=rb_errors, error="DELETE_NOT_IMPLEMENTED")
            result = self.writer.write(change.target, change.content, expected_hash=change.expected_hash)
            completed.append(result)
            if result.status not in {"COMPLETED", "NO_CHANGE"}:
                rb_errors = self.rollback(snapshots, completed)
                return TransactionResult(status="FAILED", writes=completed, rolled_back=not rb_errors, rollback_errors=rb_errors, error=result.error)
        return TransactionResult(status="COMPLETED", writes=completed, rolled_back=False)
