from app.schema.models import SchemaMapping
from app.schema.mapper import validate_mapping

columns = [
    "Revenue",
    "Margin",
    "Department",
    "State",
]

mapping = SchemaMapping(
    sales="Revenue",
    profit="Profit Margin",
    category="Department",
    region="State",
)

validated = validate_mapping(
    mapping,
    columns,
)

print(validated.model_dump())
