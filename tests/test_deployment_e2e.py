from agency.deployment.core import DeploymentGate, validate_environment_gate

def test_invalid_environment_jump_is_blocked():
    g=DeploymentGate(source_environment="DEVELOPMENT",target_environment="PRODUCTION",version_id="0.2.0",change_id="chg-x",build_completed=True,validation_passed=True,qa_status="PASS",regression_passed=True,policies_valid=True,rollback_ready=True,trace_enabled=True,human_approval_required=True,approval_valid=True)
    allowed,blockers=validate_environment_gate(g,version_status="STABLE"); assert not allowed and "INVALID_ENVIRONMENT_TRANSITION" in blockers

def test_production_without_approval_is_blocked():
    g=DeploymentGate(source_environment="STAGING",target_environment="PRODUCTION",version_id="1.0.0",change_id="chg-x",build_completed=True,validation_passed=True,qa_status="PASS",regression_passed=True,policies_valid=True,rollback_ready=True,trace_enabled=True,human_approval_required=True,approval_valid=False)
    allowed,blockers=validate_environment_gate(g,version_status="STABLE"); assert not allowed and "PRODUCTION_APPROVAL_MISSING" in blockers
