import json
from typing import Any

from langchain_core.output_parsers import StrOutputParser

from app.llm.llm_factor import get_llm
from app.reports.prompts import EXECUTIVE_REPORT_PROMPT
from app.reports.report_context import build_business_context

llm = get_llm()

parser = StrOutputParser()

executive_report_chain = EXECUTIVE_REPORT_PROMPT | llm | parser


def _json_serializer(obj: Any):

    if hasattr(obj, "to_dict"):
        return obj.to_dict(orient="records")

    if hasattr(obj, "item"):
        return obj.item()

    return str(obj)


def generate_executive_report(metrics: dict) -> str:
    """
    Generate an executive business report
    using a compact business context.
    """

    business_context = build_business_context(metrics)

    business_context_json = json.dumps(
        business_context,
        indent=2,
        default=_json_serializer,
    )

    return executive_report_chain.invoke(
        {
            "business_context": business_context_json,
        }
    )
