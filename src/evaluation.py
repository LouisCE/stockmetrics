"""
Evaluation helpers: metrics + plots.

Used by 06_model_evaluation.ipynb and dashboard pages.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true, y_pred) -> Dict[str, float]:
    return {
        "r2": float(r2_score(y_true, y_pred)),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(mean_squared_error(y_true, y_pred, squared=False)),
    }


def save_actual_vs_pred_plot(
    y_true,
    y_pred,
    out_dir: Path,
    filename: str = "actual_vs_pred.png",
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename

    plt.figure()
    plt.scatter(y_true, y_pred, alpha=0.4)
    plt.title("Actual vs Predicted")
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()

    return path
