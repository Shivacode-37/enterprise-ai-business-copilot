import time

import streamlit as st

from api import analyze_csv
from components.charts import display_charts
from components.dataset_summary import display_dataset_summary
from components.download import download_report
from components.footer import render_footer
from components.header import render_header
from components.metrics import display_metrics
from components.report import display_report
from components.sidebar import render_sidebar
from components.timer import display_analysis_time

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Enterprise AI Business Copilot",
    page_icon="📊",
    layout="wide",
)

# ----------------------------------------------------
# Header & Sidebar
# ----------------------------------------------------

render_header()
render_sidebar()

# ----------------------------------------------------
# File Upload
# ----------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Business CSV",
    type=["csv"],
)

if uploaded_file:

    # ------------------------------------------------
    # Dataset Summary
    # ------------------------------------------------

    with st.container(border=True):
        display_dataset_summary(uploaded_file)

    st.write("")

    # ------------------------------------------------
    # Analyze Button
    # ------------------------------------------------

    if st.button(
        "🚀 Analyze Business",
        use_container_width=True,
        type="primary",
    ):

        start_time = time.perf_counter()

        with st.spinner("Analyzing business data..."):

            try:

                result = analyze_csv(uploaded_file)

                elapsed_time = (
                    time.perf_counter() - start_time
                )

                # ------------------------------------
                # KPI Section
                # ------------------------------------

                with st.container(border=True):

                    st.subheader(
                        "📈 Key Performance Indicators"
                    )

                    st.caption(
                        "Financial health and operational performance metrics."
                    )

                    display_metrics(result["metrics"])

                st.write("")

                # ------------------------------------
                # Charts
                # ------------------------------------

                with st.container(border=True):

                    st.subheader("📊 Business Analytics")

                    st.caption(
                        "Interactive visualizations of business performance."
                    )

                    display_charts(result["metrics"])

                st.write("")

                # ------------------------------------
                # AI Report
                # ------------------------------------

                with st.container(border=True):

                    st.subheader(
                        "📄 AI Executive Business Report"
                    )

                    st.caption(
                        "AI-generated executive summary and strategic recommendations."
                    )

                    display_report(
                        result["executive_report"]
                    )

                    st.write("")

                    download_report(
                        result["executive_report"]
                    )

                st.write("")

                # ------------------------------------
                # Timer
                # ------------------------------------

                display_analysis_time(elapsed_time)

            except Exception as e:

                st.error(f"❌ Analysis Failed\n\n{e}")

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

render_footer()
