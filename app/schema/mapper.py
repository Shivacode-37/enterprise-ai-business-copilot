from app.schema.models import SchemaMapping


def validate_mapping(
    mapping: SchemaMapping,
    columns: list[str],
) -> SchemaMapping:
    """
    Validate that detected columns actually exist in the uploaded dataset.
    Invalid mappings are replaced with None.
    """

    valid_columns = set(columns)

    validated = {}

    for field, value in mapping.model_dump().items():

        if value in valid_columns:
            validated[field] = value
        else:
            validated[field] = None

    return SchemaMapping(**validated)
