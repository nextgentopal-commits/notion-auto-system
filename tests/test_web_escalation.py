from agency.agents.orchestrator import Orchestrator
from agency.agents.research import ResearchAgent
from agency.research.sources import SourceFinding, WebFinding, WebResearchPacket


class CountingGitHub:
    def __init__(self, confidence=0.5):
        self.calls = 0
        self.confidence = confidence

    def inspect_repository(self, repository):
        self.calls += 1
        return [
            SourceFinding(
                claim=f"Repository {repository} exists but needs independent verification",
                source=f"https://github.com/{repository}",
                evidence_level="E4",
                relevance="R3",
                confidence=self.confidence,
            )
        ]


class CountingWeb:
    def __init__(self):
        self.calls = 0

    def search(self, query):
        self.calls += 1
        return WebResearchPacket(
            findings=[
                WebFinding(
                    claim="Official documentation independently verifies the architecture",
                    source="https://example.com/official",
                    evidence_level="E4",
                    relevance="R3",
                    confidence=0.95,
                )
            ],
            contradictions=[],
            unknowns=[],
            confidence=0.95,
        )


def make_orchestrator(github, web):
    orchestrator = Orchestrator()
    orchestrator.research = ResearchAgent(github_source=github, web_source=web)
    return orchestrator


def test_auto_escalates_to_web_for_low_confidence_github_evidence():
    github = CountingGitHub(confidence=0.5)
    web = CountingWeb()
    result = make_orchestrator(github, web).run(
        "Prüfe Repository VRSEN/agency-swarm",
        web_mode="auto",
    )

    assert result["source_route"]["include_web"] is True
    assert result["source_route"]["reason"] == "LOW_CONFIDENCE"
    assert github.calls == 1
    assert web.calls == 1
    assert len(result["research_result"]["findings"]) == 2


def test_never_mode_blocks_web_even_when_github_evidence_is_weak():
    github = CountingGitHub(confidence=0.4)
    web = CountingWeb()
    result = make_orchestrator(github, web).run(
        "Prüfe Repository VRSEN/agency-swarm",
        web_mode="never",
    )

    assert result["source_route"]["include_web"] is False
    assert result["source_route"]["reason"] == "WEB_DISABLED"
    assert github.calls == 1
    assert web.calls == 0


def test_always_mode_adds_web_without_refetching_github():
    github = CountingGitHub(confidence=0.99)
    web = CountingWeb()
    result = make_orchestrator(github, web).run(
        "Prüfe Repository VRSEN/agency-swarm",
        web_mode="always",
    )

    assert result["source_route"]["include_web"] is True
    assert result["source_route"]["reason"] == "WEB_FORCED"
    assert github.calls == 1
    assert web.calls == 1
