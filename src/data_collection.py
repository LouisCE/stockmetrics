"""
Data collection helpers for Yahoo Finance via yfinance.

Notebooks can call these helpers, and later the Streamlit app can too.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd
import yfinance as yf


def download_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Download historical OHLCV data for a single ticker.

    Returns a tidy DataFrame with:
    - Date column
    - OHLCV columns
    - Ticker column
    """
    df = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=False,
        progress=False,
    )

    if df is None or df.empty:
        raise ValueError(f"No data returned for ticker: {ticker}")

    df = df.reset_index()
    df["Ticker"] = ticker
    return df


def make_timestamp() -> str:
    """UTC timestamp for snapshot file names."""
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def save_snapshot(df: pd.DataFrame, out_dir: Path, ticker: str, version: str) -> Path:
    """Save a single ticker snapshot as CSV and return the saved path."""
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = make_timestamp()
    file_path = out_dir / f"{ticker}_raw_{version}_{stamp}.csv"
    df.to_csv(file_path, index=False)
    return file_path


def download_many(
    tickers: Iterable[str],
    start: str,
    end: str,
    out_dir: Path,
    version: str,
) -> tuple[list[pd.DataFrame], list[str], list[Path]]:
    """
    Download many tickers, saving a CSV per ticker.

    Returns:
    - list of successful DataFrames
    - list of failed tickers (with error messages)
    - list of saved CSV Paths (same order as successful DataFrames)
    """
    all_data: list[pd.DataFrame] = []
    failed: list[str] = []
    saved_paths: list[Path] = []

    for ticker in tickers:
        try:
            df = download_stock_data(ticker, start, end)
            saved_path = save_snapshot(df, out_dir, ticker, version)
            all_data.append(df)
            saved_paths.append(saved_path)
        except Exception as e:
            failed.append(f"{ticker}: {e}")

    return all_data, failed, saved_paths
