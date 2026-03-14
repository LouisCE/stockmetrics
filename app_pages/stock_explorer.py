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
def load_prices(version: str) -> pd.DataFrame:
    """Load the cleaned prices dataset for the selected version."""
    paths = get_paths(version)
    df = load_clean_prices_latest(paths.processed_dir, version)
    df = df.sort_values(["Date", "Ticker"]).reset_index(drop=True)
    return df


def get_asset_summaries() -> dict[str, tuple[str, str]]:
    """Return beginner-friendly titles and summaries for all assets."""
    return {
        "AAPL": (
            "What is Apple?",
            "Apple is a global technology company best known for the iPhone, "
            "Mac, iPad, Apple Watch, and services such as iCloud and the App "
            "Store. Investors often watch Apple because of its strong brand, "
            "large profits, and loyal customer base.",
        ),
        "AMZN": (
            "What is Amazon?",
            "Amazon is a major technology and e-commerce company. It makes "
            "money from online shopping, cloud computing through AWS, digital "
            "services, and advertising. Investors often track Amazon because "
            "it operates in several large and growing industries.",
        ),
        "GOOGL": (
            "What is Alphabet (Class A)?",
            "Alphabet is the parent company of Google. Its business includes "
            "search, YouTube, digital advertising, cloud services, and AI. "
            "Investors often follow Alphabet because advertising revenue and "
            "technology innovation play a major role in its performance.",
        ),
        "META": (
            "What is Meta Platforms?",
            "Meta owns Facebook, Instagram, WhatsApp, and other digital "
            "platforms. It earns much of its revenue from advertising and is "
            "also investing heavily in AI and virtual reality. Investors "
            "watch Meta because user growth and advertising demand can "
            "strongly affect profits.",
        ),
        "MSFT": (
            "What is Microsoft?",
            "Microsoft is a large technology company known for Windows, "
            "Office, Azure cloud computing, LinkedIn, and other business "
            "software. Investors often see Microsoft as a major blue-chip "
            "company with strong recurring revenue and broad business "
            "diversification.",
        ),
        "NVDA": (
            "What is Nvidia?",
            "Nvidia designs advanced computer chips used in gaming, data "
            "centres, and artificial intelligence. It has become especially "
            "important in the AI boom. Investors follow Nvidia closely "
            "because demand for its chips can drive very rapid growth, but "
            "also higher volatility.",
        ),
        "TSLA": (
            "What is Tesla?",
            "Tesla is an electric vehicle and clean energy company. It is "
            "also closely associated with themes such as innovation, "
            "automation, and AI. Investors often view Tesla as a "
            "high-growth but highly volatile stock, meaning its price can "
            "move sharply.",
        ),
        "VUSA.L": (
            "What is the S&P 500 ETF?",
            "VUSA.L is Vanguard's S&P 500 UCITS ETF. It tracks the S&P 500, "
            "which includes 500 of the largest publicly traded companies in "
            "the United States. Investors use it as a simple way to gain "
            "broad exposure to the US stock market.",
        ),
        "VWRL.L": (
            "What is the All-World ETF?",
            "VWRL.L is Vanguard's FTSE All-World UCITS ETF. It provides "
            "exposure to a broad mix of companies across developed and "
            "emerging markets. Investors often use it as a simple example of "
            "global diversification in one fund.",
        ),
    }


def render_asset_guide() -> None:
    """Render a beginner-friendly guide to all included assets."""
    summaries = get_asset_summaries()

    st.divider()
    st.subheader("Know your assets")
    st.markdown(
        "Investors should have a basic understanding of the companies or "
        "funds they invest in so they can better understand what may drive "
        "profits, losses, and price movements."
    )

    ordered_tickers = [
        "AAPL",
        "AMZN",
        "GOOGL",
        "META",
        "MSFT",
        "NVDA",
        "TSLA",
        "VUSA.L",
        "VWRL.L",
    ]

    for ticker in ordered_tickers:
        title, summary = summaries[ticker]
        with st.expander(title):
            st.write(summary)


def render() -> None:
    """Render the Stock Explorer page."""
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
            "This chart shows how the adjusted price changed over the selected "
            "time period."
        )

    with tab2:
        st.plotly_chart(line_returns(filtered_df, ticker), use_container_width=True)
        st.caption(
            "Daily returns show day-to-day volatility. Short-term noise is "
            "normal."
        )

    with tab3:
        st.plotly_chart(hist_returns(filtered_df, ticker), use_container_width=True)
        st.caption(
            "The distribution helps show which daily return outcomes were "
            "most common and which were more extreme."
        )

    st.caption(
        "Charts are based on the cleaned dataset in "
        "data/processed/<version>/ and are intended for education, not "
        "trading signals."
    )

    render_asset_guide()
