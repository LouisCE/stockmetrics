"""
Feature engineering functions.

Used by notebooks and later by the Streamlit app.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd


FEATURE_COLUMNS = [
    "log_return_1d",
    "return_1d",
    "vol_30d",
    "vol_90d",
    "mom_30d",
    "mom_90d",
    "drawdown",
    "lag_return_1",
    "lag_return_5",
    "lag_return_21",
]


def add_features_per_ticker(g: pd.DataFrame) -> pd.DataFrame:
    """Add time-series features for one ticker (expects Date-sorted tidy data)."""
    g = g.sort_values("Date").copy()

    s = pd.to_numeric(g["Adj_Close"], errors="coerce")

    # Returns
    g["return_1d"] = s.pct_change()

    # Log returns (stable baseline)
    g["log_return_1d"] = (s / s.shift(1)).apply(lambda v: pd.NA if pd.isna(v) else v)
    g["log_return_1d"] = pd.to_numeric(g["log_return_1d"], errors="coerce")

    # Volatility
    g["vol_30d"] = g["return_1d"].rolling(30).std()
    g["vol_90d"] = g["return_1d"].rolling(90).std()

    # Momentum
    g["mom_30d"] = g["return_1d"].rolling(30).mean()
    g["mom_90d"] = g["return_1d"].rolling(90).mean()

    # Drawdown
    running_max = s.cummax()
    g["drawdown"] = s / running_max - 1.0

    # Lags
    g["lag_return_1"] = g["return_1d"].shift(1)
    g["lag_return_5"] = g["return_1d"].shift(5)
    g["lag_return_21"] = g["return_1d"].shift(21)

    return g


def build_features(clean_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build a model-ready feature table from the cleaned prices table.

    Returns a tidy DataFrame (same rows as clean_df minus initial rolling windows).
    """
    feat_df = clean_df.groupby("Ticker", group_keys=False).apply(add_features_per_ticker)

    # Drop early rows where rolling windows aren't available yet
    feat_df = feat_df.dropna(
        subset=["return_1d", "vol_30d", "mom_30d", "drawdown", "lag_return_21"]
    )

    return feat_df


def save_features(
    feat_df: pd.DataFrame,
    processed_dir: Path,
    version: str,
) -> Tuple[Path, Path]:
    """Save features as archived timestamped + stable latest copy."""
    processed_dir.mkdir(parents=True, exist_ok=True)
    timestamp = pd.Timestamp.utcnow().strftime("%Y%m%d_%H%M%S")

    archived_path = processed_dir / f"features_{version}_{timestamp}.csv"
    latest_path = processed_dir / f"features_{version}_latest.csv"

    feat_df.to_csv(archived_path, index=False)
    feat_df.to_csv(latest_path, index=False)

    return archived_path, latest_path


def load_features_latest(processed_dir: Path, version: str) -> pd.DataFrame:
    """Load the stable latest features dataset."""
    path = processed_dir / f"features_{version}_latest.csv"
    return pd.read_csv(path, parse_dates=["Date"])
