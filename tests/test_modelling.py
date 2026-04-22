"""
Pytest checks for lightweight modelling helpers in `src/modelling.py`.
"""

import pandas as pd

from src.modelling import get_param_grid, time_split


def test_get_param_grid_full_has_expected_keys() -> None:
    grid = get_param_grid(fast=False)

    expected = {
        "model__n_estimators",
        "model__max_depth",
        "model__min_samples_split",
        "model__min_samples_leaf",
        "model__max_features",
        "model__max_leaf_nodes",
    }

    assert expected.issubset(grid.keys())


def test_get_param_grid_full_uses_advanced_modelling_threshold() -> None:
    grid = get_param_grid(fast=False)

    for values in grid.values():
        assert len(values) >= 3


def test_get_param_grid_fast_returns_smaller_grid() -> None:
    grid = get_param_grid(fast=True)

    assert "model__n_estimators" in grid
    assert len(grid["model__n_estimators"]) == 2


def test_time_split_preserves_order() -> None:
    df = pd.DataFrame(
        {
            "Date": pd.date_range("2024-01-01", periods=10, freq="D"),
            "value": range(10),
        }
    )

    train_df, test_df = time_split(df, test_size=0.2)

    assert len(train_df) == 8
    assert len(test_df) == 2
    assert train_df["Date"].max() < test_df["Date"].min()
