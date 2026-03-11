"""
Portfolio Plans page.

Compares the four risk-based plans using historical daily returns.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.config import DEFAULT_VERSION, get_paths
from src.data_processing import load_clean_prices_latest
from src.portfolio import (
    PLAN_WEIGHTS,
    build_plan_returns,
    compute_plan_metrics,
    daily_returns_from_prices,
    price_wide,
)


@st.cache_data(show_spinner=False)
def load_returns(version: str) -> pd.DataFrame:
    paths = get_paths(version)
    clean_df = load_clean_prices_latest(paths.processed_dir, version)
    prices = price_wide(clean_df)
    return daily_returns_from_prices(prices)


def render() -> None:
    st.title("💼 Portfolio Plans")

    version = st.selectbox("Data version", options=[DEFAULT_VERSION], index=0)
    plan_name = st.selectbox("Select plan", options=list(PLAN_WEIGHTS.keys()))

    returns = load_returns(version)
    weights = PLAN_WEIGHTS[plan_name]
    plan_ret = build_plan_returns(returns, weights)
    metrics = compute_plan_metrics(plan_ret)

    st.markdown(
        """
### What's your appetite for risk?

In StockMetrics, these risk labels are **relative to each other**.
They describe how concentrated each plan is, not whether investing is ever risk-free.

A more concentrated plan may offer higher potential upside,
but it may also experience larger drawdowns and a bumpier ride.
"""
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Mean daily return", f"{metrics.mean_daily_return:.4f}")
    c2.metric("Daily volatility", f"{metrics.daily_volatility:.4f}")
    c3.metric("Ann. return (approx)", f"{metrics.annualised_return_approx:.2f}")
    c4.metric("Ann. volatility (approx)", f"{metrics.annualised_volatility_approx:.2f}")
    c5.metric("Max drawdown", f"{metrics.max_drawdown:.2%}")

    st.divider()

    equity = (1 + plan_ret.fillna(0)).cumprod()
    equity_df = equity.rename("equity").reset_index()
    equity_df.columns = ["Date", "Equity"]

    fig = px.line(
        equity_df,
        x="Date",
        y="Equity",
        title=f"{plan_name} — Growth of £1 (historical)",
    )
    fig.update_layout(yaxis_title="Equity curve", xaxis_title="Date")
    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        "This chart shows how £1 would have grown historically under the selected plan. "
        "It helps illustrate the trade-off between diversification, concentration, and volatility."
    )

    st.subheader("Plan composition")
    st.write("Weights (renormalised if tickers are missing):")
    st.json(weights)

    st.info(
        "Educational use only. These plans illustrate risk trade-offs and are not "
        "personal investment recommendations."
    )
