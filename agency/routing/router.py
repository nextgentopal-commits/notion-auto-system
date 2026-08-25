from dataclasses import dataclass

@dataclass
class RouteDecision:
    task_type: str
    route: list[str]
    reason: str

def route_task(goal: str) -> RouteDecision:
    text = goal.lower()
    signals = ("github", "repository", "repo", "recherch", "prüfe", "suche", "quelle")
    if any(s in text for s in signals):
        return RouteDecision("repository_analysis", ["research", "analyst"], "Verifizierbare externe Information erforderlich.")
    return RouteDecision("direct", [], "Kein Research-Bedarf erkannt.")
