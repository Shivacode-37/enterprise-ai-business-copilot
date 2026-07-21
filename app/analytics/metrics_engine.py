import pandas as pd
from app.schema.models import SchemaMapping
from app.schema.column_accessor import ColumnAccessor
# ---------------------------
# Column normalization
# ---------------------------
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w]+", "_", regex=True)
    )
    return df


# ---------------------------
# Day 2 – Core KPIs
# ---------------------------
def compute_kpis(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict:
    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    total_revenue = df[cols.sales].sum()
    total_profit = df[cols.profit].sum()
    profit_margin = (total_profit / total_revenue) * 100

    total_orders = df[cols.order_id].nunique()
    loss_orders = df[df[cols.profit] < 0][cols.order_id].nunique()
    loss_order_pct = (loss_orders / total_orders) * 100

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin_pct": round(profit_margin, 2),
        "total_orders": total_orders,
        "loss_order_pct": round(loss_order_pct, 2),
    }


# ---------------------------
# Day 3 – Helper functions
# ---------------------------
def profit_by_dimension(
    df: pd.DataFrame,
    mapping: SchemaMapping,
    dimension: str,
) -> pd.DataFrame:
    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    if dimension not in df.columns:
        raise ValueError(f"Column '{dimension}' not found in dataframe")

    summary = (
        df.groupby(dimension)
        .agg(
            total_sales=(cols.sales, "sum"),
            total_profit=(cols.profit, "sum"),
        )
        .reset_index()
    )

    summary["profit_margin_pct"] = (
        summary["total_profit"] / summary["total_sales"] * 100
    )

    return summary.sort_values("total_profit")


def worst_performers(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict:

    cols = ColumnAccessor(mapping)

    return {
        "worst_category": profit_by_dimension(
            df,
            mapping,
            cols.category,
        ).iloc[0][cols.category],

        "worst_sub_category": profit_by_dimension(
            df,
            mapping,
            cols.sub_category,
        ).iloc[0][cols.sub_category],

        "worst_region": profit_by_dimension(
            df,
            mapping,
            cols.region,
        ).iloc[0][cols.region],

        "worst_segment": profit_by_dimension(
            df,
            mapping,
            cols.segment,
        ).iloc[0][cols.segment],
    }

def high_sales_negative_profit(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> pd.DataFrame:

    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    sales_threshold = df[cols.sales].median()

    return df[
        (df[cols.sales] > sales_threshold)
        & (df[cols.profit] < 0)
    ][
        [
            cols.order_id,
            cols.sales,
            cols.profit,
            cols.discount,
            cols.category,
            cols.sub_category,
        ]
    ]


def discount_profit_analysis(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> pd.DataFrame:

    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    bins = [-0.01, 0.10, 0.20, 0.30, 1.0]
    labels = ["0-10%", "10-20%", "20-30%", "30%+"]

    df = df.copy()

    df["discount_bucket"] = pd.cut(
        df[cols.discount],
        bins=bins,
        labels=labels,
    )

    summary = (
        df.groupby("discount_bucket")
        .agg(
            total_sales=(cols.sales, "sum"),
            total_profit=(cols.profit, "sum"),
            order_count=(cols.order_id, "nunique"),
        )
        .reset_index()
    )

    summary["profit_margin_pct"] = (
        summary["total_profit"] / summary["total_sales"] * 100
    )

    return summary
# ---------------------------
# Day 3 – Main aggregator
# ---------------------------
def compute_advanced_metrics(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict:

    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    metrics = {}

    # ---------- Core Breakdowns ----------
    metrics["profit_by_category"] = profit_by_dimension(
        df,
        mapping,
        cols.category,
    )

    metrics["profit_by_sub_category"] = profit_by_dimension(
        df,
        mapping,
        cols.sub_category,
    )

    metrics["profit_by_region"] = profit_by_dimension(
        df,
        mapping,
        cols.region,
    )

    metrics["profit_by_segment"] = profit_by_dimension(
        df,
        mapping,
        cols.segment,
    )

    # ---------- Diagnostic Insights ----------
    metrics["worst_performers"] = worst_performers(
        df,
        mapping,
    )

    metrics["discount_analysis"] = discount_profit_analysis(
        df,
        mapping,
    )

    metrics["high_sales_negative_profit"] = high_sales_negative_profit(
        df,
        mapping,
    )

    # ---------- Validation Layer ----------
    metrics["structural_collapse_by_category"] = consistency_analysis(
        df,
        mapping,
        cols.category,
    )

    metrics["structural_inefficiency_by_category"] = order_loss_consistency(
        df,
        mapping,
        cols.category,
    )

    # ---------- Executive Score ----------
    metrics["business_health"] = profit_health_score(
        df,
        mapping,
    )

    return metrics

def consistency_analysis(
    df: pd.DataFrame,
    mapping: SchemaMapping,
    dimension: str,
) -> pd.DataFrame:

    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    if dimension not in df.columns:
        raise ValueError(f"Column '{dimension}' not found")

    if cols.year is None:
        raise ValueError("Year column not detected")

    summary = (
        df.groupby([dimension, cols.year])
        .agg(total_profit=(cols.profit, "sum"))
        .reset_index()
    )

    summary["is_loss"] = summary["total_profit"] < 0

    consistency = (
        summary.groupby(dimension)
        .agg(
            loss_periods=("is_loss", "sum"),
            total_periods=(cols.year, "nunique"),
            avg_profit=("total_profit", "mean"),
        )
        .reset_index()
    )

    consistency["loss_consistency_ratio"] = (
        consistency["loss_periods"] /
        consistency["total_periods"]
    )

    return consistency.sort_values(
        "loss_consistency_ratio",
        ascending=False,
    )


def profit_health_score(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict:

    kpis = compute_kpis(
        df,
        mapping,
    )

    score = 100

    # Weighted penalties
    score -= max(0, -kpis["profit_margin_pct"]) * 2
    score -= max(0, kpis["loss_order_pct"] - 15) * 1.5

    return {
        "health_score": round(max(score, 0), 2),
        "profit_margin_pct": kpis["profit_margin_pct"],
        "loss_order_pct": kpis["loss_order_pct"],
    }
def order_loss_consistency(
    df: pd.DataFrame,
    mapping: SchemaMapping,
    dimension: str,
) -> pd.DataFrame:

    df = normalize_columns(df)
    cols = ColumnAccessor(mapping)

    if dimension not in df.columns:
        raise ValueError(f"Column '{dimension}' not found")

    if cols.year is None:
        raise ValueError("Year column not detected")

    summary = (
        df.groupby([dimension, cols.year])
        .agg(
            total_orders=(cols.order_id, "nunique"),
            loss_orders=(cols.profit, lambda x: (x < 0).sum()),
        )
        .reset_index()
    )

    summary["loss_order_ratio"] = (
        summary["loss_orders"] /
        summary["total_orders"]
    )

    consistency = (
        summary.groupby(dimension)
        .agg(
            avg_loss_ratio=("loss_order_ratio", "mean"),
            std_loss_ratio=("loss_order_ratio", "std"),
            periods_analyzed=(cols.year, "nunique"),
        )
        .reset_index()
    )

    consistency["std_loss_ratio"] = (
        consistency["std_loss_ratio"]
        .fillna(0)
    )

    consistency["stability"] = consistency[
        "std_loss_ratio"
    ].apply(
        lambda x: (
            "Stable"
            if x < 0.05
            else "Moderate"
            if x < 0.15
            else "Unstable"
        )
    )

    return consistency.sort_values(
        "avg_loss_ratio",
        ascending=False,
    )
