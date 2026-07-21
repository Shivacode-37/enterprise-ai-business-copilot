from langchain_core.prompts import ChatPromptTemplate


SCHEMA_DETECTION_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert data analyst.

Your task is to identify which columns represent common business fields.

Return ONLY valid JSON.

Possible fields:
sales
profit
quantity
category
sub_category
region
customer
order_date
segment
discount
order_id
year

Columns:

{columns}

Rules:

- Map only if reasonably confident.
- If a field does not exist, return null.
- Do not explain your reasoning.

Example:

{{
    "sales": "Revenue",
    "profit": "Margin",
    "quantity": null,
    "category": "Department",
    "sub_category": null,
    "region": "State",
    "customer": "Client Name",
    "order_date": "Invoice Date"
}}
Return valid JSON only.

Use JSON syntax:
- null (not None)
- true (not True)
- false (not False)
"""
)
