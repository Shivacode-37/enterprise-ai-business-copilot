from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents
from app.rag.vector_store import create_vector_store


def ingest_documents() -> None:
    """
    Load, split, embed, and store documents in ChromaDB.
    """

    print("Loading documents...")
    documents = load_documents()

    print(f"Loaded {len(documents)} documents.")

    print("Splitting documents...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating vector store...")
    create_vector_store(chunks)

    print("✅ Vector store created successfully!")
