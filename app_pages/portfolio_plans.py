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
            f"🛡️ **{plans[0]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[0]]}\n\n"
            f"{label}"
        )

    with col2:
        label = "✅ Selected" if plans[1] == selected_plan else ""
        st.success(
            f"⚖️ **{plans[1]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[1]]}\n\n"
            f"{label}"
        )

    with col3:
        label = "✅ Selected" if plans[2] == selected_plan else ""
        st.warning(
            f"🧗 **{plans[2]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[2]]}\n\n"
            f"{label}"
        )

    with col4:
        label = "✅ Selected" if plans[3] == selected_plan else ""
        st.error(
            f"🌋 **{plans[3]}**\n\n"
            f"{PLAN_DESCRIPTIONS[plans[3]]}\n\n"
            f"{label}"
        )


def render() -> None:
    st.title("💼 Portfolio Plans")

    st.divider()

    st.header("Compare the four risk-based plans")

    st.write(
        "This page is designed to help you understand how different "
        "portfolio plans would have performed historically, and to show the "
        "trade-offs between diversification, concentration, and volatility. "
        "It's not a recommendation for which plan to choose, but it can help "
        "you see how different approaches might have played out in the past."
    )

    st.image(
        "documentation/dashboard/portfolio_plans_hero.png",
        caption=(
            "The historical resilience of the U.S. stock market against "
            "major global crises from the late 1920s through the early 2020s."
        ),
        use_container_width=True,
    )

    version = DEFAULT_VERSION

    st.divider()

    st.header("What's your appetite for risk?")

    st.write(
        """
In StockMetrics, these risk labels are **relative to each other**.
They describe how concentrated each plan is, not whether investing is
ever risk-free.

A more concentrated plan may offer higher potential upside, but it may
also experience larger drawdowns and a bumpier ride.
"""
    )

    plan_name = st.selectbox(
        "Select plan",
        options=list(PLAN_WEIGHTS.keys()),
    )

    render_plan_boxes(plan_name)

    st.divider()

    st.header("Historical performance of your selected plan")

    st.write(
        "This section shows how the selected plan would have performed "
        "historically based on daily returns. It includes key metrics, a "
        "growth of £1 chart, and a table of the plan's asset weights."
    )

    returns = load_returns(version)
    weights = PLAN_WEIGHTS[plan_name]
    plan_ret = build_plan_returns(returns, weights)
    metrics = compute_plan_metrics(plan_ret)

    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    row1_col1.metric("Mean daily return", f"{metrics.mean_daily_return:.2%}")
    row1_col2.metric("Daily volatility", f"{metrics.daily_volatility:.2%}")
    row2_col1.metric(
        "Approx annual return",
        f"{metrics.annualised_return_approx:.2%}",
    )
    row2_col2.metric(
        "Annual volatility",
        f"{metrics.annualised_volatility_approx:.2%}",
    )

    st.metric("Max drawdown", f"{metrics.max_drawdown:.2%}")

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
    fig.update_layout(
        yaxis_title="Portfolio growth index",
        xaxis_title="Date",
    )
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
                "Asset": TICKER_DISPLAY_NAMES.get(ticker, ticker),
                "Ticker": ticker,
                "Weight (%)": round(weight * 100, 2),
            }
            for ticker, weight in weights.items()
        ]
    )

    st.dataframe(plan_table, use_container_width=True, hide_index=True)

    st.caption(
        "This is your selected plan. It is shown for educational comparison "
        "only and is not a personal investment recommendation."
    )

    st.info(
        "Educational use only. These plans illustrate risk trade-offs and "
        "are not personal investment recommendations."
    )
