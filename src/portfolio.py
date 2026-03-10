"""
Portfolio plan calculations for StockMetrics.

Defines plan weights and helper functions to:
- build plan daily returns from ticker returns
- compute summary metrics (mean return, volatility, max drawdown)

Used by the Streamlit dashboard pages.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np
import pandas as pd

from src.config import ALL_WORLD_TICKER, SP500_TICKER


PLAN_WEIGHTS: Dict[str, Dict[str, float]] = {
    # Vanguard All-World ETF for a simple, diversified baseline
    # with a broad, global index
    "Diversified (Low Risk)": {ALL_WORLD_TICKER: 1.0},

    # Vanguard S&P 500 ETF for a more targeted US-focused plan
    "Targeted (Moderate Risk)": {SP500_TICKER: 1.0},

    # Concentrated on high-growth US tech for higher risk/reward potential
    "Concentrated (High Risk)": {
        SP500_TICKER: 0.75,
        "AAPL": 0.25 / 7,
        "AMZN": 0.25 / 7,
        "GOOGL": 0.25 / 7,
        "META": 0.25 / 7,
        "MSFT": 0.25 / 7,
        "NVDA": 0.25 / 7,
        "TSLA": 0.25 / 7,
    },

    # More aggressive with a Tesla overweight to show volatility impact
    "Aggressive (Higher Risk)": {
        SP500_TICKER: 0.50,
        "AAPL": 0.25 / 6,
        "AMZN": 0.25 / 6,
        "GOOGL": 0.25 / 6,
        "META": 0.25 / 6,
        "MSFT": 0.25 / 6,
        "NVDA": 0.25 / 6,
        # Tesla is volatile but has high growth potential
        "TSLA": 0.25,
    },
}


def price_wide(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert tidy clean prices df into wide Adj_Close prices:
    index=Date, columns=Ticker.
    """
    wide = df.pivot(index="Date", columns="Ticker", values="Adj_Close").sort_index()
    return wide


def daily_returns_from_prices(prices: pd.DataFrame) -> pd.DataFrame:
    """Compute daily percent returns from wide prices."""
    return prices.pct_change().dropna(how="all")


def build_plan_returns(returns: pd.DataFrame, weights: Dict[str, float]) -> pd.Series:
    """
    Weighted plan return series from wide returns.

    Missing tickers are ignored (weight renormalised).
    """
    cols = [t for t in weights.keys() if t in returns.columns]
    if not cols:
        raise ValueError("No plan tickers found in returns data.")

    w = np.array([weights[t] for t in cols], dtype=float)
    w = w / w.sum()

    plan_ret = (returns[cols] * w).sum(axis=1)
    plan_ret.name = "plan_return"
    return plan_ret


def max_drawdown_from_returns(r: pd.Series) -> float:
    """
    Max drawdown from returns series using cumulative equity curve.
    Returns a negative number (e.g. -0.55 == -55%).
    """
    equity = (1 + r.fillna(0)).cumprod()
    peak = equity.cummax()
    dd = equity / peak - 1.0
    return float(dd.min())


@dataclass(frozen=True)
class PlanMetrics:
    mean_daily_return: float
    daily_volatility: float
    annualised_return_approx: float
    annualised_volatility_approx: float
    max_drawdown: float


def compute_plan_metrics(r: pd.Series) -> PlanMetrics:
    """Compute key metrics used in StockMetrics dashboard."""
    mean = float(r.mean())
    vol = float(r.std())
    return PlanMetrics(
        mean_daily_return=mean,
        daily_volatility=vol,
        annualised_return_approx=mean * 252,
        annualised_volatility_approx=vol * np.sqrt(252),
        max_drawdown=max_drawdown_from_returns(r),
    )
