import pandas as pd
from app.schema.models import SchemaMapping
from app.schema.column_accessor import ColumnAccessor
from app.schema.capabilities import DatasetCapabilities

# ---------------------------
# Day 2 – Core KPIs
# ---------------------------
def compute_kpis(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict:


    cols = ColumnAccessor(mapping)
    caps = DatasetCapabilities(mapping)

    metrics = {}

    # ---------- Revenue ----------
    if caps.has("sales"):
        metrics["total_revenue"] = round(
            df[cols.sales].sum(),
            2,
        )
    else:
        metrics["total_revenue"] = None

    # ---------- Profit ----------
    if caps.has("profit"):
        metrics["total_profit"] = round(
            df[cols.profit].sum(),
            2,
        )
    else:
        metrics["total_profit"] = None

    # ---------- Profit Margin ----------
    if caps.can_compute_kpis():

        revenue = df[cols.sales].sum()
        profit = df[cols.profit].sum()

        metrics["profit_margin_pct"] = (
            round((profit / revenue) * 100, 2)
            if revenue != 0
            else 0
        )

    else:
        metrics["profit_margin_pct"] = None

    # ---------- Orders ----------
    if caps.can_analyze_orders():

        total_orders = df[cols.order_id].nunique()

        metrics["total_orders"] = total_orders

        if caps.has("profit"):

            loss_orders = (
                df[df[cols.profit] < 0][cols.order_id]
                .nunique()
            )

            metrics["loss_order_pct"] = (
                round((loss_orders / total_orders) * 100, 2)
                if total_orders != 0
                else 0
            )

        else:
            metrics["loss_order_pct"] = None

    else:

        metrics["total_orders"] = None
        metrics["loss_order_pct"] = None

    return metrics
# ---------------------------
# Day 3 – Helper functions
# ---------------------------
def profit_by_dimension(
    df: pd.DataFrame,
    mapping: SchemaMapping,
    dimension: str,
) -> pd.DataFrame:
    # df = normalize_columns(df)
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
    caps = DatasetCapabilities(mapping)

    result = {}

    if caps.can_analyze_category():
        result["worst_category"] = (
            profit_by_dimension(
                df,
                mapping,
                cols.category,
            )
            .iloc[0][cols.category]
        )

    if caps.can_analyze_sub_category():
        result["worst_sub_category"] = (
            profit_by_dimension(
                df,
                mapping,
                cols.sub_category,
            )
            .iloc[0][cols.sub_category]
        )

    if caps.can_analyze_region():
        result["worst_region"] = (
            profit_by_dimension(
                df,
                mapping,
                cols.region,
            )
            .iloc[0][cols.region]
        )

    if caps.can_analyze_segment():
        result["worst_segment"] = (
            profit_by_dimension(
                df,
                mapping,
                cols.segment,
            )
            .iloc[0][cols.segment]
        )

    return result

def high_sales_negative_profit(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> pd.DataFrame | None:

    # df = normalize_columns(df)
    cols = ColumnAccessor(mapping)
    caps = DatasetCapabilities(mapping)

    # Required columns
    required = [
        "sales",
        "profit",
        "order_id",
        "category",
        "sub_category",
    ]

    if not all(caps.has(field) for field in required):
        return None

    sales_threshold = df[cols.sales].median()

    result = df[
        (df[cols.sales] > sales_threshold)
        & (df[cols.profit] < 0)
    ][
        [
            cols.order_id,
            cols.sales,
            cols.profit,
            cols.category,
            cols.sub_category,
        ]
    ]

    # Include discount only if available
    if caps.can_analyze_discount():
        result[cols.discount] = df.loc[
            result.index,
            cols.discount,
        ]

    return result.reset_index(drop=True)



def discount_profit_analysis(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> pd.DataFrame | None:

    # df = normalize_columns(df)
    cols = ColumnAccessor(mapping)
    caps = DatasetCapabilities(mapping)

    # Required columns
    if not (
        caps.can_analyze_discount()
        and caps.has("sales")
        and caps.has("profit")
        and caps.can_analyze_orders()
    ):
        return None

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
        summary["total_profit"]
        / summary["total_sales"]
        * 100
    )

    summary["profit_margin_pct"] = summary[
        "profit_margin_pct"
    ].fillna(0)

    return summary
# ---------------------------
# Day 3 – Main aggregator
# ---------------------------
def compute_advanced_metrics(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict:

    # df = normalize_columns(df)

    cols = ColumnAccessor(mapping)
    caps = DatasetCapabilities(mapping)

    metrics = {}

    # ---------- Core KPIs ----------
    if caps.can_compute_kpis():
        metrics["kpis"] = compute_kpis(
            df,
            mapping,
        )

    # ---------- Profit Breakdowns ----------
    if caps.can_analyze_category():
        metrics["profit_by_category"] = profit_by_dimension(
            df,
            mapping,
            cols.category,
        )

    if caps.can_analyze_sub_category():
        metrics["profit_by_sub_category"] = profit_by_dimension(
            df,
            mapping,
            cols.sub_category,
        )

    if caps.can_analyze_region():
        metrics["profit_by_region"] = profit_by_dimension(
            df,
            mapping,
            cols.region,
        )

    if caps.can_analyze_segment():
        metrics["profit_by_segment"] = profit_by_dimension(
            df,
            mapping,
            cols.segment,
        )

    # ---------- Diagnostic Insights ----------
    worst = worst_performers(
        df,
        mapping,
    )

    if worst:
        metrics["worst_performers"] = worst

    discount = discount_profit_analysis(
        df,
        mapping,
    )

    if discount is not None:
        metrics["discount_analysis"] = discount

    negative_profit = high_sales_negative_profit(
        df,
        mapping,
    )

    if negative_profit is not None:
        metrics["high_sales_negative_profit"] = negative_profit

    # ---------- Validation ----------
    if caps.can_analyze_category():

        collapse = consistency_analysis(
            df,
            mapping,
            cols.category,
        )

        if collapse is not None:
            metrics["structural_collapse_by_category"] = collapse

        inefficiency = order_loss_consistency(
            df,
            mapping,
            cols.category,
        )

        if inefficiency is not None:
            metrics["structural_inefficiency_by_category"] = inefficiency

    # ---------- Executive Score ----------
    health = profit_health_score(
        df,
        mapping,
    )

    if health:
        metrics["business_health"] = health

    return metrics


def consistency_analysis(
    df: pd.DataFrame,
    mapping: SchemaMapping,
    dimension: str,
) -> pd.DataFrame | None:

    # df = normalize_columns(df)
    cols = ColumnAccessor(mapping)
    caps = DatasetCapabilities(mapping)

    if (
        not caps.can_analyze_time()
        or not caps.has("profit")
        or dimension is None
        or dimension not in df.columns
    ):
        return None

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
        consistency["loss_periods"]
        / consistency["total_periods"]
    )

    return consistency.sort_values(
        "loss_consistency_ratio",
        ascending=False,
    )


def profit_health_score(
    df: pd.DataFrame,
    mapping: SchemaMapping,
) -> dict | None:

    kpis = compute_kpis(
        df,
        mapping,
    )

    # Cannot compute health without core KPIs
    if (
        kpis["profit_margin_pct"] is None
        or kpis["loss_order_pct"] is None
    ):
        return None

    score = 100

    # Profit Margin Penalty
    score -= max(
        0,
        -kpis["profit_margin_pct"],
    ) * 2

    # Loss Order Penalty
    score -= max(
        0,
        kpis["loss_order_pct"] - 15,
    ) * 1.5

    return {
        "health_score": round(max(score, 0), 2),
        "profit_margin_pct": kpis["profit_margin_pct"],
        "loss_order_pct": kpis["loss_order_pct"],
    }


def order_loss_consistency(
    df: pd.DataFrame,
    mapping: SchemaMapping,
    dimension: str,
) -> pd.DataFrame | None:

    # df = normalize_columns(df)
    cols = ColumnAccessor(mapping)
    caps = DatasetCapabilities(mapping)

    # Required fields
    if (
        not caps.can_analyze_orders()
        or not caps.can_analyze_time()
        or not caps.has("profit")
        or dimension is None
        or dimension not in df.columns
    ):
        return None

    summary = (
        df.groupby([dimension, cols.year])
        .agg(
            total_orders=(cols.order_id, "nunique"),
            loss_orders=(cols.profit, lambda x: (x < 0).sum()),
        )
        .reset_index()
    )

    summary["loss_order_ratio"] = (
        summary["loss_orders"]
        / summary["total_orders"]
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
