import streamlit as st


def render_header():
    """
    Render the application header.
    """

    col1, col2 = st.columns([5, 1])

    with col1:
        st.title("📊 Enterprise AI Business Copilot")
        st.caption(
            "AI-powered Business Intelligence Dashboard"
        )

    with col2:
        st.success("🟢 Online")

    st.divider()
