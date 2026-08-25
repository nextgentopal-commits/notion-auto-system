from dataclasses import dataclass, asdict

@dataclass
class RunMetrics:
    agent_calls: int = 0
    failures: int = 0
    blocked: int = 0
    qa_rejects: int = 0

    def to_dict(self):
        return asdict(self)

def calculate_metrics(trace) -> RunMetrics:
    m = RunMetrics()
    for e in trace.events:
        if e.category == "AGENT":
            m.agent_calls += 1
        if e.status == "FAILED":
            m.failures += 1
        if e.status == "BLOCKED":
            m.blocked += 1
        if e.category == "QA" and e.metadata.get("decision") == "REJECT":
            m.qa_rejects += 1
    return m

def health_from_metrics(metrics: RunMetrics, *, critical: bool = False) -> dict:
    if critical:
        return {"overall": 0, "status": "CRITICAL"}
    score = 100 - metrics.failures * 20 - metrics.blocked * 10 - metrics.qa_rejects * 20
    score = max(0, score)
    status = "HEALTHY" if score >= 90 else "WARNING" if score >= 75 else "DEGRADED" if score >= 50 else "CRITICAL"
    return {"overall": score, "status": status}
