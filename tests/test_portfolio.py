"""
Pytest checks for portfolio calculation helpers in `src/portfolio.py`.
"""

import pandas as pd

from src.portfolio import (
    build_plan_returns,
    daily_returns_from_prices,
    max_drawdown_from_returns,
    price_wide,
)


def test_price_wide_creates_wide_dataframe() -> None:
    df = pd.DataFrame(
        {
            "Date": pd.to_datetime(
                ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02"]
            ),
            "Ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
            "Adj_Close": [100, 200, 110, 220],
        }
    )

    result = price_wide(df)

    assert list(result.columns) == ["AAPL", "MSFT"]
    assert len(result) == 2


def test_daily_returns_from_prices() -> None:
    prices = pd.DataFrame(
        {
            "AAPL": [100, 110],
            "MSFT": [200, 220],
        },
        index=pd.to_datetime(["2024-01-01", "2024-01-02"]),
    )

    result = daily_returns_from_prices(prices)

    assert len(result) == 1
    assert round(result.iloc[0]["AAPL"], 4) == 0.1


def test_build_plan_returns() -> None:
    returns = pd.DataFrame(
        {
            "AAPL": [0.01, 0.02],
            "MSFT": [0.03, 0.04],
        }
    )

    weights = {"AAPL": 0.5, "MSFT": 0.5}
    result = build_plan_returns(returns, weights)

    assert len(result) == 2
    assert round(result.iloc[0], 4) == 0.02


def test_max_drawdown_from_returns() -> None:
    returns = pd.Series([0.10, -0.20, 0.05])
    result = max_drawdown_from_returns(returns)

    assert result < 0


def test_build_plan_returns_renormalises_missing_tickers() -> None:
    returns = pd.DataFrame(
        {
            "AAPL": [0.01, 0.02],
        }
    )

    weights = {"AAPL": 0.5, "MSFT": 0.5}
    result = build_plan_returns(returns, weights)

    assert len(result) == 2
    assert round(result.iloc[0], 4) == 0.01
