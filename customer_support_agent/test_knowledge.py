
from .knowledge.document_loader import (
    load_policy_documents,
    split_policy_documents,
)
from .knowledge.vector_store import search_policy_chunks


def test_policy_documents_load():
    documents = load_policy_documents()

    assert len(documents) >= 4
    assert any(
        document["source"] == "delivery_policy.md"
        for document in documents
    )


def test_policy_documents_split_into_chunks():
    documents = load_policy_documents()
    chunks = split_policy_documents(documents)

    assert chunks
    assert all(chunk["content"].strip() for chunk in chunks)
    assert all(chunk["source"] for chunk in chunks)


def test_missing_package_retrieval():
    results = search_policy_chunks(
        "Package marked delivered but customer never received it",
        top_k=3,
    )

    assert results
    assert any(
        "delivery" in result["source"].lower()
        or "refund" in result["source"].lower()
        for result in results
    )


def test_damaged_product_retrieval():
    results = search_policy_chunks(
        "Customer received a damaged product and wants a replacement",
        top_k=3,
    )

    assert results
    assert any(
        "damaged" in result["source"].lower()
        for result in results
    )
