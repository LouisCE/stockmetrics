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

    st.info(
        "This result reflects the saved model and processed dataset included "
        "with this project version. If the full notebook pipeline is re-run "
        "from data collection using newer Yahoo Finance data, the latest "
        "date, model metrics, and predictions may change. This is expected "
        "because the project uses live endpoint data during collection.",
        icon="ℹ️"
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

    st.info(
        "The low R² score is part of the lesson. It shows that even when a "
        "machine learning model detects a small signal, short-term market "
        "prediction remains unreliable. This supports StockMetrics' message "
        "that long-term investing and scenario thinking are generally more "
        "sensible for beginners than short-term day trading.",
        icon="ℹ️",
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

- Short-term price movement is noisy.
- Model outputs are estimates, not guarantees.
- Prediction uncertainty should be communicated clearly.
- Long-term scenario ranges are more responsible than single-point promises.
- Therefore, long-term investing is often more sensible than relying on
day-to-day predictions.
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

    st.header("Hyperparameter search space")

    st.write(
        "The final model tuning used six Random Forest hyperparameters, "
        "each with three distinct values. This created a full search space "
        "of 3⁶ = 729 possible parameter combinations before successive "
        "halving was applied to reduce runtime."
    )

    search_space = pd.DataFrame(
        [
            {
                "Hyperparameter": "n_estimators",
                "Values tested": "100, 200, 300",
            },
            {
                "Hyperparameter": "max_depth",
                "Values tested": "5, 10, None",
            },
            {
                "Hyperparameter": "min_samples_split",
                "Values tested": "2, 5, 10",
            },
            {
                "Hyperparameter": "min_samples_leaf",
                "Values tested": "1, 2, 4",
            },
            {
                "Hyperparameter": "max_features",
                "Values tested": "sqrt, log2, 0.5",
            },
            {
                "Hyperparameter": "max_leaf_nodes",
                "Values tested": "50, 200, None",
            },
        ]
    )

    st.dataframe(search_space, use_container_width=True, hide_index=True)

    st.divider()

    st.header("Evaluation plots")

    st.write(
        """
These plots are technical checks from the evaluation notebook. They help show
whether the model generalised to unseen data and whether prediction errors
looked reasonable.

They also provide dashboard-visible evidence of multiple plot types, including
scatter plots, histograms, and time-series plots.
"""
    )

    st.info(
        "**How to read these plots:**\n\n"
        "- **Actual vs predicted plots** compare the model's estimates with "
        "the real next-day returns. If the model were highly accurate, points "
        "would sit closer to a clear diagonal pattern. In this project, the "
        "relationship is weak, which matches the very small positive R².\n"
        "- The **residual histogram** shows prediction errors. A residual is "
        "the gap between the actual value and the predicted value. Errors "
        "clustered near zero are better, but wide spread means uncertainty "
        "remains high.\n"
        "- The **time-series plots** show how predictions and errors behaved "
        "over time. Large spikes or clusters of errors show that short-term "
        "market prediction is unstable across different market conditions.",
        icon="ℹ️"
    )

    plot_files = [
        (
            figures / f"eval_actual_vs_pred_train_{version}.png",
            "Train set: actual vs predicted returns",
        ),
        (
            figures / f"eval_actual_vs_pred_test_{version}.png",
            "Test set: actual vs predicted returns",
        ),
        (
            figures / f"eval_residuals_hist_test_{version}.png",
            "Test set: prediction error distribution",
        ),
        (
            figures / f"eval_residuals_timeseries_test_{version}.png",
            "Test set: prediction errors over time",
        ),
        (
            figures / f"eval_pred_timeseries_test_{version}.png",
            "Test set: actual vs predicted returns over time",
        ),
    ]

    for path, caption in plot_files:
        if path.exists():
            st.image(str(path), caption=caption, use_container_width=True)
        else:
            st.warning(f"Missing: {path.name}")

    st.divider()

    st.header("EDA plot evidence for hypotheses")

    st.write(
        """
These additional EDA plots support the project hypotheses and business
requirements around volatility, diversification, concentration risk, and
cross-asset relationships.
"""
    )

    st.info(
        "**How to read these plots:**\n\n"
        "- The **price time-series plot** shows how each asset's adjusted "
        "closing price changed over time. Rising lines show historical "
        "growth, while sharper rises and falls show a bumpier journey.\n"
        "- The **daily returns time-series plot** shows short-term ups and "
        "downs. Larger spikes mean larger day-to-day moves.\n"
        "- The **returns histogram** shows which daily return outcomes were "
        "common and which were more extreme.\n"
        "- The **box plot** compares how spread out each asset's daily "
        "returns were. A taller box or longer whiskers usually means more "
        "volatility and more extreme daily moves.\n"
        "- The **correlation heatmap** shows how similarly assets moved "
        "compared with each other. Stronger relationships mean assets tended "
        "to rise and fall together, while weaker relationships suggest more "
        "diversification benefit.\n"
        "- The **rolling volatility plot** shows how risk changed over time. "
        "Spikes mean the asset had a period of larger day-to-day movements.",
        icon="ℹ️"
    )

    eda_plot_files = [
        (
            figures / "eda_adj_close_timeseries.png",
            "Adjusted close time series: long-term price trends",
        ),
        (
            figures / "eda_daily_returns_timeseries.png",
            "Daily returns time series: short-term volatility patterns",
        ),
        (
            figures / "eda_daily_returns_hist.png",
            "Daily returns histogram: common and extreme daily outcomes",
        ),
        (
            figures / "eda_daily_returns_boxplot.png",
            "Daily returns box plot: volatility and outlier comparison",
        ),
        (
            figures / "eda_returns_correlation_heatmap.png",
            "Correlation heatmap: relationship between asset returns",
        ),
        (
            figures / "eda_rolling_volatility_30d.png",
            "Rolling volatility: changing short-term risk over time",
        ),
    ]

    for path, caption in eda_plot_files:
        if path.exists():
            st.image(str(path), caption=caption, use_container_width=True)
        else:
            st.warning(f"Missing: {path.name}")

    st.divider()

    st.header("Feature importance")

    st.write(
        """
Feature importance shows which inputs the fitted model relied on most.

Higher-ranked features had more influence on the model's predictions.

This does **not** prove that those features cause future returns. It only shows
which features were most useful to the model when making predictions.
"""
    )

    fi_path = reports / f"feature_importance_{version}.csv"
    if fi_path.exists():
        fi = pd.read_csv(fi_path)
        st.dataframe(fi.head(20), use_container_width=True, hide_index=True)
    else:
        st.warning("Feature importance file not found.")

    st.divider()

    st.header("ML model summary")

    st.write(
        "The model showed a small positive signal on unseen data, meeting the "
        "project's educational business case. However, the signal was weak, "
        "which supports the app's beginner-friendly message that short-term "
        "market prediction is difficult and uncertain. The evaluation plots "
        "and feature importance provide additional insights into how the "
        "model made predictions and which features it relied on."
    )
