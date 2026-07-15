import pandas as pd

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
def compute_kpis(df: pd.DataFrame) -> dict:
    df = normalize_columns(df)

    total_revenue = df["sales"].sum()
    total_profit = df["profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100

    total_orders = df["order_id"].nunique()
    loss_orders = df[df["profit"] < 0]["order_id"].nunique()
    loss_order_pct = (loss_orders / total_orders) * 100

    return {
        "total_revenue": round(total_revenue, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin_pct": round(profit_margin, 2),
        "total_orders": total_orders,
        "loss_order_pct": round(loss_order_pct, 2)
    }


# ---------------------------
# Day 3 – Helper functions
# ---------------------------
def profit_by_dimension(df: pd.DataFrame, column: str) -> pd.DataFrame:
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataframe")

    summary = (
        df.groupby(column)
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum")
        )
        .reset_index()
    )

    summary["profit_margin_pct"] = (
        summary["total_profit"] / summary["total_sales"] * 100
    )

    return summary.sort_values("total_profit")


def worst_performers(df: pd.DataFrame) -> dict:
    return {
        "worst_category": profit_by_dimension(df, "category").iloc[0]["category"],
        "worst_sub_category": profit_by_dimension(df, "sub_category").iloc[0]["sub_category"],
        "worst_region": profit_by_dimension(df, "region").iloc[0]["region"],
        "worst_segment": profit_by_dimension(df, "segment").iloc[0]["segment"],
    }


def discount_profit_analysis(df: pd.DataFrame) -> pd.DataFrame:
    bins = [-0.01, 0.10, 0.20, 0.30, 1.0]
    labels = ["0-10%", "10-20%", "20-30%", "30%+"]

    df = df.copy()
    df["discount_bucket"] = pd.cut(df["discount"], bins=bins, labels=labels)

    summary = (
        df.groupby("discount_bucket")
        .agg(
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            order_count=("order_id", "nunique")
        )
        .reset_index()
    )

    summary["profit_margin_pct"] = (
        summary["total_profit"] / summary["total_sales"] * 100
    )

    return summary


def high_sales_negative_profit(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)

    sales_threshold = df["sales"].median()

    return df[
        (df["sales"] > sales_threshold) &
        (df["profit"] < 0)
    ][["order_id", "sales", "profit", "discount", "category", "sub_category"]]


# ---------------------------
# Day 3 – Main aggregator
# ---------------------------
def compute_advanced_metrics(df: pd.DataFrame) -> dict:
    df = normalize_columns(df)
    metrics = {}

# --- Core breakdowns ---
    metrics["profit_by_category"] = profit_by_dimension(df, "category")
    metrics["profit_by_sub_category"] = profit_by_dimension(df, "sub_category")
    metrics["profit_by_region"] = profit_by_dimension(df, "region")
    metrics["profit_by_segment"] = profit_by_dimension(df, "segment")

# --- Diagnostic insights ---
    metrics["worst_performers"] = worst_performers(df)
    metrics["discount_analysis"] = discount_profit_analysis(df)
    metrics["high_sales_negative_profit"] = high_sales_negative_profit(df)

# --- Validation layer (Day 4) ---
    metrics["structural_collapse_by_category"] = consistency_analysis(df, "category")
    metrics["structural_inefficiency_by_category"] = order_loss_consistency(df, "category")

# --- Executive scoring ---
    metrics["business_health"] = profit_health_score(df)

    return metrics



def consistency_analysis(df: pd.DataFrame, dimension: str, time_col: str = "year") -> pd.DataFrame:
    df = normalize_columns(df)

    if dimension not in df.columns or time_col not in df.columns:
        raise ValueError("Invalid dimension or time column")

    summary = (
        df.groupby([dimension, time_col])
        .agg(total_profit=("profit", "sum"))
        .reset_index()
    )

    summary["is_loss"] = summary["total_profit"] < 0

    consistency = (
        summary.groupby(dimension)
        .agg(
            loss_periods=("is_loss", "sum"),
            total_periods=(time_col, "nunique"),
            avg_profit=("total_profit", "mean")
        )
        .reset_index()
    )

    consistency["loss_consistency_ratio"] = (
        consistency["loss_periods"] / consistency["total_periods"]
    )

    return consistency.sort_values("loss_consistency_ratio", ascending=False)


def profit_health_score(df: pd.DataFrame) -> dict:
    kpis = compute_kpis(df)

    score = 100

    # Weighted penalties
    score -= max(0, -kpis["profit_margin_pct"]) * 2
    score -= max(0, kpis["loss_order_pct"] - 15) * 1.5

    return {
        "health_score": round(max(score, 0), 2),
        "profit_margin_pct": kpis["profit_margin_pct"],
        "loss_order_pct": kpis["loss_order_pct"]
    }


def order_loss_consistency(
    df: pd.DataFrame,
    dimension: str,
    time_col: str = "year"
) -> pd.DataFrame:

    df = normalize_columns(df)

    summary = (
        df.groupby([dimension, time_col])
        .agg(
            total_orders=("order_id", "nunique"),
            loss_orders=("profit", lambda x: (x < 0).sum())
        )
        .reset_index()
    )

    summary["loss_order_ratio"] = (
        summary["loss_orders"] / summary["total_orders"]
    )

    consistency = (
        summary.groupby(dimension)
        .agg(
            avg_loss_ratio=("loss_order_ratio", "mean"),
            std_loss_ratio=("loss_order_ratio", "std"),
            periods_analyzed=(time_col, "nunique")
        )
        .reset_index()
    )

    # Handle NaN std (happens if only 1 period exists)
    consistency["std_loss_ratio"] = consistency["std_loss_ratio"].fillna(0)

    # Stability classification
    consistency["stability"] = consistency["std_loss_ratio"].apply(
        lambda x: "Stable"
        if x < 0.05
        else "Moderate"
        if x < 0.15
        else "Unstable"
    )

    return consistency.sort_values("avg_loss_ratio", ascending=False)




