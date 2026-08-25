from agency.validation.schemas import ResearchFinding, ResearchResult

class ResearchAgent:
    def inspect_repository(self, repository: str, facts: dict | None = None) -> ResearchResult:
        if not facts:
            return ResearchResult(
                status="FAILED", findings=[], contradictions=[],
                unknowns=["Keine Repository-Fakten injiziert."],
                confidence=0.0, error="SOURCE_NOT_AVAILABLE"
            )
        findings = [
            ResearchFinding(
                claim=f"{repository}: {claim}",
                source=source,
                evidence_level=evidence,
                relevance=relevance,
                confidence=confidence,
            )
            for claim, source, evidence, relevance, confidence in facts.get("findings", [])
        ]
        return ResearchResult(
            status="COMPLETED" if findings else "UNKNOWN",
            findings=findings,
            contradictions=facts.get("contradictions", []),
            unknowns=facts.get("unknowns", []),
            confidence=facts.get("confidence", 0.0),
        )
