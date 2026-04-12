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
