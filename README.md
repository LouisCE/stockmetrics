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

---

## Epics and User Stories

The project was organised into several Epics that reflect the stages of data science development and dashboard delivery. Each Epic contains a set of User Stories that describe the intended functionality of the StockMetrics application and the development work required to support it.

---

### Epic - Dashboard Introduction and User Guidance

| Target | Expectation | Outcome |
|---|---|---|
| As a beginner investor | I want a simple homepage explaining what StockMetrics does and who it is for | so I can quickly understand the app. |
| As a beginner investor | I want clear disclaimers that this is educational and not financial advice | so I can use the dashboard responsibly. |

---

### Epic - Asset Exploration and Market Insights

| Target | Expectation | Outcome |
|---|---|---|
| As a beginner investor | I want to explore a curated list of well-known stocks and index funds | so I don’t get overwhelmed by too many choices. |
| As a beginner investor | I want to select a ticker and date range | so I can focus analysis on a time period that matters to me. |
| As a beginner investor | I want interactive charts of historical prices and returns | so I can visually understand how performance changes over time. |
| As a beginner investor | I want to view daily returns | so I can understand how volatile an asset is in the short term. |
| As a beginner investor | I want beginner-friendly explanations of investing terms | so I can understand what the dashboard is showing me. |
| As a beginner investor | I want to compare assets using the same metrics | so I can make fair comparisons without guessing. |

---

### Epic - Portfolio Planning and Forecasting

| Target | Expectation | Outcome |
|---|---|---|
| As a beginner investor | I want a forecast for different time horizons (1 to 10 years) | so I can see how profits compound over time. |
| As a beginner investor | I want forecasts presented as optimistic, realistic, and pessimistic scenarios | so I can understand prediction uncertainty instead of seeing one “magic number.” |
| As a beginner investor | I want four risk-based portfolio plans with clear allocations | so I can pick a plan that matches my risk tolerance. |
| As a beginner investor | I want to compare portfolio plans using performance and risk visuals | so I can understand the trade-offs between conservative and aggressive strategies. |

---

### Epic - Data Science Pipeline Development

| Target | Expectation | Outcome |
|---|---|---|
| As a data scientist | I want to collect historical stock data | so the dataset can be used for analysis and modelling. |
| As a data analyst | I want to clean and prepare the dataset | so the data is suitable for analysis and modelling. |
| As a data analyst | I want to explore the dataset visually | so I can understand patterns and relationships in the data. |
| As a data scientist | I want to engineer predictive features | so the machine learning model has meaningful inputs. |
| As a data scientist | I want to train a machine learning model | so the application can assess short-term market uncertainty and support model evaluation. |
| As a data scientist | I want to evaluate the machine learning model | so I can determine whether it meets the business case requirements. |

The workflow is implemented across the following notebooks:

- `jupyter_notebooks/01_data_collection.ipynb`
- `jupyter_notebooks/02_data_cleaning.ipynb`
- `jupyter_notebooks/03_eda.ipynb`
- `jupyter_notebooks/04_feature_engineering.ipynb`
- `jupyter_notebooks/05_model_training.ipynb`
- `jupyter_notebooks/06_model_evaluation.ipynb`

---

### Epic - Model Transparency and Evaluation

| Target | Expectation | Outcome |
|---|---|---|
| As a technical reviewer | I want a model performance page with metrics and evaluation plots | so I can verify whether the ML pipeline meets its business case success criteria. |

---

### Epic - Deployment and Application Availability

| Target | Expectation | Outcome |
|---|---|---|
| As a user | I want the StockMetrics dashboard deployed online | so I can access the application from a live public URL. |
| As a developer | I want the application deployed using Render | so the dashboard can be reliably hosted and accessed by users. |

---

## Project Hypotheses

StockMetrics investigates several hypotheses related to stock market behaviour, diversification, and predictive modelling.  
These hypotheses help frame the exploratory analysis and modelling tasks within the project and guide the interpretation of results.

### Hypothesis 1: Concentrated portfolio plans are riskier than diversified ones but also have greater potential rewards

Large technology companies are often associated with higher growth potential but also greater volatility compared with broadly diversified index funds.

Portfolio plans that concentrate capital in a smaller number of high-growth companies may therefore experience larger gains during strong market periods but also larger losses during downturns.

This hypothesis tests whether portfolio plans that allocate more weight to individual technology stocks exhibit higher volatility and potentially higher returns than broadly diversified ETF-based plans.

### Hypothesis 2: Technology stocks exhibit higher volatility than diversified ETFs

Large technology companies are often perceived as more volatile than diversified index funds because they are exposed to company-specific risks and investor sentiment.

### Hypothesis 3: Diversified portfolios experience smaller drawdowns than concentrated portfolios

Diversification across many companies is widely considered a mechanism for reducing portfolio risk.

This hypothesis tests whether portfolios with broader diversification demonstrate smaller historical drawdowns than more concentrated portfolios.

### Hypothesis 4: Short-horizon return prediction is inherently difficult

Financial markets are known to be noisy and difficult to predict over short time horizons.

This hypothesis evaluates whether a machine learning model can successfully predict next-day stock returns.

---

## CRISP-DM Process

StockMetrics follows the CRISP-DM (Cross Industry Standard Process for Data Mining) framework to structure the data science workflow.

| CRISP-DM Stage | Implementation |
|---|---|
| Business Understanding | Defined business requirements and project hypotheses |
| Data Collection | `01_data_collection.ipynb` retrieves historical price data from the Yahoo Finance API using `yfinance` |
| Data Preparation | `02_data_cleaning.ipynb` cleans the dataset and `04_feature_engineering.ipynb` generates model features |
| Data Understanding | `03_eda.ipynb` explores trends, volatility, correlations and drawdowns |
| Modelling | `05_model_training.ipynb` trains and tunes the machine learning pipeline |
| Evaluation | `06_model_evaluation.ipynb` evaluates model performance and validates the ML business case |
| Deployment | Streamlit dashboard deployed online via Render |

Each stage produces reproducible outputs that are saved in **versioned project folders** such as:

- `data/raw/<version>/`
- `data/processed/<version>/`
- `outputs/<version>/`

This structure ensures that datasets, models and evaluation artefacts remain reproducible across project iterations.

---

## Rationale to map the business requirements to the Data Visualisations and ML tasks

This section links each business requirement to the analysis or machine learning task used to address it.

| Business Requirement | Data Analysis / Visualisation | ML Task |
|---|---|---|
| Historical Market Exploration | Price charts, daily returns visualisation, and return distribution histograms | — |
| Portfolio Risk Comparison | Portfolio equity curves, volatility metrics, and drawdown analysis | — |
| Predictive Analytics Feature | Model evaluation plots, feature importance visualisation | Regression model predicting next-day returns |
| Scenario-Based Forecasting | Scenario tables showing optimistic, realistic, and pessimistic outcomes | — |
| Clear Communication of Model Results | Actual vs predicted plots, residual analysis, and performance metrics | Evaluation of regression model performance (R², MAE, RMSE) |

This mapping ensures that each dashboard component directly supports the project’s business objectives.

---

## ML Business Case

### Predictive Task

The machine learning task in StockMetrics is supervised regression.

The model predicts:

```
next-day return (return_1d)
```

This task is intentionally framed as a predictive analytics demonstration, rather than a trading signal generator.

---

### Learning Method

The model uses a RandomForestRegressor ensemble model, a tree-based ensemble learning method well suited to tabular datasets.

Random Forest models:

- capture nonlinear relationships
- are robust to noisy data
- provide feature importance estimates

---

### Feature Engineering

Features used in the model include:

- rolling volatility measures
- momentum indicators
- drawdown metrics
- lagged returns

These features are engineered in:

```
jupyter_notebooks/04_feature_engineering.ipynb
src/features.py
```

---

### Hyperparameter Optimisation

Hyperparameter optimisation was implemented using:

```
GridSearchCV
```

with a TimeSeriesSplit cross-validation strategy to ensure chronological validation.

Six hyperparameters were tuned:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf
- max_features
- max_leaf_nodes

Each hyperparameter includes at least three candidate values, satisfying the advanced modelling requirement.

---

### Success Criteria

Primary evaluation metric:

```
Test R² > 0
```

Secondary metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

If the model achieves a positive test-set R², it indicates that the model captures some generalisable signal in the dataset.

---

### Model Output and User Relevance

The model predicts next-day returns, which are highly noisy in financial markets.

Therefore the predictions are not used directly as trading signals.

Instead, the model serves two purposes:

1. Demonstrating how machine learning can analyse financial time-series data.
2. Supporting educational insights about uncertainty and prediction difficulty.

Long-horizon forecasts in the dashboard are generated using historical trend and volatility simulations, rather than compounding daily ML predictions.
