from dataclasses import dataclass
from hashlib import sha256

@dataclass
class RuntimeBudget:
    max_agent_calls: int = 4
    max_tool_calls: int = 12
    max_retries: int = 2
    max_revision_cycles: int = 3
    max_cost: float | None = None

class RuntimeGuard:
    def __init__(self, budget: RuntimeBudget | None = None, loop_threshold: int = 3):
        self.budget = budget or RuntimeBudget()
        self.agent_calls = 0
        self.tool_calls = 0
        self.retries = 0
        self.revisions = 0
        self.loop_threshold = loop_threshold
        self.signatures: dict[str, int] = {}
        self.circuit_open = False

    def before_agent(self, actor: str, action: str, input_repr: str, state_repr: str = ""):
        if self.circuit_open:
            return False, "CIRCUIT_OPEN"
        if self.agent_calls >= self.budget.max_agent_calls:
            return False, "AGENT_CALL_LIMIT"
        sig = sha256(f"{actor}|{action}|{input_repr}|{state_repr}".encode()).hexdigest()
        self.signatures[sig] = self.signatures.get(sig, 0) + 1
        if self.signatures[sig] >= self.loop_threshold:
            self.circuit_open = True
            return False, "LOOP_DETECTED"
        self.agent_calls += 1
        return True, "OK"
