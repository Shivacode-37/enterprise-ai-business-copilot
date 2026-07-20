from langchain_core.prompts import ChatPromptTemplate

from app.rag.retriever import get_retriever
from app.core.llm import llm


retriever = get_retriever()

prompt = ChatPromptTemplate.from_template(
    """
You are a Senior Business Consultant.

Answer ONLY using:

1. Business Metrics
2. Retrieved Business Knowledge

If the knowledge base does not contain enough information,
say so explicitly.

-------------------------

Business Metrics

{metrics}

-------------------------

Business Knowledge

{context}

-------------------------

User Question

{question}

Provide a detailed, actionable business recommendation.
"""
)


def answer_question(metrics: str, question: str):

    docs = retriever.invoke(question)
# will combine them in one line
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "metrics": metrics,
            "context": context,
            "question": question,
        }
    )

    return response.content
