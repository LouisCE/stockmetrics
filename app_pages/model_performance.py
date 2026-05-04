"""
Model Performance page.

Loads evaluation artefacts from outputs/<version> and explains:
- whether the model met the ML business case
- what the metrics mean in beginner-friendly language
- why weak short-term prediction supports the project message
- which evaluation plots and feature importance artefacts were produced
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from src.config import DEFAULT_VERSION


def read_json(path: Path) -> dict:
    """Read a JSON report file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def render() -> None:
    """Render the Model Performance page."""
    st.title("🧪 Model Performance")

    st.divider()

    st.header("Machine learning model evaluation and what it means")
    st.write(
        "Review whether the machine learning model met its business case, "
        "what the results mean, and why the signal should be interpreted "
        "carefully."
    )

    st.image(
        "documentation/dashboard/model_performance_hero.png",
        caption=(
            "StockMetrics uses supervised learning and regression techniques "
            "to do market forecasting with a next-day return prediction model."
        ),
        use_container_width=True,
    )

    st.divider()

    st.header("Next-day return prediction performance")

    st.write(
        """
This page explains how the StockMetrics machine learning model performed.

The model tries to estimate **next-day return**, which is a deliberately
difficult short-term prediction task. This helps demonstrate why beginner
investors should be cautious about short-term trading signals.

StockMetrics uses this model as an **educational snapshot**, not as a
buy/sell recommendation.
"""
    )

    st.success(
        "In simple terms: the model found a very small short-term signal, "
        "but daily market prediction remains difficult. This supports the "
        "project's focus on long-term scenario thinking.",
        icon="💡"
    )

    st.info(
        "The long-term scenario ranges on the Predictor page are generated "
        "separately using historical trend and volatility. They are **not** "
        "created by compounding the next-day machine learning prediction.",
        icon="ℹ️"
    )

    version = DEFAULT_VERSION
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
    success = bool(
        eval_report.get(
            "model_successful_against_business_case",
            False,
        )
    )
    rule = eval_report.get(
        "success_rule",
        "Test R² > 0 indicates a generalisable signal",
    )

    st.divider()

    st.header("Business case result")

    st.write(
        """
The business case did **not** require a perfect market predictor. It required
evidence that the model could detect at least some generalisable signal on
unseen chronological test data.

The model was evaluated using chronological train/test splitting and
time-aware cross-validation, helping avoid unrealistic random shuffling of
time-series data.
"""
    )

    if success:
        st.success(
            "The model met the project business case\n\n"
            f"Success rule: **{rule}**",
            icon="✅"
        )
    else:
        st.warning(
            "The model did not meet the project business case\n\n"
            f"Success rule: **{rule}**",
            icon="⚠️"
        )

    st.divider()

    st.header("Model performance metrics")

    st.write(
        "The model's performance was evaluated using several metrics. These "
        "metrics help us understand how well the model is predicting next-day "
        "returns and whether it shows any generalisable signal."
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Test R²", f"{metrics_test.get('r2', float('nan')):.6f}")
    c2.metric("Test MAE", f"{metrics_test.get('mae', float('nan')):.6f}")
    c3.metric("Test RMSE", f"{metrics_test.get('rmse', float('nan')):.6f}")
    c4.metric("Train R²", f"{metrics_train.get('r2', float('nan')):.6f}")

    st.divider()

    st.header("What these results mean")

    st.write(
        "**R²** shows whether the model performed better than a simple "
        "baseline. A value above 0 suggests some useful signal. A value close "
        "to 0 means the signal is weak."
    )

    st.write(
        "**MAE** and **RMSE** show average prediction error. Lower values are "
        "better, but they should be interpreted carefully because daily "
        "returns are naturally noisy."
    )

    st.write(
        "For StockMetrics, the key lesson is that even when a model meets the "
        "minimum success rule, short-term predictions can still be weak. This "
        "supports the app's beginner-friendly message: long-term investing "
        "is usually more sensible than relying on day-to-day predictions."
    )

    if success:
        st.success(
            "The model showed a **small positive signal** on unseen data. "
            "That means it performed slightly better than a simple baseline "
            "according to the project success rule.",
            icon="✅"
        )
    else:
        st.warning(
            "The model did not show enough generalisable signal to beat the "
            "project success rule. This would still be useful evidence that "
            "short-term market prediction is difficult.",
            icon="⚠️"
        )

    st.divider()

    st.header("Why R² > 0 is a meaningful success rule")

    st.write(
        """
Normally, an R² barely above 0 might seem underwhelming.
However, in the context of next-day stock return prediction, even a small
positive R² can be meaningful. It indicates that the model is capturing some
generalisable signal in a very noisy and difficult prediction task.

Low R² values are common in financial prediction, and they reflect the inherent
unpredictability of markets. The key point is that the model's performance is
not expected to be perfect, but it should show some evidence of learning from
the data. This is a more realistic and educational success criterion than
expecting a high R², which would be unlikely in this context.

This supports the project's educational message that while
short-term predictions are challenging, there can still be some signal
to learn from, and that long-term scenario thinking is often more sensible
than relying on day-to-day predictions.
"""
    )

    st.divider()

    st.header("Why the model is intentionally limited")

    st.write(
        """
The model predicts only the **next trading day's return**. It does not know
future news, earnings reports, interest-rate decisions, investor sentiment, or
unexpected market shocks.

That limitation is part of the learning goal. It shows beginners that:

- short-term price movement is noisy
- model outputs are estimates, not guarantees
- prediction uncertainty should be communicated clearly
- long-term scenario ranges are more responsible than single-point promises
- therefore, long-term investing is often more sensible than relying on
day-to-day predictions
"""
    )

    st.divider()

    st.header("Best hyperparameters")

    st.write(
        "Hyperparameters are model settings chosen during training. "
        "They control how the Random Forest learns, such as the number "
        "of trees, tree depth, and how splits are made."
        "\n\n"
        "These are the parameters selected during model tuning in the "
        "training notebook."
        "\n\n"
        "These technical settings are included for transparency and "
        "reproducibility."
    )
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
