# Project Testing

> [!NOTE]
> Return to the [README.md](README.md) file.

---

## Code Validation

All custom-written code for the **StockMetrics** project was validated using appropriate tools to help ensure standards compliance, readability, and correctness.

Validation focused on the final project code that supports the deployed dashboard and notebook workflow.

---

### Python Files

All custom Python `.py` files were validated using the **PEP 8 CI Python Linter** to check compliance with **PEP 8** standards and general Python best practices.

- [PEP 8 CI Python Linter](https://pep8ci.herokuapp.com)

---

#### Validation Approach

Each Python file was validated by:

1. Opening the file in the GitHub repository.
2. Selecting the **Raw** view to obtain the direct raw file URL.
3. Appending that raw URL to the PEP 8 CI validator base URL.
4. Running validation against the raw file.

This approach provides a consistent and repeatable way to validate the final committed Python files.

---

#### Excluded Files

The following files and directories were intentionally excluded from PEP 8 validation because they are auto-generated, non-Python, configuration-only, or not part of the custom Python application logic:

- generated artefacts such as saved datasets, model files, and report outputs
- notebook metadata and saved cell outputs within `.ipynb` files
- non-Python project files such as `.gitignore`, `.python-version`, `requirements.txt`, `requirements-dev.txt`, `runtime.txt`, `Procfile`, `setup.sh`, `README.md`, and `TESTING.md`
- image, JSON, and CSV artefacts used for documentation, reporting, or deployment support

Only custom Python files directly maintained as part of the StockMetrics codebase were validated with the PEP 8 CI Python Linter.

---

#### Python Validation Results

| Directory | File | GitHub File | Validator URL | Screenshot | Notes |
| --- | --- | --- | --- | --- | --- |
| - | `app.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app.py) | ![screenshot](documentation/validation/app.png) | No issues found |
| `app_pages/` | `__init__.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app_pages/__init__.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app_pages/__init__.py) | ![screenshot](documentation/validation/app_pages/__init__.png) | No issues found |
| `app_pages/` | `home.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app_pages/home.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app_pages/home.py) | ![screenshot](documentation/validation/app_pages/home.png) | No issues found |
| `app_pages/` | `stock_explorer.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app_pages/stock_explorer.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app_pages/stock_explorer.py) | ![screenshot](documentation/validation/app_pages/stock_explorer.png) | No issues found |
| `app_pages/` | `predictor.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app_pages/predictor.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app_pages/predictor.py) | ![screenshot](documentation/validation/app_pages/predictor.png) | No issues found |
| `app_pages/` | `portfolio_plans.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app_pages/portfolio_plans.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app_pages/portfolio_plans.py) | ![screenshot](documentation/validation/app_pages/portfolio_plans.png) | No issues found |
| `app_pages/` | `model_performance.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/app_pages/model_performance.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/app_pages/model_performance.py) | ![screenshot](documentation/validation/app_pages/model_performance.png) | No issues found |
| `src/` | `__init__.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/__init__.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/__init__.py) | ![screenshot](documentation/validation/src/__init__.png) | No issues found |
| `src/` | `config.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/config.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/config.py) | ![screenshot](documentation/validation/src/config.png) | No issues found |
| `src/` | `data_collection.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/data_collection.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/data_collection.py) | ![screenshot](documentation/validation/src/data_collection.png) | No issues found |
| `src/` | `data_processing.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/data_processing.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/data_processing.py) | ![screenshot](documentation/validation/src/data_processing.png) | No issues found |
| `src/` | `evaluation.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/evaluation.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/evaluation.py) | ![screenshot](documentation/validation/src/evaluation.png) | No issues found |
| `src/` | `features.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/features.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/features.py) | ![screenshot](documentation/validation/src/features.png) | No issues found |
| `src/` | `forecast.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/forecast.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/forecast.py) | ![screenshot](documentation/validation/src/forecast.png) | No issues found |
| `src/` | `modelling.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/modelling.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/modelling.py) | ![screenshot](documentation/validation/src/modelling.png) | No issues found |
| `src/` | `portfolio.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/portfolio.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/portfolio.py) | ![screenshot](documentation/validation/src/portfolio.png) | No issues found |
| `src/` | `viz.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/src/viz.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/src/viz.py) | ![screenshot](documentation/validation/src/viz.png) | No issues found |
| `tests/` | `test_config.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/tests/test_config.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/tests/test_config.py) | ![screenshot](documentation/validation/tests/test_config.png) | No issues found |
| `tests/` | `test_data_processing.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/tests/test_data_processing.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/tests/test_data_processing.py) | ![screenshot](documentation/validation/tests/test_data_processing.png) | No issues found |
| `tests/` | `test_features.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/tests/test_features.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/tests/test_features.py) | ![screenshot](documentation/validation/tests/test_features.png) | No issues found |
| `tests/` | `test_forecast.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/tests/test_forecast.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/tests/test_forecast.py) | ![screenshot](documentation/validation/tests/test_forecast.png) | No issues found |
| `tests/` | `test_modelling.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/tests/test_modelling.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/tests/test_modelling.py) | ![screenshot](documentation/validation/tests/test_modelling.png) | No issues found |
| `tests/` | `test_portfolio.py` | [View](https://github.com/LouisCE/stockmetrics/blob/main/tests/test_portfolio.py) | [PEP 8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LouisCE/stockmetrics/refs/heads/main/tests/test_portfolio.py) | ![screenshot](documentation/validation/tests/test_portfolio.png) | No issues found |

---

### Jupyter Notebooks

Because Jupyter Notebook (`.ipynb`) files store code, Markdown, metadata, and output in JSON format, they were not validated as raw notebook files like the `.py` files above. Instead, the executable Python code cells were manually copied and pasted into the **PEP 8 CI Python Linter** for validation.

For notebook validation, only the **Python code cells** were checked. Markdown cells and notebook metadata were excluded because they are documentation rather than executable Python code.

---

#### Notebook Validation Approach

Each notebook was reviewed by validating its Python code cells separately. This ensured that the executable notebook code was checked for PEP 8 issues without treating notebook metadata or Markdown content as Python.

For validation purposes, notebook Python code cells were pasted into the PEP 8 CI linter as a single script. A short notebook title comment was included at the top of each pasted validation input only to make the validation screenshots easier to identify; this was not added to the real notebook code cells because each notebook already includes its title in the opening Markdown section.

Where necessary, imports were grouped at the top of the pasted validation input to satisfy linter expectations without changing the actual notebook logic, execution order, or saved outputs.

---

#### Notebook Validation Results

| Directory | File | GitHub File | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| `jupyter_notebooks/` | `01_data_collection.ipynb` | [View](https://github.com/LouisCE/stockmetrics/blob/main/jupyter_notebooks/01_data_collection.ipynb) | ![screenshot](documentation/validation/jupyter_notebooks/01_data_collection.png) | Python code cells validated |
| `jupyter_notebooks/` | `02_data_cleaning.ipynb` | [View](https://github.com/LouisCE/stockmetrics/blob/main/jupyter_notebooks/02_data_cleaning.ipynb) | ![screenshot](documentation/validation/jupyter_notebooks/02_data_cleaning.png) | Python code cells validated |
| `jupyter_notebooks/` | `03_eda.ipynb` | [View](https://github.com/LouisCE/stockmetrics/blob/main/jupyter_notebooks/03_eda.ipynb) | ![screenshot](documentation/validation/jupyter_notebooks/03_eda.png) | Python code cells validated |
| `jupyter_notebooks/` | `04_feature_engineering.ipynb` | [View](https://github.com/LouisCE/stockmetrics/blob/main/jupyter_notebooks/04_feature_engineering.ipynb) | ![screenshot](documentation/validation/jupyter_notebooks/04_feature_engineering.png) | Python code cells validated |
| `jupyter_notebooks/` | `05_model_training.ipynb` | [View](https://github.com/LouisCE/stockmetrics/blob/main/jupyter_notebooks/05_model_training.ipynb) | ![screenshot](documentation/validation/jupyter_notebooks/05_model_training.png) | Python code cells validated |
| `jupyter_notebooks/` | `06_model_evaluation.ipynb` | [View](https://github.com/LouisCE/stockmetrics/blob/main/jupyter_notebooks/06_model_evaluation.ipynb) | ![screenshot](documentation/validation/jupyter_notebooks/06_model_evaluation.png) | Python code cells validated |

---

### Code Validation Summary

- All custom `.py` files passed PEP 8 validation.
- Notebook validation was carried out on executable Python code cells only.
- No unresolved linting issues remain in the validated `.py` files or notebook validation inputs.
- Validation confirmed that the custom codebase is clean, readable, and suitable for submission.

---

## Automated Testing

Automated testing was implemented using `pytest` to validate reusable project logic within the `src/` modules.

The tests focused on deterministic functions and data-processing helpers where expected outputs could be asserted reliably without depending on Streamlit UI rendering or expensive model-training runs.

This approach complemented manual dashboard testing by adding repeatable checks for backend logic while keeping the test suite lightweight and practical for the project scope.

---

### Automated Test Scope

Automated tests were created for:

- configuration helpers
- data cleaning and schema consistency
- feature engineering outputs
- chronological train/test splitting
- portfolio calculation helpers
- forecasting utility functions

The Streamlit interface itself was tested manually, while backend logic was tested automatically.

---

### Test Execution

| Test Module | Command Used | Result | Screenshot |
| --- | --- | --- | --- |
| config tests | `python -m pytest tests/test_config.py` | Passed | ![screenshot](documentation/tests/test_config.png) |
| data processing tests | `python -m pytest tests/test_data_processing.py` | Passed | ![screenshot](documentation/tests/test_data_processing.png) |
| features tests | `python -m pytest tests/test_features.py` | Passed | ![screenshot](documentation/tests/test_features.png) |
| forecast tests | `python -m pytest tests/test_forecast.py` | Passed | ![screenshot](documentation/tests/test_forecast.png) |
| modelling tests | `python -m pytest tests/test_modelling.py` | Passed | ![screenshot](documentation/tests/test_modelling.png) |
| portfolio tests | `python -m pytest tests/test_portfolio.py` | Passed | ![screenshot](documentation/tests/test_portfolio.png) |
| full suite | `python -m pytest` | All tests passed | ![screenshot](documentation/tests/test_full.png) |

> **Full test suite result:** 21 tests passed in 3.15 seconds

---

### Automated Testing Summary

- Core reusable functions were tested in isolation.
- Automated tests increased confidence in data handling, calculations, and scenario logic.
- The Streamlit UI was validated manually, while backend logic was validated automatically.

Automated testing was intentionally focused on reusable backend logic rather than full application coverage.

The following parts of the project were not prioritised for automated unit tests:

- `app.py` and `app_pages/`, because these files mainly handle Streamlit page layout, routing, and UI rendering, which were better validated through manual functional and widget testing
- `jupyter_notebooks/`, because these notebooks were assessed through successful execution, saved outputs, and documented evidence rather than isolated unit tests
- selected `src/` modules such as `data_collection.py`, `viz.py`, and `evaluation.py`, because they either depend on external services, generate visual outputs, or were less suitable for lightweight deterministic unit testing than the core reusable logic covered here

This kept the automated test suite lightweight, relevant, and aligned with the overall project architecture and testing strategy.

---

## User Story Testing

User Story Testing was carried out by manually checking the deployed dashboard against the implemented dashboard User Stories.

This section focuses on dashboard behaviour only. Code validation, notebook validation, automated testing, deployment testing, widget interaction testing, and bug tracking are documented separately in this file.

The following dashboard epics are linked to the relevant implementation milestones documented in README.md.

---

### Epic - Dashboard Structure and Navigation System

This Epic is linked to **Milestone 3**.

This Epic covers the main Streamlit entry point in `app.py`, including branding, navigation, disclaimer messaging, routing, and the persistent footer.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a beginner investor | I want the browser tab to show the StockMetrics name and chart icon | so the dashboard feels branded, professional, and easy to identify. | ![screenshot](documentation/dashboard/favicon.png) |
| As a beginner investor | I want to see the StockMetrics title and tagline | so I immediately understand the dashboard purpose. | ![screenshot](documentation/dashboard/title_tagline.png) |
| As a beginner investor | I want a clear sidebar navigation menu | so I can move easily between all dashboard pages. | ![screenshot](documentation/dashboard/navigation_menu.png)  |
| As a beginner investor | I want each navigation option to load the correct page | so the app feels reliable and consistent. | ![screenshot](documentation/dashboard/routing.png)  |
| As a beginner investor | I want a visible educational disclaimer | so I understand the dashboard is not financial advice. | ![screenshot](documentation/dashboard/disclaimer.png) |
| As a beginner investor | I want a persistent footer with attribution and GitHub access | so I can identify the project source and repository. | ![screenshot](documentation/dashboard/footer.png) |

---

### Epic - Home Page and User Onboarding

This Epic is linked to **Milestone 3**.

This Epic covers the `app_pages/home.py` page, which introduces StockMetrics and provides beginner-friendly investing guidance.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a beginner investor | I want a welcoming title and inspirational quote | so I feel motivated to begin my investing journey. | ![screenshot](documentation/dashboard/home_title_intro.png) |
| As a beginner investor | I want a clear Home page introduction and hero image | so I understand that StockMetrics helps explain risk, returns, and uncertainty without overwhelming me. | ![screenshot](documentation/dashboard/home_hero_image.png) |
| As a beginner investor | I want the app purpose and audience explained | so I understand how StockMetrics helps beginners in more detail. | ![screenshot](documentation/dashboard/home_purpose_section.png) |
| As an assessor | I want a project validation summary on the dashboard | so I can quickly see how business requirements and hypotheses are supported by dashboard evidence. | ![screenshot](documentation/dashboard/home_validation_summary.png) |
| As a beginner investor | I want core investing principles displayed | so I can learn the basic ideas of starting early, thinking long-term, and diversifying. | ![screenshot](documentation/dashboard/home_core_principles.png) |
| As a beginner investor | I want a plain-English glossary | so I can understand key investing terms. | ![screenshot](documentation/dashboard/home_glossary.png) |
| As a beginner investor | I want expandable FAQs | so I can learn answers to common beginner investing questions. | ![screenshot](documentation/dashboard/home_faq_expanders.png) |
| As a beginner investor | I want a preview of the four risk-based plans | so I understand the available portfolio styles before comparing them. | ![screenshot](documentation/dashboard/home_plan_preview.png) |

---

### Epic - Stock Explorer and Asset Education

This Epic is linked to **Milestone 4**.

This Epic covers the `app_pages/stock_explorer.py` page, which allows users to explore selected assets using historical price and return data.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a beginner investor | I want a clear Stock Explorer introduction and hero image | so I understand the purpose of the page. | ![screenshot](documentation/dashboard/stock_intro_hero.png) |
| As a beginner investor | I want to select an asset from a curated dropdown | so I can explore a specific stock or ETF without being overwhelmed. | ![screenshot](documentation/dashboard/stock_asset_select.png) |
| As a beginner investor | I want to select a date range | so I can focus on a specific time period. | ![screenshot](documentation/dashboard/stock_date_range.png) |
| As a beginner investor | I want key metrics for my selected asset and period | so I understand the data scope being shown. | ![screenshot](documentation/dashboard/stock_metrics.png) |
| As a beginner investor | I want an interactive price chart | so I can visualise historical price movement. | ![screenshot](documentation/dashboard/stock_price_chart.png) |
| As a beginner investor | I want an interactive daily returns chart | so I can understand short-term movement and volatility. | ![screenshot](documentation/dashboard/stock_returns_chart.png) |
| As a beginner investor | I want an interactive return distribution chart | so I can see common and extreme daily return outcomes. | ![screenshot](documentation/dashboard/stock_distribution_chart.png) |
| As a beginner investor | I want educational chart captions and messages | so I understand that historical data is for learning, not trading signals. | ![screenshot](documentation/dashboard/stock_chart_guidance.png) |
| As a beginner investor | I want expandable asset explanations | so I understand what each included company or ETF represents. | ![screenshot](documentation/dashboard/stock_asset_expanders.png) |

---

### Epic - Predictor and Scenario Guidance

This Epic is linked to **Milestone 4**.

This Epic covers the `app_pages/predictor.py` page, which separates short-term machine learning output from long-term historical scenario ranges.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a beginner investor | I want a clear Predictor introduction and hero image | so I understand the purpose of the forecasting page. | ![screenshot](documentation/dashboard/predictor_intro_hero.png) |
| As a beginner investor | I want the page to explain short-term ML and long-term scenarios separately | so I understand that they are different types of outputs. | ![screenshot](documentation/dashboard/predictor_explanation.png) |
| As a beginner investor | I want to select an asset | so I can generate outputs for the investment I am interested in. | ![screenshot](documentation/dashboard/predictor_asset_select.png) |
| As a beginner investor | I want to select a forecast horizon | so I can compare different long-term timeframes. | ![screenshot](documentation/dashboard/predictor_horizon.png) |
| As a beginner investor | I want to select a trend window | so I can control how much historical data informs the scenario ranges. | ![screenshot](documentation/dashboard/predictor_window.png) |
| As a beginner investor | I want scenario assumption metrics for the selected asset | so I understand the latest price, date, trend window, and drift used in the scenario calculation. | ![screenshot](documentation/dashboard/predictor_metrics.png) |
| As a beginner investor | I want a separate next-day ML estimate with reproducibility context and plain-English interpretation | so I can understand the short-term model output without confusing it with the long-term scenarios. | ![screenshot](documentation/dashboard/predictor_ml_estimate.png) |
| As a beginner investor | I want a clear ML risk warning | so I understand the next-day estimate is educational and not a trading instruction. | ![screenshot](documentation/dashboard/predictor_ml_warning.png) |
| As a beginner investor | I want a beginner-friendly explanation of short-term prediction uncertainty | so I understand why long-term thinking and scenario planning are more useful than day-to-day prediction. | ![screenshot](documentation/dashboard/predictor_beginner_explanation.png) |
| As a beginner investor | I want pessimistic, realistic, and optimistic scenario end prices | so I understand uncertainty instead of relying on one fixed prediction. | ![screenshot](documentation/dashboard/predictor_scenarios.png) |
| As a beginner investor | I want clear scenario explanations and warnings | so I understand the outputs are educational estimates, not guaranteed outcomes. | ![screenshot](documentation/dashboard/predictor_scenario_warnings.png) |

---

### Epic - Portfolio Plans and Risk Comparison

This Epic is linked to **Milestone 5**.

This Epic covers the `app_pages/portfolio_plans.py` page, which helps users compare risk-based portfolio plans using historical metrics and visualisations.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a beginner investor | I want a clear Portfolio Plans introduction and hero image | so I understand the purpose of the page. | ![screenshot](documentation/dashboard/portfolio_intro_hero.png) |
| As a beginner investor | I want the relative risk labels explained | so I understand that the plans differ by concentration and volatility. | ![screenshot](documentation/dashboard/portfolio_risk_explanation.png) |
| As a beginner investor | I want to select a portfolio plan | so I can explore a specific risk style. | ![screenshot](documentation/dashboard/portfolio_select.png) |
| As a beginner investor | I want the selected plan highlighted | so I know which plan I am currently viewing. | ![screenshot](documentation/dashboard/portfolio_selected_highlight.png) |
| As a beginner investor | I want the four plans displayed visually | so I can compare the plan styles quickly. | ![screenshot](documentation/dashboard/portfolio_plan_boxes.png) |
| As a beginner investor | I want historical performance and risk metrics | so I can compare return, volatility, and drawdown. | ![screenshot](documentation/dashboard/portfolio_metrics.png) |
| As a beginner investor | I want an explanation linking the chart to investing principles | so I understand compounding, staying invested, and diversification. | ![screenshot](documentation/dashboard/portfolio_chart_explanation.png) |
| As a beginner investor | I want a growth of £1 chart | so I can visualise how the selected plan performed historically. | ![screenshot](documentation/dashboard/portfolio_growth_chart.png) |
| As a beginner investor | I want a selected plan allocation table with weight explanations and educational guidance | so I can understand the assets, percentages, and non-recommendation context for the selected plan. | ![screenshot](documentation/dashboard/portfolio_allocation.png) |
| As a beginner investor | I want simple decision guidance if I still feel unsure | so I have a beginner-friendly fallback explanation without receiving personal financial advice. | ![screenshot](documentation/dashboard/portfolio_decision_guidance.png) |
| As a beginner investor | I want an encouraging final message | so I feel confident that I have taken a positive first step in understanding investing. | ![screenshot](documentation/dashboard/portfolio_final_message.png) |

---

### Epic - Model Performance and Transparency

This Epic is linked to **Milestone 5**.

This Epic covers the `app_pages/model_performance.py` page, which presents model performance, evaluation evidence, hyperparameters, plots, feature importance, and educational interpretation.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a technical reviewer | I want a clear Model Performance introduction and hero image | so I understand the purpose of the page. | ![screenshot](documentation/dashboard/model_intro_hero.png) |
| As a technical reviewer | I want the next-day prediction task explained | so I understand what the model is trying to predict. | ![screenshot](documentation/dashboard/model_task_explanation.png) |
| As a technical reviewer | I want the business case result displayed clearly | so I can see whether the model met its success rule. | ![screenshot](documentation/dashboard/model_business_case.png) |
| As a technical reviewer | I want model reproducibility explained | so I understand the displayed result reflects the saved dataset and model artefacts for this project version. | ![screenshot](documentation/dashboard/model_reproducibility.png) |
| As a technical reviewer | I want train and test evaluation metrics displayed | so I can assess model performance. | ![screenshot](documentation/dashboard/model_metrics.png) |
| As a technical reviewer | I want plain-English explanations of R², MAE, and RMSE | so the metrics are understandable in context. | ![screenshot](documentation/dashboard/model_metrics_explained.png) |
| As a technical reviewer | I want the R² success rule explained | so I understand why a small positive signal can still support the business case. | ![screenshot](documentation/dashboard/model_r2_explanation.png) |
| As a technical reviewer | I want the model limitations explained | so I understand why short-term prediction is difficult. | ![screenshot](documentation/dashboard/model_limitations.png) |
| As a technical reviewer | I want the best hyperparameters displayed | so I can inspect the tuned model settings. | ![screenshot](documentation/dashboard/model_hyperparameters.png) |
| As a technical reviewer | I want the full hyperparameter search space displayed | so I can verify that the final model tuning used six hyperparameters with three values each. | ![screenshot](documentation/dashboard/model_search_space.png) |
| As a technical reviewer | I want evaluation plots displayed | so I can visually assess model behaviour and prediction errors. | ![screenshot](documentation/dashboard/model_plots.png) |
| As a technical reviewer | I want EDA plot evidence displayed | so I can connect the dashboard evidence to the project hypotheses around volatility, diversification, and concentration risk. | ![screenshot](documentation/dashboard/model_eda_evidence.png) |
| As a technical reviewer | I want feature importance displayed | so I can see which features influenced the model most. | ![screenshot](documentation/dashboard/model_feature_importance.png) |
| As a technical reviewer | I want a final ML model summary | so I can understand the overall model conclusion. | ![screenshot](documentation/dashboard/model_summary.png) |

---

### Epic - Deployment and Application Availability

This Epic is linked to **Milestone 6**.

This Epic covers deployment configuration, hosted availability, and the steps required to make the finished dashboard publicly accessible on Render.

| Target | Expectation | Outcome | Screenshot |
|---|---|---|---|
| As a user | I want the StockMetrics dashboard deployed online | so I can access the application from a live public URL. | ![screenshot](documentation/deployment/stockmetrics_url.png) |
| As a developer | I want the application deployed using Render | so the dashboard can be reliably hosted and accessed by users. | ![screenshot](documentation/deployment/render_live.png) |

---

### User Story Testing Summary

All dashboard User Stories were manually tested against the deployed Streamlit application.

Each User Story maps directly to a visible dashboard feature, with evidence captured through screenshots. Navigation behaved consistently, interactive widgets updated outputs correctly, visualisations rendered without error, and all educational guidance was displayed as intended.

This provides clear traceability from User Story → Implementation → Validation, satisfying Agile and assessment requirements.

---

## Widget Interaction Testing

Widget interaction testing was carried out by manually checking that each interactive Streamlit widget behaved correctly and updated the dashboard as expected.

This testing focused specifically on user-interactive widgets, including sidebar navigation, link buttons, selectboxes, date inputs, tabs, and expanders.

---

### Widget Interaction Testing Results

| Widget | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| Sidebar navigation radio | Selecting each sidebar page option should load the correct dashboard page | Each page loaded correctly from the sidebar navigation without errors, including Home, Stock Explorer, Predictor, Portfolio Plans, and Model Performance | ![screenshot](documentation/dashboard/routing.png) |
| Footer GitHub link button | Clicking the footer button should provide access to the project repository | The footer button displayed consistently and linked users to the StockMetrics GitHub repository | ![screenshot](documentation/dashboard/footer_button.png) |
| Home page FAQ expanders | Expanding and collapsing FAQ sections should reveal the correct beginner-friendly guidance | FAQ expanders opened and displayed the expected explanations for investing basics, buying and selling, investment frequency, S&P 500, FTSE All-World, Magnificent Seven, Tesla, scenario ranges, Trading 212, and additional assets | ![screenshot](documentation/dashboard/home_faqs.png) |
| Stock Explorer asset selectbox | Selecting a different asset should update the selected asset label, metrics, charts, and asset-specific outputs | Asset-specific metrics and visualisations updated correctly when switching between included ETFs and Magnificent Seven stocks | ![screenshot](documentation/dashboard/stock_explorer_asset_selector.png) |
| Stock Explorer date range input | Changing the start and end dates should filter the displayed data to the selected period | Row count, date range metrics, price chart, returns chart, and distribution chart updated correctly to match the selected date range | ![screenshot](documentation/dashboard/stock_explorer_date_range.png) |
| Stock Explorer chart tabs | Selecting each chart tab should display the correct chart and supporting guidance | The Prices, Returns, and Distribution tabs displayed the expected Plotly charts with relevant educational guidance | ![screenshot](documentation/dashboard/stock_returns_chart.png) |
| Stock Explorer asset guide expanders | Expanding an asset guide item should reveal the correct plain-English company or fund explanation | Asset guide expanders opened correctly for the included stocks and ETFs and displayed the expected beginner-friendly descriptions | ![screenshot](documentation/dashboard/stock_explorer_asset_guide.png) |
| Predictor asset selectbox | Selecting a different asset should update the latest price, latest date, drift, volatility, ML estimate, and scenario table | Predictor outputs refreshed correctly for each selected asset using the relevant historical data and ticker-specific currency formatting | ![screenshot](documentation/dashboard/predictor_asset_selector.png) |
| Predictor forecast horizon selectbox | Changing the forecast horizon should update the long-term scenario output table | Scenario end-price outputs updated correctly when switching between 1, 2, 5, and 10 year horizons | ![screenshot](documentation/dashboard/predictor_horizon_selector.png) |
| Predictor trend window selectbox | Changing the trend window should update the historical assumptions used for the scenario ranges | Trend window used, estimated daily drift, estimated volatility context, and scenario values updated correctly when switching between 1, 2, 5, and 10 year windows | ![screenshot](documentation/dashboard/predictor_trend_window_selector.png) |
| Portfolio Plans selectbox | Selecting a different portfolio plan should update all plan-specific outputs | The selected plan, highlighted plan box, performance metrics, growth chart, and allocation table all updated correctly for each plan | ![screenshot](documentation/dashboard/portfolio_plan_selector.png) |

---

### Widget Interaction Testing Summary

All interactive Streamlit widgets were manually tested and behaved as expected.

Sidebar navigation loaded the correct pages, the footer GitHub link button opened the project repository, FAQ and asset guide expanders displayed the correct content, selectboxes updated dashboard outputs appropriately, date inputs filtered data correctly, and tabs displayed the expected chart views.

No widget-related issues were identified during testing.
