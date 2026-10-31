
import faiss
from sentence_transformers import SentenceTransformer

from .document_loader import (
    load_policy_documents,
    split_policy_documents,
)

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

_model = None
_index = None
_chunks = None


def get_model():
    """Load the embedding model once per Python process."""
    global _model

    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)

    return _model


def get_policy_index():
    """Create the FAISS index and chunks on first use."""
    global _index, _chunks

    if _index is None:
        documents = load_policy_documents()

        if not documents:
            raise ValueError(
                "No policy documents found in the policies directory."
            )

        _chunks = split_policy_documents(documents)

        if not _chunks:
            raise ValueError("Policy documents produced no chunks.")

        texts = [chunk["content"] for chunk in _chunks]

        embeddings = get_model().encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

        embeddings = embeddings.astype("float32")

        _index = faiss.IndexFlatIP(embeddings.shape[1])
        _index.add(embeddings)

    return _index, _chunks


def search_policy_chunks(
    query: str,
    top_k: int = 3,
) -> list[dict]:
    """Return the most semantically similar policy chunks."""
    if not query.strip():
        return []

    index, chunks = get_policy_index()

    query_embedding = get_model().encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype("float32")

    count = min(max(top_k, 1), len(chunks))
    scores, indices = index.search(query_embedding, count)

    results = []

    for score, position in zip(scores[0], indices[0]):
        if position < 0:
            continue

        results.append({
            **chunks[int(position)],
            "similarity_score": round(float(score), 4),
        })

    return results
