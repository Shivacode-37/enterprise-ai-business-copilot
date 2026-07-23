import pandas as pd

def _safe_float(value):
    """Safely convert numeric values to float."""
    if value is None:
        return None

    try:
        value = float(value)
        return round(value, 2)
    except Exception:
        return None


def _safe_int(value):



    """Safely convert numeric values to int."""
    if value is None:
        return None

    try:
        return int(value)
    except Exception:
        return None


def _build_dimension_context(
    df: pd.DataFrame,
    dimension_col: str,
) -> dict | None:
    """
    Build executive context for a business dimension
    (Category, Region, Segment, etc.).
    """

    if df is None or df.empty:
        return None

    best_profit = df.loc[df["total_profit"].idxmax()]
    worst_profit = df.loc[df["total_profit"].idxmin()]

    best_margin = df.loc[df["profit_margin_pct"].idxmax()]
    worst_margin = df.loc[df["profit_margin_pct"].idxmin()]

    return {
        "best_profit": {
            "name": best_profit[dimension_col],
            "total_sales": _safe_float(best_profit["total_sales"]),
            "total_profit": _safe_float(best_profit["total_profit"]),
            "profit_margin_pct": _safe_float(best_profit["profit_margin_pct"]),
        },
        "worst_profit": {
            "name": worst_profit[dimension_col],
            "total_sales": _safe_float(worst_profit["total_sales"]),
            "total_profit": _safe_float(worst_profit["total_profit"]),
            "profit_margin_pct": _safe_float(worst_profit["profit_margin_pct"]),
        },
        "highest_margin": {
            "name": best_margin[dimension_col],
            "profit_margin_pct": _safe_float(best_margin["profit_margin_pct"]),
        },
        "lowest_margin": {
            "name": worst_margin[dimension_col],
            "profit_margin_pct": _safe_float(worst_margin["profit_margin_pct"]),
        },
    }

def build_category_context(metrics: dict) -> dict | None:
    """
    Build executive category context.
    """

    return _build_dimension_context(
        metrics.get("profit_by_category"),
        dimension_col="category",
    )
def build_kpi_context(metrics: dict) -> dict | None:
    """
    Build executive KPI context.
    """

    kpis = metrics.get("kpis")

    if not kpis:
        return None

    return {
        "total_revenue": _safe_float(kpis.get("total_revenue")),
        "total_profit": _safe_float(kpis.get("total_profit")),
        "profit_margin_pct": _safe_float(kpis.get("profit_margin_pct")),
        "total_orders": _safe_int(kpis.get("total_orders")),
        "loss_orders": _safe_int(kpis.get("loss_orders")),
        "loss_order_pct": _safe_float(kpis.get("loss_order_pct")),
    }

def build_region_context(metrics: dict) -> dict | None:
    """
    Build executive region context.
    """

    return _build_dimension_context(
        metrics.get("profit_by_region"),
        dimension_col="region",
    )
def build_segment_context(metrics: dict) -> dict | None:
    """
    Build executive segment context.
    """

    return _build_dimension_context(
        metrics.get("profit_by_segment"),
        dimension_col="segment",
    )

def build_health_context(metrics: dict) -> dict | None:
    """
    Build executive business health context.
    """

    health = metrics.get("business_health")

    if not health:
        return None

    return {
        "health_score": _safe_float(health.get("health_score")),
        "profit_margin_pct": _safe_float(health.get("profit_margin_pct")),
        "loss_order_pct": _safe_float(health.get("loss_order_pct")),
    }

def build_discount_context(metrics: dict) -> dict | None:
    """
    Build executive discount performance context.
    """

    df = metrics.get("discount_analysis")

    if df is None or df.empty:
        return None

    best = df.loc[df["profit_margin_pct"].idxmax()]
    worst = df.loc[df["profit_margin_pct"].idxmin()]

    return {
        "best_discount_band": {
            "range": best["discount_bucket"],
            "profit_margin_pct": _safe_float(best["profit_margin_pct"]),
            "total_profit": _safe_float(best["total_profit"]),
            "order_count": _safe_int(best["order_count"]),
        },
        "worst_discount_band": {
            "range": worst["discount_bucket"],
            "profit_margin_pct": _safe_float(worst["profit_margin_pct"]),
            "total_profit": _safe_float(worst["total_profit"]),
            "order_count": _safe_int(worst["order_count"]),
        },
        "key_insight": (
            f"Profitability decreases as discount levels increase. "
            f"The {best['discount_bucket']} bucket performs best, while "
            f"{worst['discount_bucket']} is significantly unprofitable."
        ),
    }
def build_risk_context(metrics: dict) -> dict | None:
    """
    Build executive structural risk context.
    """

    inefficiency = metrics.get("structural_inefficiency_by_category")
    collapse = metrics.get("structural_collapse_by_category")

    if inefficiency is None or inefficiency.empty:
        return None

    highest_risk = inefficiency.loc[
        inefficiency["avg_loss_ratio"].idxmax()
    ]

    context = {
        "highest_risk_category": {
            "name": highest_risk["category"],
            "avg_loss_ratio": _safe_float(
                highest_risk["avg_loss_ratio"] * 100
            ),
            "stability": highest_risk["stability"],
            "periods_analyzed": _safe_int(
                highest_risk["periods_analyzed"]
            ),
        }
    }

    if collapse is not None and not collapse.empty:
        worst = collapse.loc[
            collapse["loss_consistency_ratio"].idxmax()
        ]

        context["structural_collapse"] = {
            "category": worst["category"],
            "loss_consistency_ratio": _safe_float(
                worst["loss_consistency_ratio"] * 100
            ),
            "loss_periods": _safe_int(worst["loss_periods"]),
            "total_periods": _safe_int(worst["total_periods"]),
        }

    return context
def build_business_context(metrics: dict) -> dict:
    """
    Build a compact, business-friendly context
    for the Executive Report.
    """

    context = {
        "kpis": build_kpi_context(metrics),
        "category": build_category_context(metrics),
        "region": build_region_context(metrics),
        "segment": build_segment_context(metrics),
        "business_health": build_health_context(metrics),
        "discount": build_discount_context(metrics),
        "risk": build_risk_context(metrics),
    }

    return context
