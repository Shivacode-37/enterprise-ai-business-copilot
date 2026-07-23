import streamlit as st


def render_sidebar():
    """
    Render application sidebar.
    """

    with st.sidebar:

        st.title("🤖 Enterprise AI")

        st.markdown("---")

        st.markdown(
            """
            ### Features

            ✅ CSV Analysis

            ✅ Business KPIs

            ✅ Interactive Charts

            ✅ AI Executive Report

            """
        )

        st.markdown("---")

        st.info(
            "Upload a business dataset to generate AI-powered insights."
        )
