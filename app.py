import streamlit as st
import pandas as pd
import plotly.express as px

from src.metrics_engine import compute_advanced_metrics
from src.ai_reasoning import summarize_business, generate_executive_summary, answer_business_question

st.set_page_config(page_title="AI Business Analyst Copilot", layout="wide")

st.title("AI-Driven Business Analyst Copilot")
st.markdown("Upload your dataset and get structured business insights")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    metrics = compute_advanced_metrics(df)
    summary = summarize_business(metrics)

    st.divider()

    st.header("📊 Business Health Overview")
    col1, col2, col3 = st.columns(3)

    col1.metric("Health Score", summary["health_score"])
    col2.metric("Profit Margin (%)", summary["profit_margin_pct"])
    col3.metric("Loss Order (%)", summary["loss_order_pct"])

    st.divider()

    st.header("⚠ Structural Risk Diagnostics")

    st.subheader("Structural Inefficiency by Category")
    st.dataframe(metrics["structural_inefficiency_by_category"])

    ineff = metrics["structural_inefficiency_by_category"]

    fig = px.bar(
        ineff,
        x="category",
        y="avg_loss_ratio",
        title="Average Loss Ratio by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Structural Collapse by Category")
    st.dataframe(metrics["structural_collapse_by_category"])

    st.divider()

    st.subheader("Risk Analysis")
    st.write(f"Highest Risk Category: **{summary['highest_risk_category']}**")
    st.write(f"Loss Ratio: **{summary['highest_loss_ratio']}%**")
    st.write(f"Risk Level: **{summary['risk_level']}**")

    st.subheader("🧠 Executive Summary")
    st.info(generate_executive_summary(summary))

    st.subheader("❓ Ask a Business Question")

    user_question = st.text_input("Type your question")

    if user_question:
        answer = answer_business_question(user_question, metrics)
        st.write("### 💬 Answer:")
        st.write(answer)
