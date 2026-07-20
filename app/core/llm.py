from langchain_openai import ChatOpenAI

from app.core.config import settings

llm = ChatOpenAI(
    model="gpt-4.1-mini",  # or the model you have access to
    api_key=settings.OPENAI_API_KEY,
    temperature=0.2,
)
