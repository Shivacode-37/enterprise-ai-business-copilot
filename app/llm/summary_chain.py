from langchain_core.output_parsers import StrOutputParser
from app.llm.llm_factor import get_llm
from app.llm.prompt_template import BUSINESS_SUMMARY_PROMPT

llm = get_llm()

parser = StrOutputParser()

summary_chain = BUSINESS_SUMMARY_PROMPT | llm | parser

def generate_ai_summary(metrics:dict)-> str:
    """
Generate an executive business summary using Langchain + Openai

    """
    return summary_chain.invoke({
        "metrics": metrics
    })
