"""
Data processing helpers (loading latest raw snapshots, cleaning, saving).

Used by notebooks and later by the Streamlit app.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, Tuple

import pandas as pd

REQUIRED_COLUMNS = [
    "Date",
    "Open",
    "High",
    "Low",
    "Close",
    "Adj_Close",
    "Volume",
    "Ticker",
]


def latest_snapshot_for_ticker(raw_dir: Path, ticker: str, version: str) -> Path:
    """
    Return the newest snapshot CSV for a ticker/version.

    Snapshots are named like: {TICKER}_raw_{version}_YYYYMMDD_HHMMSS.csv
    """
    pattern = f"{ticker}_raw_{version}_*.csv"
    matches = sorted(raw_dir.glob(pattern))
    if not matches:
        raise FileNotFoundError(
            f"No raw snapshots found for {ticker} in {raw_dir} (pattern: {pattern})"
        )
    return matches[-1]


def build_latest_snapshot_map(
    raw_dir: Path,
    tickers: Iterable[str],
    version: str,
) -> Dict[str, Path]:
    """Map each ticker to its latest snapshot path."""
    return {t: latest_snapshot_for_ticker(raw_dir, t, version) for t in tickers}


def clean_prices(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and standardise a single-ticker raw price DataFrame.

    Outputs exactly REQUIRED_COLUMNS, with consistent naming and types.
    """
    df = df.copy()

    # Standardise column names (yfinance outputs can vary)
    df.columns = [str(c).strip().replace(" ", "_") for c in df.columns]

    # Required columns checks
    if "Ticker" not in df.columns:
        raise KeyError("Expected 'Ticker' column is missing.")
    if "Date" not in df.columns:
        raise KeyError("Expected 'Date' column is missing.")

    # Ensure Adj_Close exists (fallback to Close if needed)
    if "Adj_Close" not in df.columns and "Close" in df.columns:
        df["Adj_Close"] = df["Close"]

    # Parse dates
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    # Coerce numerics
    for col in ["Open", "High", "Low", "Close", "Adj_Close", "Volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop duplicates + sort
    df = df.drop_duplicates(subset=["Ticker", "Date"])
    df = df.sort_values(["Ticker", "Date"])

    # Ensure schema consistency
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            df[col] = pd.NA

    return df[REQUIRED_COLUMNS]


def load_and_clean_latest_raw(
    raw_dir: Path,
    tickers: Iterable[str],
    version: str,
) -> Tuple[pd.DataFrame, Dict[str, Path]]:
    """
    Load the latest raw snapshot per ticker, clean, and concatenate.

    Returns:
      - clean_df (all tickers combined)
      - file_map (ticker -> snapshot path used)
    """
    file_map = build_latest_snapshot_map(raw_dir, tickers, version)

    frames = []
    for ticker, path in file_map.items():
        temp = pd.read_csv(path)
        temp = clean_prices(temp)
        frames.append(temp)

    clean_df = pd.concat(frames, ignore_index=True)
    return clean_df, file_map


def save_clean_prices(
    clean_df: pd.DataFrame,
    processed_dir: Path,
    version: str,
) -> Tuple[Path, Path]:
    """
    Save clean prices as:
      - archived timestamped copy (audit trail)
      - stable latest copy (for app)
    """
    processed_dir.mkdir(parents=True, exist_ok=True)
    timestamp = pd.Timestamp.utcnow().strftime("%Y%m%d_%H%M%S")

    archived_path = processed_dir / f"clean_prices_{version}_{timestamp}.csv"
    latest_path = processed_dir / f"clean_prices_{version}_latest.csv"

    clean_df.to_csv(archived_path, index=False)
    clean_df.to_csv(latest_path, index=False)

    return archived_path, latest_path


def load_clean_prices_latest(processed_dir: Path, version: str) -> pd.DataFrame:
    """Load the stable latest cleaned dataset."""
    path = processed_dir / f"clean_prices_{version}_latest.csv"
    return pd.read_csv(path, parse_dates=["Date"])
