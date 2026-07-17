from langchain_core.prompts import ChatPromptTemplate

BUSINESS_SUMMARY_PROMPT = ChatPromptTemplate.from_template(
    """
You are a Senior Business Strategy Consultant.

Analyze the following business metrics and generate an executive summary.

Business Metrics:
{metrics}

Instructions:
- Summarize overall business performance.
- Identify the biggest risks.
- Highlight key strengths.
- Suggest 3 actionable business recommendations.

Keep the tone professional and concise.
"""
)
