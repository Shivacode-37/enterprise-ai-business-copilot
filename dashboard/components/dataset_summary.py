import streamlit as st


def format_size(size_bytes: int) -> str:
    """
    Convert file size to a readable format.
    """
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"

    if size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"

    return f"{size_bytes} Bytes"


def display_dataset_summary(uploaded_file):
    """
    Display uploaded file information.
    """

    st.subheader("📂 Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("File Name", uploaded_file.name)

    with col2:
        st.metric("File Size", format_size(uploaded_file.size))

    with col3:
        st.metric("File Type", "CSV")

    st.divider()
