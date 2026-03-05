"""
Forecast helpers for StockMetrics.

Trend-following, data-driven scenarios (educational, not financial advice).

Approach (simple and stable):
- Estimate drift and volatility from the ticker's own historical returns.
- Simulate future prices using log-return compounding (GBM-style).
- Report percentile end prices as scenario ranges.

Key point:
- The ML model predicts next-day returns (short-horizon signal).
- Long-horizon scenario ranges use historical trend and volatility because
  compounding noisy 1-day predictions over many years is unstable and can
  produce misleading outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ScenarioResult:
    horizon_days: int
    optimistic: float
    realistic: float
    pessimistic: float
    mu_log_used: float
    sigma_log_used: float
    window_days: int


def get_last_price(clean_df: pd.DataFrame, ticker: str) -> Tuple[pd.Timestamp, float]:
    """
    Return (last_date, last_adj_close) for the ticker from the cleaned dataset.
    """
    d = clean_df[clean_df["Ticker"] == ticker].sort_values("Date")
    if d.empty:
        raise ValueError(f"No prices found for {ticker}")
    row = d.iloc[-1]
    return pd.to_datetime(row["Date"]), float(row["Adj_Close"])


def estimate_mu_sigma_from_history(
    clean_df: pd.DataFrame,
    ticker: str,
    window_days: int = 1260,  # ~5 years of trading days
) -> Tuple[float, float, int]:
    """
    Estimate log-return drift (mu_log) and log-return volatility (sigma_log)
    from the ticker's historical returns.

    We use log returns:
      r_log = log(Adj_Close_t / Adj_Close_{t-1})

    Returns:
      (mu_log, sigma_log, effective_window_days)
    """
    d = clean_df[clean_df["Ticker"] == ticker].sort_values("Date").copy()
    if d.empty:
        raise ValueError(f"No prices found for {ticker}")

    px = pd.to_numeric(d["Adj_Close"], errors="coerce")
    px = px.replace([np.inf, -np.inf], np.nan).dropna()
    px = px[px > 0]
    log_ret = np.log(px).diff().dropna()

    if log_ret.empty:
        raise ValueError(f"Not enough data to compute returns for {ticker}")

    # Use last window_days if available
    if len(log_ret) >= window_days:
        log_ret = log_ret.iloc[-window_days:]
        effective = window_days
    else:
        effective = int(len(log_ret))

    mu_log = float(log_ret.mean())
    sigma_log = float(log_ret.std(ddof=0))  # population-ish; stable

    # Safety fallback if sigma is degenerate
    if not np.isfinite(sigma_log) or sigma_log <= 0:
        sigma_log = 1e-6

    if not np.isfinite(mu_log):
        mu_log = 0.0

    return mu_log, sigma_log, effective


def scenario_ranges_from_history(
    last_price: float,
    mu_log: float,
    sigma_log: float,
    horizon_days: int,
    n_sims: int = 2000,
    seed: int = 42,
) -> ScenarioResult:
    """
    Simulate end-price distribution over horizon_days using log returns.

    Price evolution:
      log(P_T) = log(P_0) + sum_t Normal(mu_log, sigma_log)

    Scenarios:
      pessimistic = 25th percentile
      realistic   = 50th percentile (median)
      optimistic  = 75th percentile
    """
    rng = np.random.default_rng(seed)

    horizon_days = int(horizon_days)
    n_sims = int(n_sims)

    mu_log = float(mu_log)
    sigma_log = float(max(sigma_log, 1e-8))

    # Simulate log returns and compound
    log_rets = rng.normal(loc=mu_log, scale=sigma_log, size=(n_sims, horizon_days))
    log_growth = log_rets.sum(axis=1)

    end_prices = float(last_price) * np.exp(log_growth)

    q25, q50, q75 = np.quantile(end_prices, [0.25, 0.50, 0.75])

    # window_days is filled by caller (kept in the result for display)
    return ScenarioResult(
        horizon_days=horizon_days,
        optimistic=float(q75),
        realistic=float(q50),
        pessimistic=float(q25),
        mu_log_used=mu_log,
        sigma_log_used=sigma_log,
        window_days=0,
    )
