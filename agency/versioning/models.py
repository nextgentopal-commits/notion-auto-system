from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import List, Optional
from uuid import uuid4

@dataclass
class ChangeSet:
    change_id: str = field(default_factory=lambda: f"chg-{uuid4()}")
    base_version: str = "0.1.0"
    created_by: str = "builder"
    reason: str = ""
    files_created: List[str] = field(default_factory=list)
    files_modified: List[str] = field(default_factory=list)
    files_deleted: List[str] = field(default_factory=list)
    expected_effect: str = ""
    risk_level: str = "LOW"
    rollback_possible: bool = True

    def to_dict(self):
        return asdict(self)

@dataclass
class VersionRecord:
    version_id: str
    base_version: Optional[str]
    status: str
    change_id: str
    files_changed: List[str] = field(default_factory=list)
    qa_status: Optional[str] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    reason: str = ""

    def to_dict(self):
        return asdict(self)

class VersionRegistry:
    def __init__(self):
        self.versions: dict[str, VersionRecord] = {}
        self.history: list[dict] = []

    def register(self, record: VersionRecord):
        if record.version_id in self.versions:
            raise ValueError("VERSION_ALREADY_EXISTS")
        self.versions[record.version_id] = record
        self.history.append({"event": "REGISTERED", "version": record.version_id, "status": record.status})

    def promote_to_stable(self, version_id: str, qa_status: str):
        record = self.versions[version_id]
        if record.status != "CANDIDATE":
            raise ValueError("VERSION_NOT_CANDIDATE")
        if qa_status not in {"PASS", "PASS_WITH_WARNINGS"}:
            raise ValueError("QA_NOT_APPROVED")
        record.status = "STABLE"
        record.qa_status = qa_status
        self.history.append({"event": "PROMOTED", "version": version_id, "status": "STABLE"})
        return record
