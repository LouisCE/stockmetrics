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

PAGES = {
    "🏁 Home": home_page,
    "🔎 Stock Explorer": stock_explorer_page,
    "🎯 Predictor": predictor_page,
    "💼 Portfolio Plans": portfolio_plans_page,
    "🧪 Model Performance": model_performance_page,
}

with st.sidebar:
    st.title("📈 StockMetrics")
    st.caption("Clueless to confident in fifteen minutes")

    page_name = st.radio(
        "Navigation",
        options=list(PAGES.keys()),
        index=0,
    )

    st.divider()
    st.write("Data/artefacts are versioned (e.g. v1, v2).")
    st.code("data/raw/<version>/\ndata/processed/<version>/\noutputs/<version>/", language="text")

st.container()
PAGES[page_name]()
