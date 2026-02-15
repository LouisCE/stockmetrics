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


def get_paths(version: str = "v1") -> Paths:
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


# Defaults used during early development (safe and small)
DEFAULT_VERSION = "v1"
DEFAULT_START_DATE = "2010-01-01"
DEFAULT_END_DATE = utc_today_str()

# Starting small while developing; expanding later (Mag 7 + benchmarks)
DEFAULT_TICKERS = ["SPY", "TSLA"]
