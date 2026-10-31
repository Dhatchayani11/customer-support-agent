
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

POLICY_DIR = Path(__file__).parent.parent / "policies"


def load_policy_documents() -> list[dict]:
    """Load policy Markdown files and retain their source names."""
    documents = []

    for file_path in sorted(POLICY_DIR.glob("*.md")):
        content = file_path.read_text(encoding="utf-8").strip()

        if content:
            documents.append({
                "source": file_path.name,
                "content": content,
            })

    return documents


def split_policy_documents(
    documents: list[dict],
) -> list[dict]:
    """Split policy documents into overlapping text chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        separators=["\n## ", "\n# ", "\n\n", "\n", " "],
    )

    chunks = []

    for document in documents:
        for index, chunk in enumerate(
            splitter.split_text(document["content"])
        ):
            chunks.append({
                "chunk_id": f"{document['source']}:{index}",
                "source": document["source"],
                "content": chunk,
            })

    return chunks
