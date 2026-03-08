# [StockMetrics](https://stockmetrics-emhu.onrender.com)

Developer: Louis Cowell-English ([LouisCE](https://www.github.com/LouisCE))

StockMetrics is a predictive analytics dashboard designed to help beginners understand stock market risk and returns using historical price data and machine learning forecasts.

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/LouisCE/stockmetrics)](https://www.github.com/LouisCE/stockmetrics/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/LouisCE/stockmetrics)](https://www.github.com/LouisCE/stockmetrics/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/LouisCE/stockmetrics)](https://www.github.com/LouisCE/stockmetrics)
[![badge](https://img.shields.io/badge/deployment-Render-teal)](https://stockmetrics-emhu.onrender.com)

---

## Live Dashboard

The StockMetrics dashboard is deployed on Render and available at:

https://stockmetrics-emhu.onrender.com

---

## Project Overview

StockMetrics is a Predictive Analytics dashboard designed to make investing easier for beginners.

Learning how to invest can feel overwhelming. New investors are hit with unfamiliar terms (e.g., *dividends*, *dollar-cost averaging*, *volatility*), countless strategies and overcomplication, which often leads to **analysis paralysis** and ultimately deciding not to invest at all.

StockMetrics exists to cut through the noise and help users to capitalise on their most valuable asset: their time.

The goal is to turn **clueless users into confident investors in fifteen minutes or less** by providing:

- a clear explanation of the purpose of the app.
- simple investing principles to anchor decision-making.
- a small, carefully-chosen set of stocks/funds to keep the experience focused.
- risk-based portfolio “plans” and forecast ranges to help users understand uncertainty.

### Core Investing Principles

StockMetrics reinforces three beginner-friendly principles:

- **Start early:** to benefit from compound growth over time.
- **Think long-term:** time in the market beats timing the market.
- **Diversify:** spread exposure across companies and sectors to help mitigate risk.

### Four Risk-Based Plans

To keep the learning curve low, StockMetrics focuses on well-known index funds and large blue-chip companies. Users can explore four portfolio plans based on risk tolerance:

- **Diversified (Low Risk):** 100% All-World fund
- **Targeted (Moderate Risk):** 100% S&P 500 fund
- **Concentrated (High Risk):** 75% S&P 500 fund + 25% Magnificent Seven
- **Aggressive (Higher Risk):** 50% S&P 500 fund + 25% Magnificent Six + 25% Tesla

Risk levels in StockMetrics refer to how concentrated a portfolio is within the stock market. All plans are equity-based and may experience significant short-term volatility.

StockMetrics includes brief explanations of the funds/companies and (where applicable) a short description of the “Magnificent Seven”, so users understand what they are looking at.

### Forecasts Over Time

StockMetrics provides predicted price outcomes over multiple time horizons:

- 1 year
- 2 years
- 5 years
- 10 years
- 20 years
- 50 years

To reflect uncertainty and volatility, predictions are presented as a range of scenarios:

- **Optimistic**
- **Realistic**
- **Pessimistic**

The four plans are calibrated to be **comparable and easy to switch between**. Users can move from a lower-risk plan to a higher-risk plan as their confidence grows, or from a higher-risk plan to a lower-risk plan if their risk-aversion grows, without completely changing the overall structure of the portfolio.

Ultimately, StockMetrics is designed to be a stepping stone: users can later customise their portfolio or explore other companies and sectors, but StockMetrics helps them start sooner - with clarity and confidence.

---

## Business Requirements

StockMetrics is designed to help **beginner investors understand risk, volatility, and long-term investing behaviour** without requiring advanced financial knowledge.

Many new investors experience **analysis paralysis** due to information overload, unfamiliar terminology, and uncertainty about how markets behave.  
The goal of StockMetrics is to reduce this barrier by presenting financial data in a simplified, visual, and educational format.

This section corresponds to the **Business Understanding stage of CRISP-DM** and defines the problems the project aims to address.

---

### Target Audience

The primary audience for StockMetrics is:

- beginner investors.
- individuals learning basic investing principles.
- users who want to understand market behaviour before investing.

The dashboard focuses on **clarity and simplicity**, using a curated set of widely recognised stocks and index funds rather than overwhelming users with thousands of assets.

---

### Core Business Goals

StockMetrics aims to solve two key problems for beginner investors.

**Problem 1: Understanding historical market behaviour**

New investors often struggle to interpret stock price charts or understand key concepts such as volatility and drawdowns.

StockMetrics addresses this by providing:

- interactive price charts
- daily return analysis
- volatility comparisons
- drawdown calculations

These visualisations help users understand how different assets behave historically.

---

**Problem 2: Understanding uncertainty in future outcomes**

Financial markets are inherently uncertain.  
Many beginner tools present a single predicted outcome, which can be misleading.

StockMetrics instead focuses on **scenario ranges** to demonstrate uncertainty.

The application generates:

- optimistic scenarios
- realistic scenarios
- pessimistic scenarios

This approach helps users understand how volatility affects potential outcomes over time.

---

### Business Requirement 1 - Historical Market Exploration

Users must be able to explore historical price behaviour for a curated set of assets.

The dashboard must allow users to:

- select a ticker
- select a date range
- view price history
- view daily returns
- view return distributions

These features help users understand **how volatile different assets are** and how performance changes over time.

Implemented in:

```
app_pages/stock_explorer.py
src/viz.py
```

---

### Business Requirement 2 - Portfolio Risk Comparison

Users must be able to compare several portfolio structures representing different levels of diversification and concentration.

The dashboard provides four portfolio plans:

- Diversified (Low Risk)
- Targeted (Moderate Risk)
- Concentrated (High Risk)
- Aggressive (Higher Risk)

Each plan demonstrates how portfolio concentration affects:

- returns
- volatility
- drawdowns

This comparison helps users understand the relationship between **risk and diversification**.

Implemented in:

```
app_pages/portfolio_plans.py
src/portfolio.py
```

---

### Business Requirement 3 - Predictive Analytics Feature

The application must include at least one **machine learning task** to support predictive analytics.

StockMetrics implements a supervised machine learning regression model that predicts:

```
next-day return (return_1d)
```

This model is not used to produce trading signals. Instead, it demonstrates how machine learning can attempt to detect patterns in financial time-series data.

The model output is used as an **educational indicator of short-term market uncertainty**.

Implemented in:

```
jupyter_notebooks/05_model_training.ipynb
jupyter_notebooks/06_model_evaluation.ipynb
src/modelling.py
app_pages/model_performance.py
```

---

### Business Requirement 4 - Scenario-Based Forecasting

Users must be able to explore potential future outcomes over multiple time horizons.

StockMetrics generates scenario ranges using historical trend and volatility.

Supported horizons include:

- 1 year
- 2 years
- 5 years
- 10 years
- 20 years
- 50 years

Forecasts are presented as:

- optimistic scenario
- realistic scenario
- pessimistic scenario

This approach helps communicate uncertainty and reinforces the importance of **long-term investing**.

Implemented in:

```
app_pages/predictor.py
src/forecast.py
```

---

### Business Requirement 5 - Clear Communication of Model Results

The dashboard must clearly communicate whether the machine learning model successfully met its business case criteria.

The Model Performance page displays:

- R² score
- MAE
- RMSE
- evaluation plots
- feature importance

This ensures transparency regarding the model’s performance and limitations.

Implemented in:

```
app_pages/model_performance.py
jupyter_notebooks/06_model_evaluation.ipynb
```

---

## Dataset Content

StockMetrics uses **historical financial market data** collected programmatically from Yahoo Finance using the `yfinance` Python library.

The dataset contains **daily time-series price data** for a curated set of global index funds and large technology companies.

Each row represents a single trading day for a specific asset.

Data collection is performed in:

```
jupyter_notebooks/01_data_collection.ipynb
```

This satisfies **CRISP-DM Data Collection** by retrieving data directly from an external endpoint.

---

### Dataset Scope

The project focuses on a small set of widely recognised assets to keep the experience beginner-friendly.

The dataset includes:

- two global index funds
- the Magnificent Seven technology companies

The tickers are defined centrally in:

```
src/config.py
```

This ensures that both the notebooks and the Streamlit dashboard use the same dataset configuration.

---

### ETFs Included

| Ticker | Description |
|------|------|
| VWRL.L | Vanguard FTSE All-World UCITS ETF |
| VUSA.L | Vanguard S&P 500 UCITS ETF |

These funds provide broad exposure to global and US equity markets.

---

### Technology Stocks Included

| Ticker | Company |
|------|------|
| AAPL | Apple |
| AMZN | Amazon |
| GOOGL | Alphabet |
| META | Meta Platforms |
| MSFT | Microsoft |
| NVDA | Nvidia |
| TSLA | Tesla |

These companies are commonly referred to as the **Magnificent Seven**, a group of large technology firms that have significantly influenced recent US market performance.

---

### Data Collection Window

To ensure consistent historical coverage across all assets, the dataset uses a unified start date.

```
Start date: 2012-05-22
End date: Current date (UTC)
```

This date corresponds to the earliest available trading history shared by both ETFs.

The configuration is defined in:

```
src/config.py
```

---

### Raw Dataset Variables

The dataset retrieved from Yahoo Finance contains standard **OHLCV market data**.

| Variable | Description |
|------|------|
| Date | Trading day |
| Open | Opening price |
| High | Highest price during the trading session |
| Low | Lowest price during the trading session |
| Close | Closing price |
| Adj_Close | Adjusted closing price accounting for splits and dividends |
| Volume | Number of shares traded |
| Ticker | Asset identifier |

The **Adjusted Close** price is used for most analysis because it reflects corporate actions such as stock splits and dividend adjustments.

---

### Dataset Versioning

To ensure reproducibility, StockMetrics stores datasets and artefacts in **versioned folders**.

```
data/raw/<version>/
data/processed/<version>/
outputs/<version>/
```

Each processing stage saves both:

- timestamped archive files
- stable "latest" files used by the dashboard

Example:

```
data/processed/v2/clean_prices_v2_latest.csv
```

This design allows experiments to be repeated while keeping a clear audit trail.

---

### Data Processing Workflow

The dataset is prepared through a structured CRISP-DM pipeline implemented across multiple Jupyter notebooks.

| Notebook | Purpose | CRISP-DM Stage |
|------|------|------|
| 01_data_collection.ipynb | Collect raw price data | Data Collection |
| 02_data_cleaning.ipynb | Clean and standardise raw data | Data Preparation |
| 03_eda.ipynb | Explore trends, volatility and correlations | Data Understanding |
| 04_feature_engineering.ipynb | Generate model features | Data Preparation |
| 05_model_training.ipynb | Train and tune the ML model | Modelling |
| 06_model_evaluation.ipynb | Evaluate model performance | Evaluation |

Each notebook begins with clearly defined:

- Objective
- Inputs
- Outputs

to document the workflow and ensure reproducibility.

---

### Data Limitations

Financial market data contains several inherent limitations.

- Markets are closed on weekends and holidays.
- Assets have different listing dates.
- Daily returns contain significant noise.

These limitations are explicitly acknowledged in the project documentation and dashboard explanations to ensure responsible interpretation of results.

