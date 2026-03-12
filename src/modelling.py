"""
Model training + hyperparameter tuning.

This file is used by 05_model_training.ipynb and later by the Streamlit app.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.experimental import enable_halving_search_cv  # noqa: F401
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV, HalvingGridSearchCV, TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


TARGET_COL = "return_1d"

FEATURE_COLS_NUM = [
    "vol_30d",
    "vol_90d",
    "mom_30d",
    "mom_90d",
    "drawdown",
    "lag_return_1",
    "lag_return_5",
    "lag_return_21",
]

FEATURE_COLS_CAT = ["Ticker"]


@dataclass(frozen=True)
class TrainResult:
    model: Pipeline
    best_params: Dict[str, object]
    metrics_train: Dict[str, float]
    metrics_test: Dict[str, float]


def time_split(
    df: pd.DataFrame,
    test_size: float = 0.2,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Simple chronological split per full dataset (assumes Date-sorted)."""
    df = df.sort_values(["Date"]).reset_index(drop=True)
    n = len(df)
    cut = int(np.floor(n * (1 - test_size)))
    return df.iloc[:cut].copy(), df.iloc[cut:].copy()


def build_pipeline() -> Pipeline:
    """Preprocess + model pipeline."""
    numeric = Pipeline(steps=[("imputer", SimpleImputer(strategy="median"))])
    categorical = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    pre = ColumnTransformer(
        transformers=[
            ("num", numeric, FEATURE_COLS_NUM),
            ("cat", categorical, FEATURE_COLS_CAT),
        ]
    )

    model = RandomForestRegressor(random_state=42, n_jobs=1)

    pipe = Pipeline(steps=[("preprocess", pre), ("model", model)])
    return pipe


def get_param_grid(fast: bool = False) -> Dict[str, list[object]]:
    """
    Hyperparameter options for search.

    fast=True:
        Small grid used for quick validation during notebook development.

    fast=False:
        Full parameter space:
        6 hyperparameters, each with 3 distinct acceptable values.
    """
    if fast:
        return {
            "model__n_estimators": [25, 50],
            "model__max_depth": [5, 10],
            "model__min_samples_split": [2],
            "model__min_samples_leaf": [1],
            "model__max_features": ["sqrt"],
            "model__max_leaf_nodes": [200],
        }

    return {
        "model__n_estimators": [100, 200, 300],
        "model__max_depth": [5, 10, None],
        "model__min_samples_split": [2, 5, 10],
        "model__min_samples_leaf": [1, 2, 4],
        "model__max_features": ["sqrt", "log2", 0.5],
        "model__max_leaf_nodes": [50, 200, None],
    }


def train_and_tune(
    feat_df: pd.DataFrame,
    test_size: float = 0.2,
    fast: bool = False,
) -> TrainResult:
    """
    Train + tune on a time-aware CV search.

    Target: next-day return (return_1d).

    fast=True:
        Uses GridSearchCV on a small grid for quick notebook iteration.

    fast=False:
        Uses HalvingGridSearchCV on the full parameter
        space to reduce runtime while still searching across all defined
        hyperparameter options.
    """
    df = feat_df.dropna(
        subset=FEATURE_COLS_NUM + FEATURE_COLS_CAT + [TARGET_COL]
    ).copy()
    df = df.sort_values(["Date", "Ticker"]).reset_index(drop=True)

    train_df, test_df = time_split(df, test_size=test_size)

    X_train = train_df[FEATURE_COLS_NUM + FEATURE_COLS_CAT]
    y_train = train_df[TARGET_COL].astype(float)

    X_test = test_df[FEATURE_COLS_NUM + FEATURE_COLS_CAT]
    y_test = test_df[TARGET_COL].astype(float)

    pipe = build_pipeline()
    grid = get_param_grid(fast=fast)

    tscv = TimeSeriesSplit(n_splits=3)

    if fast:
        search = GridSearchCV(
            estimator=pipe,
            param_grid=grid,
            scoring="r2",
            cv=tscv,
            n_jobs=1,
            verbose=2,
        )
    else:
        search = HalvingGridSearchCV(
            estimator=pipe,
            param_grid=grid,
            scoring="r2",
            cv=tscv,
            factor=3,
            resource="n_samples",
            max_resources="auto",
            min_resources="exhaust",
            n_jobs=1,
            verbose=2,
        )

    search.fit(X_train, y_train)
    best_model = search.best_estimator_

    pred_train = best_model.predict(X_train)
    pred_test = best_model.predict(X_test)

    metrics_train = {
        "r2": float(r2_score(y_train, pred_train)),
        "mae": float(mean_absolute_error(y_train, pred_train)),
        "rmse": float(mean_squared_error(y_train, pred_train, squared=False)),
    }
    metrics_test = {
        "r2": float(r2_score(y_test, pred_test)),
        "mae": float(mean_absolute_error(y_test, pred_test)),
        "rmse": float(mean_squared_error(y_test, pred_test, squared=False)),
    }

    return TrainResult(
        model=best_model,
        best_params=search.best_params_,
        metrics_train=metrics_train,
        metrics_test=metrics_test,
    )


def save_model(model: Pipeline, models_dir: Path, filename: str) -> Path:
    models_dir.mkdir(parents=True, exist_ok=True)
    path = models_dir / filename
    joblib.dump(model, path)
    return path
