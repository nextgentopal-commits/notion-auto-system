from agency.validation.schemas import ResearchResult, AnalysisResult, FeatureAssessment, FeatureScoring, DecisionOverride

class AnalystAgent:
    def analyze_repository(self, research: ResearchResult) -> AnalysisResult:
        text = " ".join(f.claim.lower() for f in research.findings)
        benefits = 0
        if "type-safe" in text or "pydantic" in text:
            benefits += 1
        if "directional" in text or "communication flow" in text:
            benefits += 1
        if "state persistence" in text or "persistence" in text:
            benefits += 1
        if benefits >= 2:
            decision, benefit, fit = "A", 5, 5
        elif benefits == 1:
            decision, benefit, fit = "B", 3, 4
        else:
            decision, benefit, fit = "C", 1, 2
        evidence = max((f.evidence_level for f in research.findings), default="E0", key=lambda x: int(x[1]))
        score = benefit * 2 + fit * 2 - 2 - 1 - 1
        override = DecisionOverride()
        final = decision
        if evidence in {"E0", "E1"} and decision == "A":
            final = "B"
            override = DecisionOverride(applied=True, type="EVIDENCE", reason="E0/E1 cannot auto-integrate.")
        assessment = FeatureAssessment(feature_id="repository.selected-capabilities", feature_name="Selected repository capabilities", source_refs=[f.source for f in research.findings], evidence_level=evidence, confidence=research.confidence, scoring=FeatureScoring(benefit=benefit, integration_effort=2, risk=1, redundancy=1, system_fit=fit, raw_score=score), override=override, score_decision=decision, final_decision=final, rationale="Selective integration based on evidence and system fit.", recommended_next_step="BUILD" if final == "A" else "STOP_OR_RESERVE")
        return AnalysisResult(status="COMPLETED", assessments=[assessment], overall_decision=final, confidence=research.confidence)
