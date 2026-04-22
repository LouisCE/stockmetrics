"""
Pytest checks for small deterministic helpers in `src/config.py`.
"""

from src.config import format_display_date, format_ticker_label


def test_format_ticker_label_known_ticker() -> None:
    assert format_ticker_label("AAPL") == "Apple (AAPL)"


def test_format_ticker_label_unknown_ticker() -> None:
    assert format_ticker_label("XYZ") == "XYZ"


def test_format_display_date() -> None:
    assert format_display_date("2024-01-15") == "15/01/2024"
