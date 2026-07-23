import streamlit as st


def download_report(report: str):
    """
    Download the AI executive report.
    """

    st.download_button(
        label="📥 Download Executive Report",
        data=report,
        file_name="executive_report.md",
        mime="text/markdown",
    )
