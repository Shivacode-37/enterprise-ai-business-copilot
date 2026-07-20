from langchain_chroma import Chroma

from app.rag.embedding_model import get_embedding_model
from app.rag.config import (
    CHROMA_PERSIST_DIRECTORY,
    RETRIEVAL_TOP_K,
)


def get_retriever(
    persist_directory: str = CHROMA_PERSIST_DIRECTORY,
    k: int = RETRIEVAL_TOP_K,
):
    """
    Return a retriever for semantic search.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model,
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever
