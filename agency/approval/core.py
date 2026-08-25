from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

@dataclass
class ApprovalToken:
    action: str
    target: str
    change_id: str
    state_version: int
    expected_hash: Optional[str] = None
    status: str = "PENDING"
    approval_id: str = field(default_factory=lambda: f"apr-{uuid4()}")
    execution_id: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    approved_at: Optional[str] = None

    def to_dict(self):
        return asdict(self)

class ApprovalManager:
    def approve(self, token: ApprovalToken) -> ApprovalToken:
        if token.status != "PENDING":
            raise ValueError("ILLEGAL_APPROVAL_STATE")
        token.status = "APPROVED"
        token.approved_at = datetime.now(timezone.utc).isoformat()
        return token

    def reject(self, token: ApprovalToken) -> ApprovalToken:
        if token.status != "PENDING":
            raise ValueError("ILLEGAL_APPROVAL_STATE")
        token.status = "REJECTED"
        return token

    def validate(self, token: ApprovalToken, *, action: str, target: str, change_id: str, state_version: int, current_hash: Optional[str] = None) -> tuple[bool, str]:
        if token.status != "APPROVED":
            return False, "APPROVAL_NOT_APPROVED"
        if token.action != action:
            return False, "APPROVAL_ACTION_MISMATCH"
        if token.target != target:
            return False, "APPROVAL_TARGET_MISMATCH"
        if token.change_id != change_id:
            return False, "APPROVAL_CHANGESET_MISMATCH"
        if token.state_version != state_version:
            return False, "APPROVAL_STATE_MISMATCH"
        if token.expected_hash is not None and token.expected_hash != current_hash:
            return False, "APPROVAL_HASH_MISMATCH"
        return True, "APPROVAL_VALID"

    def reserve(self, token: ApprovalToken, execution_id: str) -> tuple[bool, str]:
        if token.status != "APPROVED":
            return False, "APPROVAL_NOT_AVAILABLE"
        token.status = "RESERVED"
        token.execution_id = execution_id
        return True, "APPROVAL_RESERVED"

    def consume(self, token: ApprovalToken, execution_id: str) -> tuple[bool, str]:
        if token.status != "RESERVED":
            return False, "APPROVAL_NOT_RESERVED"
        if token.execution_id != execution_id:
            return False, "EXECUTION_ID_MISMATCH"
        token.status = "USED"
        return True, "APPROVAL_CONSUMED"

    def invalidate(self, token: ApprovalToken) -> ApprovalToken:
        token.status = "INVALIDATED"
        return token
