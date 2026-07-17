import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


import pandas as pd
import plotly.express as px
import streamlit as st

from app.services.analysis_service import AnalysisService
from app.services.summary_service import (
    answer_business_question,
    
)

st.set_page_config(page_title="AI Business Analyst Copilot", layout="wide")

st.title("Enterprise AI Business Copilot")
st.markdown("Upload your dataset and get structured business insights")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    result = AnalysisService.analyze(df)

    metrics = result["metrics"]
    summary = result["summary"]
    ai_summary = result["ai_summary"]

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

    st.subheader("🤖 Ai Executive Summary")
    st.info(ai_summary)

    st.subheader("❓ Ask a Business Question")

    user_question = st.text_input("Type your question")

    if user_question:
        answer = answer_business_question(user_question, metrics)
        st.write("### 💬 Answer:")
        st.write(answer)
