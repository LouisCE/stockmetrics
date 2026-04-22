"""
Pytest checks for expected engineered feature outputs in `src/features.py`.
"""

import numpy as np
import pandas as pd

from src.features import build_features


def test_build_features_creates_expected_columns() -> None:
    dates = pd.date_range("2023-01-01", periods=150, freq="D")
    prices = np.linspace(100, 150, 150)

    df = pd.DataFrame(
        {
            "Date": dates,
            "Open": prices,
            "High": prices + 1,
            "Low": prices - 1,
            "Close": prices,
            "Adj_Close": prices,
            "Volume": 1000,
            "Ticker": "AAPL",
        }
    )

    result = build_features(df)

    expected_columns = {
        "target_next_day_return",
        "return_1d",
        "log_return_1d",
        "vol_30d",
        "vol_90d",
        "mom_30d",
        "mom_90d",
        "zscore_30d",
        "mean_reversion_5d",
        "drawdown",
        "lag_return_1",
        "lag_return_5",
        "lag_return_21",
    }

    assert expected_columns.issubset(result.columns)
    assert not result.empty
    assert result["Ticker"].eq("AAPL").all()
