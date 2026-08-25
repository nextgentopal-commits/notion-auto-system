from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

SENSITIVE_KEYS = {"password", "token", "api_key", "authorization", "secret", "cookie"}

def sanitize(data: dict[str, Any]) -> dict[str, Any]:
    out = {}
    for k, v in data.items():
        out[k] = "[REDACTED]" if k.lower() in SENSITIVE_KEYS else v
    return out

@dataclass
class TraceEvent:
    category: str
    event_type: str
    status: str
    run_id: str
    actor: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

@dataclass
class RunTrace:
    run_id: str
    events: list[TraceEvent] = field(default_factory=list)

    def record(self, *, category: str, event_type: str, status: str="INFO", actor: str | None=None, metadata: dict[str, Any] | None=None):
        event = TraceEvent(category=category, event_type=event_type, status=status, run_id=self.run_id, actor=actor, metadata=sanitize(metadata or {}))
        self.events.append(event)
        return event

    def to_dict(self):
        return {"run_id": self.run_id, "events": [asdict(e) for e in self.events]}
