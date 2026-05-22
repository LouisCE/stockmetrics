"""
StockMetrics Streamlit app entrypoint.

Navigation is defined here so dashboard pages can live in app_pages/
as small, testable modules with a render() function.
"""

from __future__ import annotations

import streamlit as st

from app_pages.home import render as home_page
from app_pages.stock_explorer import render as stock_explorer_page
from app_pages.predictor import render as predictor_page
from app_pages.portfolio_plans import render as portfolio_plans_page
from app_pages.model_performance import render as model_performance_page

st.set_page_config(
    page_title="StockMetrics",
    page_icon="📈",
    layout="centered",
)

# Define the available pages and their render functions
PAGES = {
    "🏁 Home": home_page,
    "🔎 Stock Explorer": stock_explorer_page,
    "🎯 Predictor": predictor_page,
    "💼 Portfolio Plans": portfolio_plans_page,
    "🧪 Model Performance": model_performance_page,
}

with st.sidebar:
    st.title("📈 StockMetrics")

    # StockMetrics tagline
    st.markdown("*Clueless to confident in fifteen minutes*")

    # Divider to separate tagline from navigation
    st.divider()

    # Navigation
    page_name = st.radio(
        "Navigation",
        options=list(PAGES.keys()),
        index=0,
    )

    # Divider to separate navigation from legal info
    st.divider()

    # Legal disclaimer
    st.warning(
        "**Disclaimer:**\n"
        "- StockMetrics is for educational use only, not financial advice.\n"
        "- Forecasts show scenarios and uncertainty, not guaranteed "
        "outcomes.\n"
        "- Do your own research; **your capital is at risk.**",
        icon="⚠️",
    )


# Render persistent footer across all pages
def render_footer() -> None:
    st.divider()
    st.caption("StockMetrics © 2026. All rights reserved.")
    st.caption(
        "This site was developed by Louis Cowell-English as part of a "
        "Portfolio Project for educational use."
    )
    st.link_button(
        "View the project on GitHub",
        "https://github.com/LouisCE/stockmetrics",
    )


with st.container():
    PAGES[page_name]()  # Page content

render_footer()     # Footer content
