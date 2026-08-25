from dataclasses import dataclass, asdict
from pathlib import Path
import json

@dataclass
class RunState:
    run_id: str
    status: str
    step: str
    version: int = 1
    error: str | None = None

    def to_dict(self):
        return asdict(self)

class RunStateStore:
    def __init__(self, path: str):
        self.path = Path(path)

    def save(self, state: RunState):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(state.to_dict(), indent=2), encoding="utf-8")
        tmp.replace(self.path)

    def load(self) -> RunState | None:
        if not self.path.exists():
            return None
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return RunState(**raw)
