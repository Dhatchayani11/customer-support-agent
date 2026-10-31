REQUIRED_SECTIONS = [
    "Case Overview",
    "Verified Facts",
    "Customer-Reported Claims",
    "Relevant Policy Evidence",
    "Evidence Comparison",
    "Missing Information and Risks",
    "Recommended Next Investigation Step",
]


def validate_case_assessment(case_assessment: str) -> dict:
    """
    Check whether the Case Analysis report contains the
    expected sections before preparing resolution options.

    Args:
        case_assessment: The Case Analysis Agent's report.

    Returns:
        Assessment completeness and missing sections.
    """
    if not case_assessment or not case_assessment.strip():
        return {
            "ready_for_review": False,
            "missing_sections": REQUIRED_SECTIONS,
            "message": "No case assessment was provided.",
        }

    missing_sections = [
        section
        for section in REQUIRED_SECTIONS
        if section.lower() not in case_assessment.lower()
    ]

    return {
        "ready_for_review": len(missing_sections) == 0,
        "missing_sections": missing_sections,
        "message": (
            "Case assessment contains all expected sections."
            if not missing_sections
            else "Case assessment is incomplete. Review the missing sections."
        ),
    }