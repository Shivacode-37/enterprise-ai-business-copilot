from app.schema.models import SchemaMapping


class ColumnAccessor:
    def __init__(self, mapping: SchemaMapping):
        self.mapping = mapping

    @property
    def sales(self):
        return self.mapping.sales

    @property
    def profit(self):
        return self.mapping.profit

    @property
    def quantity(self):
        return self.mapping.quantity

    @property
    def category(self):
        return self.mapping.category

    @property
    def sub_category(self):
        return self.mapping.sub_category

    @property
    def region(self):
        return self.mapping.region

    @property
    def customer(self):
        return self.mapping.customer

    @property
    def order_date(self):
        return self.mapping.order_date

    @property
    def segment(self):
        return self.mapping.segment

    @property
    def discount(self):
        return self.mapping.discount

    @property
    def order_id(self):
        return self.mapping.order_id

    @property
    def year(self):
        return self.mapping.year
