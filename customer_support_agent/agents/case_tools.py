
from ..order_tools import (
    get_order,
    get_customer,
    get_delivery_status,
)
from ..knowledge.retrieval_tools import search_policy


def gather_case_evidence(order_id: str, complaint: str) -> dict:
    """Gather order, customer, delivery, and policy evidence for analysis.

    Args:
        order_id: The customer's order identifier.
        complaint: The customer's complaint and requested outcome.

    Returns:
        A structured collection of retrieved evidence.
    """
    order = get_order(order_id)

    if "error" in order:
        return {
            "case_status": "order_not_found",
            "order_id": order_id,
            "order_evidence": order,
            "customer_evidence": None,
            "delivery_evidence": None,
            "policy_evidence": None,
        }

    customer_id = order.get("customer_id")

    customer = (
        get_customer(customer_id)
        if customer_id
        else {"error": "Order has no customer ID."}
    )

    delivery = get_delivery_status(order_id)

    policy = search_policy(
        f"Customer complaint: {complaint}. "
        f"Order details: {order}. "
        "Find applicable policy, conditions, exceptions, "
        "and evidence requirements."
    )

    return {
        "case_status": "evidence_gathered",
        "order_evidence": order,
        "customer_evidence": customer,
        "delivery_evidence": delivery,
        "policy_evidence": policy,
        "analysis_reminders": [
            "A delivery status does not prove personal receipt.",
            "Retrieved policy excerpts may not establish eligibility.",
            "Missing evidence must be reported explicitly.",
            "Do not promise or approve a resolution.",
        ],
    }
