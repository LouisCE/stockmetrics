# Project Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

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

---

### Jupyter Notebooks

Because Jupyter Notebook (`.ipynb`) files store code, Markdown, metadata, and output in JSON format, they were not validated as raw notebook files like the `.py` files above. Instead, the executable Python code cells were manually copied and pasted into the **PEP 8 CI Python Linter** for validation.

For notebook validation, only the **Python code cells** were checked. Markdown cells and notebook metadata were excluded because they are documentation rather than executable Python code.

---

#### Notebook Validation Approach

Each notebook was reviewed by validating its Python code cells separately. This ensured that the executable notebook code was checked for PEP 8 issues without treating notebook metadata or Markdown content as Python.

For validation purposes, notebook Python code cells were pasted into the PEP 8 CI linter as a single script. A short notebook title comment was included at the top of each pasted validation input only to make the validation screenshots easier to identify; this was not added to the real notebook code cells because each notebook already includes its title in the opening Markdown section.

Where necessary, imports were grouped at the top of the pasted validation input to satisfy linter expectations without changing the actual notebook logic, execution order, or saved outputs.
