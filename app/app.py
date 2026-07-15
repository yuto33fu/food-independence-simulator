"""Minimal Streamlit entry point for the Food Independence Simulator."""

from __future__ import annotations

import streamlit as st

PROJECT_TITLE = "Food Independence Simulator"
PROJECT_SUBTITLE = "Phase 0"
PROJECT_MESSAGE = "Project Foundation Initialized"


def initialize_app() -> None:
    """Render the initial placeholder interface for Phase 0."""
    st.set_page_config(page_title=PROJECT_TITLE, page_icon="🌾")
    st.title(PROJECT_TITLE)
    st.subheader(PROJECT_SUBTITLE)
    st.write(PROJECT_MESSAGE)


if __name__ == "__main__":
    initialize_app()
