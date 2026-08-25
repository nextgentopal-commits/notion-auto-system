import pytest

from agency.agents.orchestrator import Orchestrator
from agency.validation.schemas import ResearchFinding, ResearchResult


class FakeResearch:
    def __init__(self, first_confidence=0.95, first_unknowns=None):
        self.calls = []
        self.first_confidence = first_confidence
        self.first_unknowns = first_unknowns or []

    def inspect_repository(self, repository, facts=None, *, include_web=False):
        self.calls.append({"repository": repository, "facts": facts, "include_web": include_web})
        if facts is not None:
            return ResearchResult(
                status="COMPLETED",
                findings=[ResearchFinding(claim="pydantic type-safe tools", source="injected", evidence_level="E4", relevance="R3", confidence=1.0)],
                confidence=1.0,
            )
        if include_web:
            return ResearchResult(
                status="COMPLETED",
                findings=[
                    ResearchFinding(claim="pydantic type-safe tools", source="github", evidence_level="E4", relevance="R3", confidence=0.95),
                    ResearchFinding(claim="directional communication flow", source="web", evidence_level="E4", relevance="R3", confidence=0.95),
                ],
                confidence=0.95,
            )
        return ResearchResult(
            status="COMPLETED",
            findings=[ResearchFinding(claim="repository exists", source="github", evidence_level="E4", relevance="R3", confidence=self.first_confidence)],
            unknowns=self.first_unknowns,
            confidence=self.first_confidence,
        )


def _orchestrator(fake):
    orchestrator = Orchestrator()
    orchestrator.research = fake
    return orchestrator


def test_auto_keeps_github_only_when_evidence_is_sufficient():
    fake = FakeResearch(first_confidence=0.95)
    result = _orchestrator(fake).run("Inspect owner/repo", web_mode="auto")
    assert len(fake.calls) == 1
    assert result["source_route"]["include_web"] is False
    assert result["source_route"]["reason"] == "GITHUB_EVIDENCE_SUFFICIENT"


def test_auto_adds_web_when_confidence_is_low():
    fake = FakeResearch(first_confidence=0.5)
    result = _orchestrator(fake).run("Inspect owner/repo", web_mode="auto")
    assert len(fake.calls) == 2
    assert fake.calls[-1]["include_web"] is True
    assert result["source_route"]["include_web"] is True
    assert result["source_route"]["reason"] == "LOW_CONFIDENCE"


def test_auto_adds_web_when_unknowns_exist():
    fake = FakeResearch(first_confidence=0.95, first_unknowns=["missing architecture evidence"])
    result = _orchestrator(fake).run("Inspect owner/repo", web_mode="auto")
    assert len(fake.calls) == 2
    assert result["source_route"]["reason"] == "UNKNOWNS_PRESENT"


def test_injected_facts_never_trigger_live_web():
    fake = FakeResearch()
    result = _orchestrator(fake).run(
        "Inspect owner/repo",
        repository_facts={"findings": [("fact", "src", "E4", "R3", 1.0)], "confidence": 1.0},
        web_mode="always",
    )
    assert len(fake.calls) == 1
    assert result["source_route"]["mode"] == "deterministic"
    assert result["source_route"]["include_web"] is False


def test_never_blocks_web_escalation():
    fake = FakeResearch(first_confidence=0.2, first_unknowns=["missing"])
    result = _orchestrator(fake).run("Inspect owner/repo", web_mode="never")
    assert len(fake.calls) == 1
    assert result["source_route"]["reason"] == "WEB_DISABLED"


def test_invalid_web_mode_is_rejected():
    with pytest.raises(ValueError):
        Orchestrator().run("Inspect owner/repo", web_mode="sometimes")
