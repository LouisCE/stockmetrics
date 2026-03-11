"""
Stock Explorer page.

Interactive exploration of prices and returns for each ticker.
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.config import DEFAULT_VERSION, get_paths
from src.data_processing import load_clean_prices_latest
from src.viz import hist_returns, line_prices, line_returns


@st.cache_data(show_spinner=False)
def load_prices(version: str):
    paths = get_paths(version)
    df = load_clean_prices_latest(paths.processed_dir, version)
    df = df.sort_values(["Date", "Ticker"]).reset_index(drop=True)
    return df


def render() -> None:
    st.title("🔎 Stock Explorer")

    version = st.selectbox("Data version", options=[DEFAULT_VERSION], index=0)

    df = load_prices(version)

    tickers = sorted(df["Ticker"].unique().tolist())
    ticker = st.selectbox("Select ticker", options=tickers)

    ticker_df = df[df["Ticker"] == ticker].copy()
    min_date = ticker_df["Date"].min().date()
    max_date = ticker_df["Date"].max().date()

    date_range = st.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date

    filtered_df = df[
        (df["Ticker"] == ticker)
        & (df["Date"].dt.date >= start_date)
        & (df["Date"].dt.date <= end_date)
    ].copy()

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Rows", f"{len(filtered_df):,}")
    with c2:
        st.metric("Ticker", ticker)
    with c3:
        st.metric("Date range", f"{start_date} → {end_date}")

    st.divider()

    tab1, tab2, tab3 = st.tabs(["Prices", "Returns", "Distribution"])

    with tab1:
        st.plotly_chart(line_prices(filtered_df, ticker), use_container_width=True)
        st.caption(
            "This chart shows how the adjusted price changed over the selected time period."
        )

    with tab2:
        st.plotly_chart(line_returns(filtered_df, ticker), use_container_width=True)
        st.caption(
            "Daily returns show day-to-day volatility. Short-term noise is normal."
        )

    with tab3:
        st.plotly_chart(hist_returns(filtered_df, ticker), use_container_width=True)
        st.caption(
            "The distribution helps show which daily return outcomes were most common "
            "and which were more extreme."
        )

    st.caption(
        "Charts are based on the cleaned dataset in data/processed/<version>/ "
        "and are intended for education, not trading signals."
    )
