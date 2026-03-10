"""
Project-wide configuration (paths, tickers, date ranges).

If something is used in notebooks + the app,
it belongs here rather than being duplicated in multiple places.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from datetime import datetime, timezone


@dataclass(frozen=True)
class Paths:
    """Common project paths."""
    root: Path
    data_dir: Path
    raw_dir: Path
    processed_dir: Path
    outputs_dir: Path
    models_dir: Path


def get_project_root() -> Path:
    """
    Resolve the project root from the src/ directory location.

    This file lives in stockmetrics/src/, so project root is one level up.
    """
    return Path(__file__).resolve().parents[1]


def get_paths(version: str = "v2") -> Paths:
    """Build versioned folder paths."""
    root = get_project_root()
    data_dir = root / "data"
    raw_dir = data_dir / "raw" / version
    processed_dir = data_dir / "processed" / version
    outputs_dir = root / "outputs" / version
    models_dir = root / "models"

    return Paths(
        root=root,
        data_dir=data_dir,
        raw_dir=raw_dir,
        processed_dir=processed_dir,
        outputs_dir=outputs_dir,
        models_dir=models_dir,
    )


def utc_today_str() -> str:
    """Today's date (UTC) as YYYY-MM-DD."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# Versioning

# v1 = original dataset/artefacts
# v2 = longer-history ETF run using VWRL/VUSA from 2012-05-22
DEFAULT_VERSION = "v2"


# Date window (single unified window across ALL tickers)

# VWRL and VUSA launched on 2012-05-22, so this is the earliest clean
# start date that keeps equal coverage across ETFs + Mag 7.
DEFAULT_START_DATE = "2012-05-22"
DEFAULT_END_DATE = utc_today_str()


# Tickers

# "Magnificent Seven" (Yahoo Finance US tickers)
MAG7_TICKERS = ["AAPL", "AMZN", "GOOGL", "META", "MSFT", "NVDA", "TSLA"]

# UK ETFs (LSE uses ".L")
# Vanguard FTSE All-World and S&P 500
# Distributing share classes (longer history)
SP500_DIST_TICKER = "VUSA.L"       # Distributing (launched 2012)
ALL_WORLD_DIST_TICKER = "VWRL.L"   # Distributing (launched 2012)

# Accumulating share classes (shorter history, kept as alternates)
SP500_ACC_TICKER = "VUAG.L"        # Accumulating (launched 2019)
ALL_WORLD_ACC_TICKER = "VWRP.L"    # Accumulating (launched 2019)

# Default ETF choices for this project run (v2)
SP500_TICKER = SP500_DIST_TICKER
ALL_WORLD_TICKER = ALL_WORLD_DIST_TICKER

# US proxies (only for emergency fallback / comparisons)
SP500_US_PROXY = "SPY"
ALL_WORLD_US_PROXY = "VT"

# Main collection list for notebooks + dashboard
CORE_TICKERS = [ALL_WORLD_TICKER, SP500_TICKER] + MAG7_TICKERS
DEFAULT_TICKERS = CORE_TICKERS
