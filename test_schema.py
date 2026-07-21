from app.schema.detector import detect_schema

columns = [
    "Revenue",
    "Margin",
    "Department",
    "State",
    "Invoice Date",
    "Client Name"
]

mapping = detect_schema(columns)

print(mapping.model_dump())
