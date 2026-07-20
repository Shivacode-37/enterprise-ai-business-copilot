from app.rag.retriever import get_retriever

retriever = get_retriever()

query = "How can a company improve profitability?"

docs = retriever.invoke(query)

print(f"Retrieved {len(docs)} documents\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print(doc.page_content)
    print(doc.metadata)
