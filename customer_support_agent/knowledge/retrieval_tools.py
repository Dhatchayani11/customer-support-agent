
from .vector_store import search_policy_chunks


def search_policy(query: str) -> dict:
    """Search approved local policy documents for relevant evidence.

    Args:
        query: The complaint, policy question, or issue to investigate.

    Returns:
        Matching policy excerpts with their source filenames and scores.
    """
    try:
        results = search_policy_chunks(query, top_k=3)

        if not results:
            return {
                "found": False,
                "message": "No relevant policy evidence was found.",
                "results": [],
            }

        return {
            "found": True,
            "results": results,
            "notice": (
                "These are retrieved excerpts. Verify the source text "
                "before drawing conclusions about policy eligibility."
            ),
        }

    except Exception:
        # Avoid exposing local paths or internal error details to the model.
        return {
            "found": False,
            "message": (
                "Policy retrieval failed. The policy evidence "
                "could not be verified."
            ),
            "results": [],
        }
