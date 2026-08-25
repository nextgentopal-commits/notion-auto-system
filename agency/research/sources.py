from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Literal
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from pydantic import BaseModel, Field


@dataclass(frozen=True)
class SourceFinding:
    claim: str
    source: str
    evidence_level: Literal["E0", "E1", "E2", "E3", "E4"] = "E4"
    relevance: Literal["R0", "R1", "R2", "R3"] = "R3"
    confidence: float = 0.95


class SourceUnavailable(RuntimeError):
    pass


class GitHubPublicSource:
    """Read-only live GitHub research using GitHub's public REST API.

    An optional GITHUB_TOKEN increases rate limits. This source never writes to GitHub.
    """

    api_base = "https://api.github.com"

    def __init__(self, token: str | None = None, timeout: float = 15.0):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.timeout = timeout

    def _get_json(self, path: str) -> dict | list:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "agency-swarm-controlled/1.0",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = Request(f"{self.api_base}{path}", headers=headers)
        try:
            with urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise SourceUnavailable(f"GitHub source unavailable: {exc}") from exc

    def inspect_repository(self, repository: str) -> list[SourceFinding]:
        repo = self._get_json(f"/repos/{repository}")
        if not isinstance(repo, dict):
            raise SourceUnavailable("Unexpected GitHub repository response")

        html_url = str(repo.get("html_url") or f"https://github.com/{repository}")
        findings = [
            SourceFinding(
                claim=(
                    f"Repository {repository} exists; default_branch={repo.get('default_branch')}; "
                    f"archived={repo.get('archived')}; visibility={repo.get('visibility') or 'unknown'}."
                ),
                source=html_url,
            ),
            SourceFinding(
                claim=(
                    f"Repository metrics: stars={repo.get('stargazers_count', 0)}, "
                    f"forks={repo.get('forks_count', 0)}, open_issues={repo.get('open_issues_count', 0)}."
                ),
                source=html_url,
                relevance="R2",
                confidence=0.98,
            ),
        ]

        try:
            release = self._get_json(f"/repos/{repository}/releases/latest")
            if isinstance(release, dict) and release.get("tag_name"):
                findings.append(
                    SourceFinding(
                        claim=(
                            f"Latest GitHub release is {release.get('tag_name')} "
                            f"published_at={release.get('published_at')}."
                        ),
                        source=str(release.get("html_url") or html_url),
                    )
                )
        except SourceUnavailable:
            # A repository may legitimately have no releases. Core repository evidence remains valid.
            pass

        return findings


class WebFinding(BaseModel):
    claim: str = Field(min_length=1)
    source: str = Field(min_length=1)
    evidence_level: Literal["E0", "E1", "E2", "E3", "E4"]
    relevance: Literal["R0", "R1", "R2", "R3"]
    confidence: float = Field(ge=0.0, le=1.0)


class WebResearchPacket(BaseModel):
    findings: list[WebFinding] = Field(default_factory=list)
    contradictions: list[str] = Field(default_factory=list)
    unknowns: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)


class OpenAIWebSearchSource:
    """Optional live web research through the OpenAI Agents SDK WebSearchTool.

    Requires the optional `live` dependency and OPENAI_API_KEY. It is read-only and returns
    structured evidence that the existing Agency validation layer can inspect.
    """

    def __init__(self, model: str | None = None):
        self.model = model

    def search(self, query: str) -> WebResearchPacket:
        try:
            from agents import Agent, Runner, WebSearchTool
        except ImportError as exc:
            raise SourceUnavailable(
                "OpenAI Agents SDK is not installed. Install the project with the 'live' extra."
            ) from exc

        if not os.getenv("OPENAI_API_KEY"):
            raise SourceUnavailable("OPENAI_API_KEY is not configured")

        kwargs = {}
        if self.model:
            kwargs["model"] = self.model

        agent = Agent(
            name="Controlled Web Research",
            instructions=(
                "Research the request using web search. Return only verifiable findings. "
                "Each finding must include a canonical source URL. Use E4 only for primary or "
                "official sources, E3 for strong secondary evidence, E2 for weaker secondary "
                "evidence, and E0/E1 when unsupported. Mark relevance R0-R3. Explicitly list "
                "contradictions and unknowns; do not conceal uncertainty."
            ),
            tools=[WebSearchTool(search_context_size="medium")],
            output_type=WebResearchPacket,
            **kwargs,
        )
        try:
            result = Runner.run_sync(agent, query, max_turns=4)
        except Exception as exc:
            raise SourceUnavailable(f"Web search source unavailable: {exc}") from exc

        packet = result.final_output
        if not isinstance(packet, WebResearchPacket):
            raise SourceUnavailable("Web search returned an unexpected output type")
        return packet
