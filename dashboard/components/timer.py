import streamlit as st


def display_analysis_time(elapsed_time: float):
    """
    Display the total analysis time.
    """

    st.success(
        f"✅ Analysis completed in {elapsed_time:.2f} seconds"
    )
