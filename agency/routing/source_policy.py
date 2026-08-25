from dataclasses import dataclass

from agency.validation.schemas import ResearchResult


@dataclass(frozen=True)
class SourceRouteDecision:
    include_web: bool
    reason: str


def decide_source_route(
    research: ResearchResult,
    *,
    force_web: bool = False,
    min_confidence: float = 0.85,
) -> SourceRouteDecision:
    """Decide whether GitHub evidence is sufficient or requires web verification.

    The policy is intentionally conservative: GitHub-only is accepted when live evidence is
    complete, high-confidence, and internally consistent. Web is added when evidence is weak,
    incomplete, contradictory, or explicitly forced by the caller.
    """
    if force_web:
        return SourceRouteDecision(True, "WEB_FORCED")
    if research.status != "COMPLETED":
        return SourceRouteDecision(True, "PRIMARY_SOURCE_INCOMPLETE")
    if not research.findings:
        return SourceRouteDecision(True, "NO_FINDINGS")
    if research.contradictions:
        return SourceRouteDecision(True, "CONTRADICTIONS_PRESENT")
    if research.unknowns:
        return SourceRouteDecision(True, "UNKNOWNS_PRESENT")
    if research.confidence < min_confidence:
        return SourceRouteDecision(True, "LOW_CONFIDENCE")
    if not any(f.evidence_level == "E4" and f.relevance == "R3" for f in research.findings):
        return SourceRouteDecision(True, "NO_HIGH_VALUE_PRIMARY_EVIDENCE")
    return SourceRouteDecision(False, "GITHUB_EVIDENCE_SUFFICIENT")
