import streamlit as st


def format_currency(value: float) -> str:
    """Format large currency values."""
    if value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"

    if value >= 1_000:
        return f"${value / 1_000:.2f}K"

    return f"${value:.2f}"


def display_metrics(metrics: dict):
    """
    Display KPI cards.
    """

    kpis = metrics["kpis"]

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Revenue",
            format_currency(kpis["total_revenue"]),
        )

    with col2:
        st.metric(
            "Profit",
            format_currency(kpis["total_profit"]),
        )

    with col3:
        st.metric(
            "Profit Margin",
            f'{kpis["profit_margin_pct"]:.2f}%',
        )

    with col4:
        st.metric(
            "Orders",
            f'{kpis["total_orders"]:,}',
        )

    with col5:
        st.metric(
            "Health Score",
            f'{metrics["business_health"]["health_score"]:.2f}',
        )
