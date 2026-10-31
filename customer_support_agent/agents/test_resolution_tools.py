from .resolution_tools import validate_case_assessment


def test_complete_case_assessment():
    assessment = """
    Case Overview
    Package marked delivered but not received.

    Verified Facts
    Order ORD1001 is marked delivered.

    Customer-Reported Claims
    Customer reports package not received.

    Relevant Policy Evidence
    Delivery policy retrieved.

    Evidence Comparison
    Delivery status shows delivered.

    Missing Information and Risks
    Personal receipt is not verified.

    Recommended Next Investigation Step
    Verify proof of delivery.
    """

    result = validate_case_assessment(assessment)

    assert result["ready_for_review"] is True
    assert result["missing_sections"] == []


def test_incomplete_case_assessment():
    assessment = """
    Case Overview
    Package marked delivered.

    Verified Facts
    Order status is delivered.
    """

    result = validate_case_assessment(assessment)

    assert result["ready_for_review"] is False
    assert len(result["missing_sections"]) > 0


def test_empty_case_assessment():
    result = validate_case_assessment("")

    assert result["ready_for_review"] is False
    assert len(result["missing_sections"]) == 7