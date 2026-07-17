from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_llm():
    """Return the configured LLM instance.
    """
    return ChatOpenAI(
        model = settings.LLM_MODEL,
        api_key= settings.LLM_API_KEY,
        temperature= 0.3,
    )
