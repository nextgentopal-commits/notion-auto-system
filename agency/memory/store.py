from dataclasses import dataclass, field, asdict, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4
import json

@dataclass
class MemoryEntry:
    key: str
    value: Any
    scope: str
    status: str = "DRAFT"
    evidence_level: Optional[str] = None
    approved_by: Optional[str] = None
    supersedes: Optional[str] = None
    memory_id: str = field(default_factory=lambda: str(uuid4()))
    version: int = 1
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self):
        return asdict(self)

def can_persist(entry: MemoryEntry) -> tuple[bool, str]:
    if entry.scope == "RUN":
        return True, "RUN_MEMORY_ALLOWED"
    if entry.status not in {"VERIFIED", "APPROVED"}:
        return False, "MEMORY_NOT_VERIFIED"
    if entry.scope == "LONG_TERM" and entry.evidence_level not in {"E3", "E4"}:
        return False, "INSUFFICIENT_LONG_TERM_EVIDENCE"
    return True, "MEMORY_ALLOWED"

class MemoryStore:
    def __init__(self, path: str | None = None):
        self.path = Path(path) if path else None
        self.entries: dict[str, MemoryEntry] = {}
        if self.path and self.path.exists():
            self.load()

    def write(self, entry: MemoryEntry) -> MemoryEntry:
        allowed, reason = can_persist(entry)
        if not allowed:
            raise ValueError(reason)
        if entry.memory_id in self.entries:
            raise ValueError("MEMORY_ID_ALREADY_EXISTS")
        self.entries[entry.memory_id] = entry
        self._save_if_needed()
        return entry

    def find_by_key(self, key: str, scope: str | None = None) -> list[MemoryEntry]:
        out = [e for e in self.entries.values() if e.key == key]
        if scope:
            out = [e for e in out if e.scope == scope]
        return out

    def active_by_key(self, key: str, scope: str | None = None) -> list[MemoryEntry]:
        return [e for e in self.find_by_key(key, scope) if e.status in {"VERIFIED", "APPROVED"}]

    def resolve_key(self, key: str, scope: str | None = None):
        active = self.active_by_key(key, scope)
        if not active:
            return None, "NO_ACTIVE_MEMORY"
        superseded = {e.supersedes for e in active if e.supersedes}
        candidates = [e for e in active if e.memory_id not in superseded]
        if len(candidates) == 1:
            return candidates[0], "RESOLVED"
        values = {repr(e.value) for e in candidates}
        if len(values) == 1:
            newest = max(candidates, key=lambda e: (e.version, e.updated_at))
            return newest, "DUPLICATE_RESOLVED"
        return None, "MEMORY_CONFLICT"

    def deprecate(self, memory_id: str) -> MemoryEntry:
        current = self.entries[memory_id]
        updated = replace(current, status="DEPRECATED", updated_at=datetime.now(timezone.utc).isoformat())
        self.entries[memory_id] = updated
        self._save_if_needed()
        return updated

    def _save_if_needed(self):
        if not self.path:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(".tmp")
        payload = {"entries": [e.to_dict() for e in self.entries.values()]}
        temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        temp.replace(self.path)

    def load(self):
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        self.entries = {item["memory_id"]: MemoryEntry(**item) for item in raw.get("entries", [])}
