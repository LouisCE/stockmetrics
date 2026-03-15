"""
Predictor page.

Trend-following scenarios driven by each ticker's historical data.
Educational scenario ranges, not guarantees.

If a ML model exists, display its next-day prediction as a separate
informational metric, but it does NOT drive the long-horizon scenarios.
"""

from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st
import numpy as np

from src.config import DEFAULT_VERSION, get_paths
from src.data_processing import load_clean_prices_latest
from src.features import load_features_latest  # only used to support model pred if present
from src.forecast import (
    estimate_mu_sigma_from_history,
    get_last_price,
    scenario_ranges_from_history,
)
from src.modelling import FEATURE_COLS_NUM, FEATURE_COLS_CAT


def _predict_next_day_if_possible(model_path: Path, feat_df: pd.DataFrame, ticker: str) -> float | None:
    """
    Best-effort next-day prediction. Returns None if anything is missing.
    """
    try:
        if not model_path.exists():
            return None

        cols = FEATURE_COLS_NUM + FEATURE_COLS_CAT
        d = feat_df[feat_df["Ticker"] == ticker].sort_values("Date").dropna(subset=cols)
        if d.empty:
            return None

        X = d.iloc[[-1]][cols]
        model = joblib.load(model_path)
        return float(model.predict(X)[0])
    except Exception:
        return None


def _ml_interpretation_message(model_pred: float | None) -> tuple[str, str]:
    """
    Return a beginner-friendly interpretation message for the optional
    next-day ML prediction.

    Returns:
        (status, message)
        status: "info", "success", or "warning"
    """
    if model_pred is None:
        return (
            "info",
            "A machine learning next-day estimate is not available for this ticker. "
            "StockMetrics can still show long-term scenario ranges using historical "
            "trend and volatility.",
        )

    if model_pred > 0:
        return (
            "success",
            f"The model's next-day estimate is **{model_pred:.2%}**, which is slightly positive. "
            "This does **not** mean the price will definitely rise tomorrow. It simply means the "
            "model detected a small positive pattern in the recent historical features.",
        )

    if model_pred < 0:
        return (
            "warning",
            f"The model's next-day estimate is **{model_pred:.2%}**, which is slightly negative. "
            "This does **not** mean the price will definitely fall tomorrow. It simply means the "
            "model detected a small negative pattern in the recent historical features.",
        )

    return (
        "info",
        "The model's next-day estimate is close to **0.00%**. In plain English, that suggests "
        "the model is not seeing a strong short-term directional signal right now.",
    )


def render() -> None:
    st.title("🎯 Predictor")
    st.markdown(
        """
StockMetrics generates **long-horizon scenario ranges** by following each ticker’s
**historical trend and volatility**.

These are **educational scenarios**, not guarantees.
"""
    )

    version = st.selectbox("Data version", options=[DEFAULT_VERSION], index=0)

    paths = get_paths(version)
    clean_df = load_clean_prices_latest(paths.processed_dir, version)

    # Ticker selection
    tickers = sorted(clean_df["Ticker"].unique().tolist())
    ticker = st.selectbox("Select ticker", options=tickers)

    # Horizon (how far to forecast)
    horizon_years = st.selectbox("Horizon", options=[1, 2, 5, 10, 20, 50], index=2)
    horizon_days = int(horizon_years * 252)

    # Trend window (how much history to follow)
    window_years = st.selectbox("Trend window (how much history to follow)", options=[1, 2, 5, 10], index=2)
    window_days = int(window_years * 252)

    last_dt, last_price = get_last_price(clean_df, ticker)

    mu_log, sigma_log, effective_window = estimate_mu_sigma_from_history(
        clean_df=clean_df,
        ticker=ticker,
        window_days=window_days,
    )

    res = scenario_ranges_from_history(
        last_price=last_price,
        mu_log=mu_log,
        sigma_log=sigma_log,
        horizon_days=horizon_days,
        n_sims=2000,
        seed=42,
    )

    # Attach window info (kept in result for display)
    res = type(res)(
        horizon_days=res.horizon_days,
        optimistic=res.optimistic,
        realistic=res.realistic,
        pessimistic=res.pessimistic,
        mu_log_used=res.mu_log_used,
        sigma_log_used=res.sigma_log_used,
        window_days=effective_window,
    )

    # Optional model metric (not used for scenarios)
    model_path = paths.models_dir / f"stock_forecast_model_{version}.pkl"
    model_pred = None
    if model_path.exists():
        feat_df = load_features_latest(paths.processed_dir, version)
        model_pred = _predict_next_day_if_possible(model_path, feat_df, ticker)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Last price", f"{last_price:,.2f}")
    c2.metric("Last date", f"{last_dt.date()}")
    c3.metric("Trend window used", f"{res.window_days} days")

    # Convert mu_log to a simple daily drift for human reading:
    # approx: mu_simple ≈ exp(mu_log) - 1
    mu_simple = float(np.expm1(res.mu_log_used))
    sigma_simple = float(np.sqrt(np.expm1(res.sigma_log_used**2))) if res.sigma_log_used > 0 else 0.0
    c4.metric("Estimated daily drift", f"{mu_simple:.4%}")

    if model_pred is not None:
        st.caption(f"ML next-day prediction (not used in scenarios): {model_pred:.4%}")

    st.caption(f"Estimated daily volatility (approx): {sigma_simple:.4%}")

    st.divider()
    st.subheader(f"Scenario end prices (≈{horizon_years}y)")

    out = pd.DataFrame(
        {
            "Scenario": ["Pessimistic", "Realistic", "Optimistic"],
            "End price": [res.pessimistic, res.realistic, res.optimistic],
        }
    )
    st.dataframe(out, use_container_width=True)

    st.info(
        "These scenarios follow the ticker’s historical trend and volatility to "
        "illustrate uncertainty over time. Not financial advice."
    )
