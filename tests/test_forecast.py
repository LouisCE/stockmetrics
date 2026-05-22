"""
Pytest checks for forecast helper behaviour in `src/forecast.py`.
"""

import pandas as pd
import pytest

from src.forecast import (
    estimate_mu_sigma_from_history,
    get_last_price,
    scenario_ranges_from_history,
)


def test_get_last_price() -> None:
    df = pd.DataFrame(
        {
            "Date": pd.to_datetime(["2024-01-01", "2024-01-02"]),
            "Ticker": ["AAPL", "AAPL"],
            "Adj_Close": [100.0, 110.0],
        }
    )

    last_dt, last_price = get_last_price(df, "AAPL")

    assert str(last_dt.date()) == "2024-01-02"
    assert last_price == 110.0


def test_estimate_mu_sigma_from_history() -> None:
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2024-01-01", periods=10, freq="D"),
            "Ticker": ["AAPL"] * 10,
            "Adj_Close": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        }
    )

    mu_log, sigma_log, effective = estimate_mu_sigma_from_history(
        clean_df=df,
        ticker="AAPL",
        window_days=5,
    )

    assert isinstance(mu_log, float)
    assert isinstance(sigma_log, float)
    assert effective == 5


def test_scenario_ranges_from_history_ordering() -> None:
    result = scenario_ranges_from_history(
        last_price=100.0,
        mu_log=0.0001,
        sigma_log=0.01,
        horizon_days=252,
        n_sims=500,
        seed=42,
    )

    assert result.pessimistic <= result.realistic <= result.optimistic


def test_get_last_price_raises_for_missing_ticker() -> None:
    df = pd.DataFrame(
        {
            "Date": pd.to_datetime(["2024-01-01"]),
            "Ticker": ["AAPL"],
            "Adj_Close": [100.0],
        }
    )

    with pytest.raises(ValueError):
        get_last_price(df, "MSFT")


def test_estimate_mu_sigma_raises_for_missing_ticker() -> None:
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2024-01-01", periods=5, freq="D"),
            "Ticker": ["AAPL"] * 5,
            "Adj_Close": [100, 101, 102, 103, 104],
        }
    )

    with pytest.raises(ValueError):
        estimate_mu_sigma_from_history(df, "MSFT")
