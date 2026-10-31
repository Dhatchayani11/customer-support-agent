
from .case_tools import gather_case_evidence


def test_delivered_package_case():
    evidence = gather_case_evidence(
        "ORD1001",
        "Package marked delivered but not received",
    )

    assert evidence["case_status"] == "evidence_gathered"
    assert evidence["order_evidence"]["order_id"] == "ORD1001"
    assert evidence["delivery_evidence"]["delivery_status"] == "Delivered"
    assert evidence["policy_evidence"]["found"] is True


def test_delayed_delivery_case():
    evidence = gather_case_evidence(
        "ORD1002",
        "Order has not arrived and is delayed",
    )

    assert evidence["case_status"] == "evidence_gathered"
    assert evidence["delivery_evidence"]["delivery_status"] == "In Transit"


def test_unknown_order_case():
    evidence = gather_case_evidence(
        "ORD9999",
        "I want a refund for my missing package",
    )

    assert evidence["case_status"] == "order_not_found"
    assert evidence["customer_evidence"] is None
    assert evidence["delivery_evidence"] is None
