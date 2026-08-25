from .schemas import ResearchResult, FeatureAssessment, AnalysisResult

class SemanticValidationError(ValueError):
    pass

def validate_research_result(result: ResearchResult) -> None:
    if result.status == "COMPLETED" and not result.findings:
        raise SemanticValidationError("COMPLETED ResearchResult benötigt Findings.")
    if result.status == "FAILED" and not result.error:
        raise SemanticValidationError("FAILED ResearchResult benötigt error.")
    if result.confidence > 0.8 and not result.findings:
        raise SemanticValidationError("Hohe Confidence ohne Findings ist unplausibel.")

def validate_feature_assessment(a: FeatureAssessment) -> None:
    if a.evidence_level in {"E0", "E1"} and a.final_decision == "A":
        raise SemanticValidationError("E0/E1 darf nicht final_decision=A ergeben.")
    if a.override.applied and (not a.override.type or not a.override.reason):
        raise SemanticValidationError("Override benötigt type und reason.")
    if not a.override.applied and a.score_decision != a.final_decision:
        raise SemanticValidationError("Ohne Override müssen Entscheidungen übereinstimmen.")
    if a.scoring.risk >= 5 and a.final_decision == "A":
        raise SemanticValidationError("Risk 5 blockiert A.")
    if a.human_review_required and a.recommended_next_step not in {"HUMAN_REVIEW", "HUMAN_APPROVAL", "WAIT_FOR_HUMAN"}:
        raise SemanticValidationError("Human Review muss im Next Step sichtbar sein.")

def validate_analysis_result(result: AnalysisResult) -> None:
    if result.status == "COMPLETED" and not result.assessments:
        raise SemanticValidationError("COMPLETED AnalysisResult benötigt Assessments.")
    if result.status == "FAILED" and not result.error:
        raise SemanticValidationError("FAILED AnalysisResult benötigt error.")
    for a in result.assessments:
        validate_feature_assessment(a)
