from agency.research.sources import (
    GitHubPublicSource,
    OpenAIWebSearchSource,
    SourceUnavailable,
)
from agency.validation.schemas import ResearchFinding, ResearchResult


class ResearchAgent:
    def __init__(self, github_source=None, web_source=None):
        self.github_source = github_source or GitHubPublicSource()
        self.web_source = web_source or OpenAIWebSearchSource()

    def _from_injected_facts(self, repository: str, facts: dict) -> ResearchResult:
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

    def augment_with_web(self, repository: str, research: ResearchResult) -> ResearchResult:
        """Add independent web evidence to an existing research result.

        The existing GitHub evidence is preserved exactly as collected. This avoids a second
        GitHub request during escalation and produces one coherent evidence packet.
        """
        findings = list(research.findings)
        contradictions = list(research.contradictions)
        unknowns = list(research.unknowns)
        errors = [research.error] if research.error else []

        try:
            packet = self.web_source.search(
                f"Research the current repository {repository}. Verify its latest release, "
                "architecture, dependencies, capabilities, and material risks using primary "
                "sources where possible."
            )
            findings.extend(
                ResearchFinding(
                    claim=item.claim,
                    source=item.source,
                    evidence_level=item.evidence_level,
                    relevance=item.relevance,
                    confidence=item.confidence,
                )
                for item in packet.findings
            )
            contradictions.extend(packet.contradictions)
            unknowns.extend(packet.unknowns)
        except SourceUnavailable as exc:
            errors.append(str(exc))
            unknowns.append("Live web evidence is unavailable.")

        if not findings:
            return ResearchResult(
                status="FAILED",
                findings=[],
                contradictions=contradictions,
                unknowns=unknowns,
                confidence=0.0,
                error="; ".join(errors) or "SOURCE_NOT_AVAILABLE",
            )

        confidence = sum(item.confidence for item in findings) / len(findings)
        return ResearchResult(
            status="COMPLETED",
            findings=findings,
            contradictions=contradictions,
            unknowns=unknowns,
            confidence=round(confidence, 4),
            error="; ".join(errors) if errors else None,
        )

    def inspect_repository(
        self,
        repository: str,
        facts: dict | None = None,
        *,
        include_web: bool = False,
    ) -> ResearchResult:
        """Inspect a repository using deterministic facts or read-only live sources.

        Existing tests can continue to inject `facts`. If facts are omitted, live GitHub
        repository metadata is fetched. Optional web search can add independent evidence.
        """
        if facts is not None:
            return self._from_injected_facts(repository, facts)

        findings: list[ResearchFinding] = []
        contradictions: list[str] = []
        unknowns: list[str] = []
        errors: list[str] = []

        try:
            for item in self.github_source.inspect_repository(repository):
                findings.append(
                    ResearchFinding(
                        claim=item.claim,
                        source=item.source,
                        evidence_level=item.evidence_level,
                        relevance=item.relevance,
                        confidence=item.confidence,
                    )
                )
        except SourceUnavailable as exc:
            errors.append(str(exc))
            unknowns.append("Live GitHub repository evidence is unavailable.")

        result = ResearchResult(
            status="COMPLETED" if findings else "FAILED",
            findings=findings,
            contradictions=contradictions,
            unknowns=unknowns,
            confidence=(round(sum(item.confidence for item in findings) / len(findings), 4) if findings else 0.0),
            error="; ".join(errors) if errors else (None if findings else "SOURCE_NOT_AVAILABLE"),
        )

        if include_web:
            return self.augment_with_web(repository, result)
        return result
