"""
Portfolio Plans page.

Compares the four risk-based plans using historical daily returns.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.config import (
    DEFAULT_VERSION,
    PLAN_DESCRIPTIONS,
    TICKER_DISPLAY_NAMES,
    get_paths,
)
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


def render_plan_boxes(selected_plan: str) -> None:
    """Render four beginner-friendly coloured plan boxes."""
    col1, col2, col3, col4 = st.columns(4)

    plans = list(PLAN_WEIGHTS.keys())

    with col1:
        label = "✅ Selected" if plans[0] == selected_plan else ""
        st.info(
            f"**{plans[0]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[0]]}\n\n"
            f"{label}"
        )

    with col2:
        label = "✅ Selected" if plans[1] == selected_plan else ""
        st.success(
            f"**{plans[1]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[1]]}\n\n"
            f"{label}"
        )

    with col3:
        label = "✅ Selected" if plans[2] == selected_plan else ""
        st.warning(
            f"**{plans[2]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[2]]}\n\n"
            f"{label}"
        )

    with col4:
        label = "✅ Selected" if plans[3] == selected_plan else ""
        st.error(
            f"**{plans[3]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[3]]}\n\n"
            f"{label}"
        )


def render() -> None:
    st.title("💼 Portfolio Plans")

    version = st.selectbox("Data version", options=[DEFAULT_VERSION], index=0)
    plan_name = st.selectbox("Select plan", options=list(PLAN_WEIGHTS.keys()))

    st.markdown(
        """
### What's your appetite for risk?

In StockMetrics, these risk labels are **relative to each other**.
They describe how concentrated each plan is, not whether investing is
ever risk-free.

A more concentrated plan may offer higher potential upside, but it may
also experience larger drawdowns and a bumpier ride.
"""
    )

    render_plan_boxes(plan_name)

    st.divider()

    returns = load_returns(version)
    weights = PLAN_WEIGHTS[plan_name]
    plan_ret = build_plan_returns(returns, weights)
    metrics = compute_plan_metrics(plan_ret)

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Mean daily return", f"{metrics.mean_daily_return:.4f}")
    c2.metric("Daily volatility", f"{metrics.daily_volatility:.4f}")
    c3.metric("Ann. return (approx)", f"{metrics.annualised_return_approx:.2f}")
    c4.metric(
        "Ann. volatility (approx)",
        f"{metrics.annualised_volatility_approx:.2f}",
    )
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
        "This chart shows how £1 would have grown historically under the "
        "selected plan. It helps illustrate the trade-off between "
        "diversification, concentration, and volatility."
    )

    st.subheader("Your selected plan")
    st.write(
        "This table shows the assets included in the selected plan and "
        "their target weights."
    )

    plan_table = pd.DataFrame(
        [
            {
                "Ticker": ticker,
                "Name": TICKER_DISPLAY_NAMES.get(ticker, ticker),
                "Weight (%)": round(weight * 100, 2),
            }
            for ticker, weight in weights.items()
        ]
    )

    st.dataframe(plan_table, use_container_width=True)

    st.caption(
        "This is your selected plan. It is shown for educational comparison "
        "only and is not a personal investment recommendation."
    )

    st.info(
        "Educational use only. These plans illustrate risk trade-offs and "
        "are not personal investment recommendations."
    )
