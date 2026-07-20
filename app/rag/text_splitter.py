from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.rag.config import CHUNK_SIZE, CHUNK_OVERLAP

def split_documents(
    documents:list[Document],
    chunk_size:int = 100,
    chunk_overlap:int = 20)-> list[Document]:
    """ Split documents into smaller chunks for embedding."""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(documents)

    return chunks
