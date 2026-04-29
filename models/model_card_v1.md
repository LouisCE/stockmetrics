# StockMetrics Model Card (v1)

## Version status

This is an earlier model iteration retained as development evidence.

The final submitted and deployed StockMetrics project uses **v2** as the production dataset and artefact version. The v1 model card is kept to show model development, dataset iteration, and experimentation during the project lifecycle.

In v1, the project used accumulating ETF share classes (`VWRP.L` and `VUAG.L`). These are suitable real-world long-term investing examples because accumulating ETFs automatically reinvest dividends.

However, these share classes have shorter available histories. `VUAG.L` has an inception date of 14 May 2019, and `VWRP.L` has an inception date of 23 July 2019. This limited the shared historical window available for modelling and comparison.

These tickers were later replaced in v2 with distributing ETF share classes (`VWRL.L` and `VUSA.L`) because both have inception dates of 22 May 2012. This provided a longer shared historical window for the ETF data and allowed the individual technology stocks to be aligned to the same common start date for fairer comparison and modelling.

## Model purpose
This model predicts a ticker’s **next-day return** (`return_1d`) using engineered
time-series features. StockMetrics uses the output to support **scenario ranges**
(Optimistic / Realistic / Pessimistic) for beginner-friendly education, not precise
short-term trading signals.

## Intended users
Beginner investors using StockMetrics to understand:
- volatility and uncertainty
- long-term investing principles
- portfolio concentration risk

## Training data
- Source: Yahoo Finance via `yfinance` (endpoint collection)
- Tickers: VWRP.L, VUAG.L, AAPL, AMZN, GOOGL, META, MSFT, NVDA, TSLA
- Period: 2010-01-01 to latest run date (see processed dataset metadata)
- Feature file: `data/processed/v1/features_v1_latest.csv`

## Features
Numerical:
- vol_30d, vol_90d
- mom_30d, mom_90d
- drawdown
- lag_return_1, lag_return_5, lag_return_21
Categorical:
- Ticker (OneHotEncoded)

Target:
- `return_1d` (next-day percent return)

## Model and training
- Algorithm: RandomForestRegressor
- Pipeline: preprocessing (imputation + OHE) → model
- Validation: Time-aware split + TimeSeriesSplit CV
- Hyperparameter tuning: GridSearchCV

## Performance (v1)
Report files:
- `outputs/v1/reports/model_training_report_v1.json`
- `outputs/v1/reports/model_evaluation_report_v1.json`

Key metrics:
- Train R²: 0.237789
- Test R²: 0.090510
- Test MAE: 0.013065
- Test RMSE: 0.020477

Business-case success rule:
- **Successful** if Test R² > 0 (generalisation signal on chronological split)

## Limitations and risks
- Daily returns are noisy; predictive signal is limited.
- Model is not designed for short-horizon trading decisions.
- Regime shifts (macro events) can reduce performance.
- Output should be communicated as uncertainty ranges.

## How StockMetrics uses this model
- Converts predicted return into scenario ranges across longer horizons.
- Displays model performance transparently on the dashboard.
- Includes clear disclaimers: educational only, not financial advice.