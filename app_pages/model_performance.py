"""
Model Performance page.

Loads evaluation artefacts from outputs/<version> and displays:
- success flag
- key metrics
- plots saved by 06_model_evaluation.ipynb
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from src.config import DEFAULT_VERSION


def read_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def render() -> None:
    st.title("🧪 Model Performance")

    version = st.selectbox("Artefact version", options=[DEFAULT_VERSION], index=0)

    base = Path("outputs") / version
    reports = base / "reports"
    figures = base / "figures"

    eval_path = reports / f"model_evaluation_report_{version}.json"
    train_path = reports / f"model_training_report_{version}.json"

    if not eval_path.exists() or not train_path.exists():
        st.error(
            "Evaluation artefacts not found. "
            "Run 05_model_training.ipynb and 06_model_evaluation.ipynb first."
        )
        st.stop()

    eval_report = read_json(eval_path)
    train_report = read_json(train_path)

    metrics_test = eval_report.get("metrics_test", {})
    metrics_train = eval_report.get("metrics_train", {})
    success = bool(eval_report.get("model_successful_against_business_case", False))
    rule = eval_report.get(
        "success_rule",
        "Test R² > 0 indicates a generalisable signal",
    )

    st.subheader("Business case result")
    if success:
        st.success(f"Model successful vs business case ✅ ({rule})")
    else:
        st.warning(f"Model not successful vs business case ⚠️ ({rule})")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Test R²", f"{metrics_test.get('r2', float('nan')):.6f}")
    c2.metric("Test MAE", f"{metrics_test.get('mae', float('nan')):.6f}")
    c3.metric("Test RMSE", f"{metrics_test.get('rmse', float('nan')):.6f}")
    c4.metric("Train R²", f"{metrics_train.get('r2', float('nan')):.6f}")

    st.divider()

    st.subheader(f"Best hyperparameters ({version})")
    st.json(train_report.get("best_params", {}))

    st.divider()

    st.subheader("Evaluation plots")
    plot_files = [
        figures / f"eval_actual_vs_pred_train_{version}.png",
        figures / f"eval_actual_vs_pred_test_{version}.png",
        figures / f"eval_residuals_hist_test_{version}.png",
        figures / f"eval_residuals_timeseries_test_{version}.png",
        figures / f"eval_pred_timeseries_test_{version}.png",
    ]
    for p in plot_files:
        if p.exists():
            st.image(str(p), caption=p.name, use_container_width=True)
        else:
            st.warning(f"Missing: {p.name}")

    st.divider()

    st.subheader("Feature importance (top rows)")
    fi_path = reports / f"feature_importance_{version}.csv"
    if fi_path.exists():
        fi = pd.read_csv(fi_path)
        st.dataframe(fi.head(20), use_container_width=True)
    else:
        st.warning("Feature importance file not found.")

    st.info(
        "StockMetrics uses scenario ranges to communicate uncertainty. "
        "This model is an educational component, not financial advice."
    )
