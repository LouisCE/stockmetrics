"""
Forecast helpers for StockMetrics.

Educational scenario ranges (not trading signals).
Uses the trained model's next-day return prediction as a baseline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import joblib
from pathlib import Path

from src.modelling import FEATURE_COLS_NUM, FEATURE_COLS_CAT


@dataclass(frozen=True)
class ScenarioResult:
    horizon_days: int
    optimistic: float
    realistic: float
    pessimistic: float


def _latest_feature_row(feat_df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    d = feat_df[feat_df["Ticker"] == ticker].sort_values("Date")
    if d.empty:
        raise ValueError(f"No feature rows found for {ticker}")
    return d.iloc[[-1]][FEATURE_COLS_NUM + FEATURE_COLS_CAT]


def predict_next_day_return(
    model_path: Path,
    feat_df: pd.DataFrame,
    ticker: str,
) -> float:
    model = joblib.load(model_path)
    X = _latest_feature_row(feat_df, ticker)
    pred = float(model.predict(X)[0])
    return pred


def scenario_ranges_from_prediction(
    last_price: float,
    mu_daily: float,
    sigma_daily: float,
    horizon_days: int,
    n_sims: int = 2000,
    seed: int = 42,
) -> ScenarioResult:
    """
    Simulate horizon price outcomes using a simple normal model.

    optimistic = 75th percentile
    realistic  = 50th percentile (median)
    pessimistic= 25th percentile
    """
    rng = np.random.default_rng(seed)
    # Simulate daily returns
    rets = rng.normal(loc=mu_daily, scale=max(sigma_daily, 1e-8), size=(n_sims, horizon_days))
    # Convert to price paths
    growth = (1.0 + rets).clip(min=0.01)  # avoid negative/zero explosions
    end_prices = last_price * growth.prod(axis=1)

    q25, q50, q75 = np.quantile(end_prices, [0.25, 0.50, 0.75])
    return ScenarioResult(
        horizon_days=horizon_days,
        optimistic=float(q75),
        realistic=float(q50),
        pessimistic=float(q25),
    )


def get_last_price(clean_df: pd.DataFrame, ticker: str) -> Tuple[pd.Timestamp, float]:
    d = clean_df[clean_df["Ticker"] == ticker].sort_values("Date")
    if d.empty:
        raise ValueError(f"No prices found for {ticker}")
    row = d.iloc[-1]
    return pd.to_datetime(row["Date"]), float(row["Adj_Close"])


def estimate_sigma_from_returns(clean_df: pd.DataFrame, ticker: str, window: int = 90) -> float:
    d = clean_df[clean_df["Ticker"] == ticker].sort_values("Date").copy()
    d["ret"] = pd.to_numeric(d["Adj_Close"], errors="coerce").pct_change()
    sigma = float(d["ret"].rolling(window).std().iloc[-1])
    if np.isnan(sigma) or sigma <= 0:
        sigma = float(d["ret"].std())
    return float(sigma if not np.isnan(sigma) else 0.02)
