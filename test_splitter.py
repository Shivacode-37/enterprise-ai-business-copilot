from app.rag.document_loader import load_documents
from app.rag.text_splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print(f"Original Documents : {len(documents)}")
print(f"Chunks Created     : {len(chunks)}")

print("\n")

for i, chunk in enumerate(chunks[:5], start=1):
    print("=" * 60)
    print(f"Chunk {i}")
    print(chunk.page_content)
