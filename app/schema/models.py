from pydantic import BaseModel


class SchemaMapping(BaseModel):
    sales: str | None = None
    profit: str | None = None
    quantity: str | None = None
    category: str | None = None
    sub_category: str | None = None
    region: str | None = None
    customer: str | None = None
    order_date: str | None = None

    # New fields
    segment: str | None = None
    discount: str | None = None
    order_id: str | None = None
    year: str | None = None
