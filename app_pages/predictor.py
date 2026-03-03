"""
Predictor page.

Uses trained model and scenario simulation.
Educational scenario ranges, not guarantees.
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.config import DEFAULT_VERSION, get_paths
from src.data_processing import load_clean_prices_latest
from src.features import load_features_latest
from src.forecast import (
    estimate_sigma_from_returns,
    get_last_price,
    predict_next_day_return,
    scenario_ranges_from_prediction,
)


def render() -> None:
    st.title("🎯 Predictor")
    st.markdown(
        """
StockMetrics predicts **next-day returns** and uses them to generate
**scenario ranges** over longer horizons.

These are **educational scenarios**, not guarantees.
"""
    )

    version = st.selectbox("Data version", options=[DEFAULT_VERSION], index=0)

    paths = get_paths(version)
    clean_df = load_clean_prices_latest(paths.processed_dir, version)
    feat_df = load_features_latest(paths.processed_dir, version)

    tickers = sorted(clean_df["Ticker"].unique().tolist())
    ticker = st.selectbox("Select ticker", options=tickers)

    horizon_years = st.selectbox("Horizon", options=[1, 2, 5, 10, 20, 50], index=2)
    horizon_days = int(horizon_years * 252)

    model_path = paths.models_dir / f"stock_forecast_model_{version}.pkl"
    if not model_path.exists():
        st.error("Model file not found. Run notebook 05 first.")
        st.stop()

    last_dt, last_price = get_last_price(clean_df, ticker)
    mu = predict_next_day_return(model_path, feat_df, ticker)
    sigma = estimate_sigma_from_returns(clean_df, ticker, window=90)

    res = scenario_ranges_from_prediction(
        last_price=last_price,
        mu_daily=mu,
        sigma_daily=sigma,
        horizon_days=horizon_days,
        n_sims=2000,
        seed=42,
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Last price", f"{last_price:,.2f}")
    c2.metric("Last date", f"{last_dt.date()}")
    c3.metric("Pred next-day return", f"{mu:.4%}")

    st.divider()
    st.subheader(f"Scenario prices (≈{horizon_years}y)")

    out = pd.DataFrame(
        {
            "Scenario": ["Pessimistic", "Realistic", "Optimistic"],
            "End price": [res.pessimistic, res.realistic, res.optimistic],
        }
    )
    st.dataframe(out, use_container_width=True)

    st.info(
        "Scenarios use a simple simulation (median/quantiles) "
        "to illustrate uncertainty. Not financial advice."
    )
