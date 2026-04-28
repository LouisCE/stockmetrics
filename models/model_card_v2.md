# StockMetrics Model Card (v2)

## Model purpose

This model predicts a ticker's **next-day return** using engineered time-series features.

In StockMetrics, the model is used as a short-term educational signal to help beginners understand that daily market prediction is difficult and noisy.

The model is **not** used as a trading tool. It is also **not** used to generate the long-term scenario ranges shown on the Predictor page.

Long-term scenario ranges are generated separately using historical trend and volatility.

## Intended users

StockMetrics is designed for beginner investors who want to understand:

- short-term market uncertainty
- volatility and drawdown
- why long-term thinking can be more useful than day trading
- how model performance should be interpreted cautiously

## Training data

- Source: Yahoo Finance via `yfinance`
- Collection method: endpoint data collection in `01_data_collection.ipynb`
- Dataset version: `v2`
- Feature file: `data/processed/v2/features_v2_latest.csv`
- Tickers:
  - VWRL.L
  - VUSA.L
  - AAPL
  - AMZN
  - GOOGL
  - META
  - MSFT
  - NVDA
  - TSLA
- Start date: 2012-05-22
- End date: latest project data collection run

## Features

Numerical features:

- `vol_30d`
- `vol_90d`
- `mom_30d`
- `mom_90d`
- `zscore_30d`
- `mean_reversion_5d`
- `drawdown`
- `lag_return_1`
- `lag_return_5`
- `lag_return_21`

Categorical feature:

- `Ticker`

Target:

- `target_next_day_return`

The target is defined as the next day's return:

`target_next_day_return = return_1d.shift(-1)`

## Model and training

- Learning method: supervised regression
- Algorithm: `RandomForestRegressor`
- Pipeline:
  - numerical imputation
  - categorical imputation
  - one-hot encoding for ticker
  - random forest regression model
- Validation approach:
  - chronological train/test split
  - `TimeSeriesSplit` cross-validation
- Hyperparameter optimisation:
  - `HalvingGridSearchCV`
  - six hyperparameters tuned
  - at least three values tested per hyperparameter in the full grid

## Hyperparameters tuned

The full tuning grid included:

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_features`
- `max_leaf_nodes`

The final selected parameters are stored in:

- `outputs/v2/reports/model_training_report_v2.json`

## Performance

Evaluation report:

- `outputs/v2/reports/model_evaluation_report_v2.json`

Key final metrics:

- Train R²: 0.035236
- Test R²: 0.000740
- Test MAE: 0.013721
- Test RMSE: 0.021400

## Business-case success rule

The model was considered successful against the project business case if:

- Test R² > 0

The final v2 model achieved a positive Test R², meaning it showed a small generalisable signal on unseen chronological test data.

However, the signal is weak. This is expected for short-term financial return prediction and is communicated clearly in the dashboard.

## Interpretation

The model met the minimum project success rule, but it should not be interpreted as a reliable short-term trading predictor.

For StockMetrics, this result supports the educational message that:

- daily market returns are noisy
- short-term prediction is difficult
- single-point forecasts should be treated carefully
- long-term scenario ranges are more appropriate for beginner education

## Limitations and risks

- The model is trained on historical data and cannot know future market events.
- Daily financial returns are noisy and difficult to predict.
- The positive R² is very small, so the model has weak predictive strength.
- Market regimes can change, reducing model relevance over time.
- The model should not be used for real trading decisions.
- The dashboard is educational only and does not provide financial advice.

## How StockMetrics uses this model

StockMetrics uses the model to display a short-term next-day return estimate as an educational snapshot.

The long-term Predictor page scenarios are generated separately using historical trend and volatility. This avoids compounding noisy daily ML predictions over long horizons.

This separation helps StockMetrics communicate uncertainty responsibly.