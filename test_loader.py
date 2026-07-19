from app.rag.document_loader import load_documents

docs = load_documents()

print(f"Loaded {len(docs)} documents\n")

for doc in docs:
    print("=" * 50)
    print(doc.metadata)
    print()
    print(doc.page_content[:300])
