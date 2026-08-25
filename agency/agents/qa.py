from dataclasses import dataclass, field

@dataclass
class QADefect:
    severity: str
    code: str
    issue: str

@dataclass
class QAResult:
    status: str
    defects: list[QADefect] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

class QAAgent:
    def review_build(self, build_result: dict) -> QAResult:
        defects = []

        if build_result.get("status") != "COMPLETED":
            defects.append(QADefect(
                "HIGH", "QA_BUILD_INCOMPLETE",
                f"Build status is {build_result.get('status')}"
            ))

        if not build_result.get("scope_respected", False):
            defects.append(QADefect(
                "HIGH", "QA_SCOPE_VIOLATION",
                "Builder exceeded approved scope."
            ))

        if not build_result.get("qa_ready", False):
            defects.append(QADefect(
                "HIGH", "QA_NOT_READY",
                "Builder did not mark result as QA-ready."
            ))

        failed_writes = [
            w for w in build_result.get("writes", [])
            if w.get("status") not in {"COMPLETED", "NO_CHANGE"}
        ]
        if failed_writes:
            defects.append(QADefect(
                "HIGH", "QA_WRITE_FAILURE",
                "One or more controlled writes failed."
            ))

        if any(d.severity in {"CRITICAL", "HIGH", "MEDIUM"} for d in defects):
            return QAResult("REJECT", defects)

        warnings = []
        if all(w.get("status") == "NO_CHANGE" for w in build_result.get("writes", [])) and build_result.get("writes"):
            warnings.append("Build produced no file changes.")
            return QAResult("PASS_WITH_WARNINGS", defects, warnings)

        return QAResult("PASS", defects, warnings)

    def review(self, *, build_status: str, scope_respected: bool, critical=False) -> QAResult:
        if critical:
            return QAResult("REJECT", [QADefect("CRITICAL", "QA_CRITICAL", "Critical failure present.")])
        return self.review_build({
            "status": build_status,
            "scope_respected": scope_respected,
            "qa_ready": build_status == "COMPLETED" and scope_respected,
            "writes": [],
        })
