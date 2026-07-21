from app.core.llm import llm
from app.schema.models import SchemaMapping
from app.schema.prompt import SCHEMA_DETECTION_PROMPT


structured_llm = llm.with_structured_output(SchemaMapping)


def detect_schema(columns: list[str]) -> SchemaMapping:
    """
    Detect business column mappings using structured LLM output.
    """

    chain = SCHEMA_DETECTION_PROMPT | structured_llm

    mapping = chain.invoke(
        {
            "columns": ", ".join(columns)
        }
    )

    return mapping
