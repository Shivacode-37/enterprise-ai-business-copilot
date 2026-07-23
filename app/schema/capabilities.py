from app.schema.models import SchemaMapping


class DatasetCapabilities:
    def __init__(self, mapping: SchemaMapping):
        self.mapping = mapping

    def has(self, field: str) -> bool:
        """
        Returns True if the mapped field exists.
        """
        value = getattr(self.mapping, field, None)
        return value is not None

    def can_compute_kpis(self) -> bool:
        return self.has("sales") and self.has("profit")

    def can_analyze_category(self) -> bool:
        return self.has("category")

    def can_analyze_sub_category(self) -> bool:
        return self.has("sub_category")

    def can_analyze_region(self) -> bool:
        return self.has("region")

    def can_analyze_segment(self) -> bool:
        return self.has("segment")

    def can_analyze_discount(self) -> bool:
        return self.has("discount")

    def can_analyze_orders(self) -> bool:
        return self.has("order_id")

    def can_analyze_time(self) -> bool:
        return self.has("year")

    def summary(self):
        """
        Returns all detected capabilities.
        """
        return {
            "kpis": self.can_compute_kpis(),
            "category": self.can_analyze_category(),
            "sub_category": self.can_analyze_sub_category(),
            "region": self.can_analyze_region(),
            "segment": self.can_analyze_segment(),
            "discount": self.can_analyze_discount(),
            "orders": self.can_analyze_orders(),
            "time": self.can_analyze_time(),
        }
