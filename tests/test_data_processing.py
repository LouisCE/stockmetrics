"""
Pytest checks for schema cleaning and data consistency
in `src/data_processing.py`.
"""

import pandas as pd
import pytest

from src.data_processing import REQUIRED_COLUMNS, clean_prices


def test_clean_prices_keeps_required_columns() -> None:
    df = pd.DataFrame(
        {
            "Date": ["2024-01-01", "2024-01-02"],
            "Open": [100, 101],
            "High": [102, 103],
            "Low": [99, 100],
            "Close": [101, 102],
            "Adj Close": [101, 102],
            "Volume": [1000, 1200],
            "Ticker": ["AAPL", "AAPL"],
        }
    )

    result = clean_prices(df)

    assert list(result.columns) == REQUIRED_COLUMNS
    assert len(result) == 2


def test_clean_prices_falls_back_to_close_for_adj_close() -> None:
    df = pd.DataFrame(
        {
            "Date": ["2024-01-01"],
            "Open": [100],
            "High": [102],
            "Low": [99],
            "Close": [101],
            "Volume": [1000],
            "Ticker": ["AAPL"],
        }
    )

    result = clean_prices(df)

    assert "Adj_Close" in result.columns
    assert result.loc[0, "Adj_Close"] == 101


def test_clean_prices_drops_duplicate_rows() -> None:
    df = pd.DataFrame(
        {
            "Date": ["2024-01-01", "2024-01-01"],
            "Open": [100, 100],
            "High": [102, 102],
            "Low": [99, 99],
            "Close": [101, 101],
            "Adj Close": [101, 101],
            "Volume": [1000, 1000],
            "Ticker": ["AAPL", "AAPL"],
        }
    )

    result = clean_prices(df)

    assert len(result) == 1


def test_clean_prices_raises_without_ticker_column() -> None:
    df = pd.DataFrame(
        {
            "Date": ["2024-01-01"],
            "Close": [101],
        }
    )

    with pytest.raises(KeyError):
        clean_prices(df)
