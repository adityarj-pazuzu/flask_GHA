# Simple Flask Hello World Application

This is a basic "Hello World" Flask application used to demonstrate the integration of DevOps tools including:

- **Pre-commit hooks** for automatic code quality checks.
- **Pylint** for Python linting.
- **Pytest** for running tests.
- **GitHub Actions** for Continuous Integration (CI) automation.

The main goal of this project is to understand how to integrate pre-commit, pylint, pytest, and GitHub Actions into your development workflow.


## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/adityarj-pazuzu/flask_GHA.git
cd flask_GHA
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

# On Windows use
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install pre-commit hooks and run
```bash
pre-commit install
pre-commit run --show-diff-on-failure --color=always --all-files
```

### 5. Check pylint
```bash
pylint app.py
```

### 6. Run the application
```bash
python app.py
```

### 7. Run the test cases
```bash
pytest
```

## Pre-commit Hooks Configuration
The pre-commit hooks are configured in the `.pre-commit-config.yaml` file. By default, the hooks include checks for:
Python code formatting (via black).



## GitHub Actions
The project is configured with a simple GitHub Actions workflow that runs the following steps:

- Pre-commit: Checks for code formatting and styling issues.
- Pylint: Lints the code to ensure it adheres to coding standards.
- Pytest: Runs the unit tests to verify the application works as expected.

- The workflow file is located at `.github/workflows/python-app.yml`.

GitHub Actions will automatically run these checks when you push code to the repository or create a pull request.
