from typing import List, Literal, Optional
from pydantic import BaseModel, Field

EvidenceLevel = Literal["E0", "E1", "E2", "E3", "E4"]
RelevanceLevel = Literal["R0", "R1", "R2", "R3"]
ABCDecision = Literal["A", "B", "C"]
AgentStatus = Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "BLOCKED", "UNKNOWN"]

class ResearchFinding(BaseModel):
    claim: str = Field(min_length=1)
    source: str = Field(min_length=1)
    evidence_level: EvidenceLevel
    relevance: RelevanceLevel
    confidence: float = Field(ge=0.0, le=1.0)

class ResearchResult(BaseModel):
    status: AgentStatus
    findings: List[ResearchFinding] = Field(default_factory=list)
    contradictions: List[str] = Field(default_factory=list)
    unknowns: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
    error: Optional[str] = None

class FeatureScoring(BaseModel):
    benefit: int = Field(ge=0, le=5)
    integration_effort: int = Field(ge=0, le=5)
    risk: int = Field(ge=0, le=5)
    redundancy: int = Field(ge=0, le=5)
    system_fit: int = Field(ge=0, le=5)
    raw_score: int

class DecisionOverride(BaseModel):
    applied: bool = False
    type: Optional[str] = None
    reason: Optional[str] = None

class FeatureAssessment(BaseModel):
    feature_id: str = Field(min_length=1)
    feature_name: str = Field(min_length=1)
    source_refs: List[str] = Field(default_factory=list)
    evidence_level: EvidenceLevel
    confidence: float = Field(ge=0.0, le=1.0)
    scoring: FeatureScoring
    override: DecisionOverride = Field(default_factory=DecisionOverride)
    score_decision: ABCDecision
    final_decision: ABCDecision
    human_review_required: bool = False
    rationale: str = Field(min_length=1)
    risks: List[str] = Field(default_factory=list)
    dependencies: List[str] = Field(default_factory=list)
    open_questions: List[str] = Field(default_factory=list)
    recommended_next_step: str = ""

class AnalysisResult(BaseModel):
    status: AgentStatus
    assessments: List[FeatureAssessment] = Field(default_factory=list)
    overall_decision: Optional[ABCDecision] = None
    confidence: float = Field(ge=0.0, le=1.0)
    error: Optional[str] = None
