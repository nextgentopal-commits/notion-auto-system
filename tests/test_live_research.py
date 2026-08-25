from agency.agents.research import ResearchAgent
from agency.research.sources import (
    SourceFinding,
    SourceUnavailable,
    WebFinding,
    WebResearchPacket,
)


class FakeGitHub:
    def inspect_repository(self, repository):
        return [
            SourceFinding(
                claim=f"{repository} exists",
                source=f"https://github.com/{repository}",
            )
        ]


class FakeWeb:
    def search(self, query):
        return WebResearchPacket(
            findings=[
                WebFinding(
                    claim="official architecture verified",
                    source="https://example.com/official",
                    evidence_level="E4",
                    relevance="R3",
                    confidence=0.9,
                )
            ],
            contradictions=["one contradiction"],
            unknowns=[],
            confidence=0.9,
        )


class DownGitHub:
    def inspect_repository(self, repository):
        raise SourceUnavailable("down")


def test_injected_facts_path_still_works():
    result = ResearchAgent(github_source=DownGitHub()).inspect_repository(
        "x/y",
        {
            "findings": [("fact", "src", "E4", "R3", 1.0)],
            "confidence": 1.0,
        },
    )
    assert result.status == "COMPLETED"
    assert result.findings[0].claim == "x/y: fact"


def test_live_sources_merge_into_contract():
    result = ResearchAgent(
        github_source=FakeGitHub(),
        web_source=FakeWeb(),
    ).inspect_repository("x/y", include_web=True)
    assert result.status == "COMPLETED"
    assert len(result.findings) == 2
    assert result.contradictions == ["one contradiction"]


def test_live_source_failure_is_explicit():
    result = ResearchAgent(github_source=DownGitHub()).inspect_repository("x/y")
    assert result.status == "FAILED"
    assert "Live GitHub" in result.unknowns[0]
