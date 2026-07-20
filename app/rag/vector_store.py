from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.rag.embedding_model import get_embedding_model
from app.rag.config import CHROMA_PERSIST_DIRECTORY


def create_vector_store(
    chunks: list[Document],
    persist_directory: str = CHROMA_PERSIST_DIRECTORY,
) -> Chroma:
    """
    Create and persist a Chroma vector database.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )

    return vector_store
