# app/rag/config.py

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

CHROMA_PERSIST_DIRECTORY = "data/chroma_db"
KNOWLEDGE_BASE_DIRECTORY = "data/knowledge_base"

RETRIEVAL_TOP_K = 3

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
