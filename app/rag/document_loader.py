from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)
from langchain_core.documents import Document

from app.rag.config import KNOWLEDGE_BASE_DIRECTORY


def load_documents(
    data_dir: str = KNOWLEDGE_BASE_DIRECTORY,
) -> list[Document]:
    """
    Load all supported documents from the knowledge base directory.
    """

    knowledge_path = Path(data_dir)

    if not knowledge_path.exists():
        raise FileNotFoundError(
            f"Knowledge base directory not found: {data_dir}"
        )

    documents: list[Document] = []

    for file in sorted(knowledge_path.iterdir()):

        if file.suffix == ".txt":
            loader = TextLoader(str(file), encoding="utf-8")

        elif file.suffix == ".pdf":
            loader = PyPDFLoader(str(file))

        else:
            continue

        documents.extend(loader.load())

    return documents
