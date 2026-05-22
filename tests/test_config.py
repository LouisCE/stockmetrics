"""
Pytest checks for small deterministic helpers in `src/config.py`.
"""

from src.config import (
    format_display_date,
    format_ticker_label,
    get_currency_symbol,
)


def test_format_ticker_label_known_ticker() -> None:
    assert format_ticker_label("AAPL") == "Apple (AAPL)"


def test_format_ticker_label_unknown_ticker() -> None:
    assert format_ticker_label("XYZ") == "XYZ"


def test_format_display_date() -> None:
    assert format_display_date("2024-01-15") == "15/01/2024"


def test_get_currency_symbol_us_stock() -> None:
    assert get_currency_symbol("AAPL") == "$"


def test_get_currency_symbol_uk_etf() -> None:
    assert get_currency_symbol("VUSA.L") == "£"
