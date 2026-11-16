.DEFAULT_GOAL := help
PYTHON ?= python3
VENV   ?= .venv
BIN    := $(VENV)/bin

.PHONY: help venv install lint format typecheck test cov check build clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

## ---- setup ----------------------------------------------------------------

venv:  ## Create the virtual environment
	$(PYTHON) -m venv $(VENV)

install: venv  ## Install the package with dev extras
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"

## ---- quality --------------------------------------------------------------

lint:  ## Lint with ruff
	$(BIN)/ruff check .

format:  ## Auto-format and fix lint issues
	$(BIN)/ruff format .
	$(BIN)/ruff check --fix .

typecheck:  ## Strict type-check the reusable package
	$(BIN)/mypy --strict src/

test:  ## Run the test suite
	$(BIN)/pytest

cov:  ## Tests with coverage report (fails under 85%)
	$(BIN)/pytest --cov=src/pydeep --cov-report=term-missing --cov-fail-under=85

check: lint typecheck test  ## Everything CI runs

## ---- release / cleanup ----------------------------------------------------

build:  ## Build sdist and wheel
	$(BIN)/pip install --quiet build
	$(BIN)/python -m build

clean:  ## Remove caches and build artifacts
	rm -rf build dist .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name "*.egg-info" -prune -exec rm -rf {} +
