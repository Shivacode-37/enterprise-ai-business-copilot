import pandas as pd
import plotly.express as px
import streamlit as st


def display_charts(metrics: dict):

    # -----------------------------
    # DataFrames
    # -----------------------------

    category_df = pd.DataFrame(metrics["profit_by_category"])
    region_df = pd.DataFrame(metrics["profit_by_region"])
    segment_df = pd.DataFrame(metrics["profit_by_segment"])
    discount_df = pd.DataFrame(metrics["discount_analysis"])

    col1, col2 = st.columns(2)

    # -----------------------------
    # Category
    # -----------------------------

    with col1:

        fig = px.bar(
            category_df,
            x="category",
            y="total_profit",
            color="category",
            title="Profit by Category",
        )

        st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Region
    # -----------------------------

    with col2:

        fig = px.bar(
            region_df,
            x="region",
            y="total_profit",
            color="region",
            title="Profit by Region",
        )

        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)

    # -----------------------------
    # Segment
    # -----------------------------

    with col3:

        fig = px.pie(
            segment_df,
            values="total_sales",
            names="segment",
            title="Sales by Segment",
        )

        st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Discount
    # -----------------------------

    with col4:

        fig = px.bar(
            discount_df,
            x="discount_bucket",
            y="profit_margin_pct",
            color="discount_bucket",
            title="Discount vs Profit Margin",
        )

        st.plotly_chart(fig, use_container_width=True)
