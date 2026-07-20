from langchain_huggingface import HuggingFaceEmbeddings
from app.rag.config import EMBEDDING_MODEL


def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Return the embedding model used throughout the RAG pipeline.
    """

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
