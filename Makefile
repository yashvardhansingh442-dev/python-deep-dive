.DEFAULT_GOAL := help
PYTHON ?= python3
VENV   ?= .venv
BIN    := $(VENV)/bin

.PHONY: help venv install hooks lint format typecheck test test-module cov check \
        bench docs docs-serve progress new-module build clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

## ---- setup ----------------------------------------------------------------

venv:  ## Create the virtual environment
	$(PYTHON) -m venv $(VENV)

install: venv  ## Install the package with dev + docs extras
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev,docs]"

hooks:  ## Install pre-commit hooks
	$(BIN)/pre-commit install

## ---- quality --------------------------------------------------------------

lint:  ## Lint with ruff
	$(BIN)/ruff check .

format:  ## Auto-format and fix lint issues
	$(BIN)/ruff format .
	$(BIN)/ruff check --fix .

typecheck:  ## Strict type-check the reusable package
	$(BIN)/mypy --strict src/

test:  ## Run the full test suite
	$(BIN)/pytest

test-module:  ## Test one curriculum module, e.g. make test-module M=06
	@test -n "$(M)" || (echo "usage: make test-module M=06" && exit 1)
	$(BIN)/pytest tests/curriculum/test_$(M)_*.py -v

cov:  ## Tests with coverage report (fails under 85%)
	$(BIN)/pytest --cov=src/pydeep --cov-report=term-missing --cov-fail-under=85

check: lint typecheck test  ## Everything CI runs

## ---- performance ----------------------------------------------------------

bench:  ## Run all benchmarks and save output to benchmarks/results/
	@mkdir -p benchmarks/results
	@for f in benchmarks/bench_*.py; do \
		echo "== $$f"; \
		$(BIN)/python $$f | tee benchmarks/results/$$(basename $$f .py).txt; \
	done

## ---- docs and progress ----------------------------------------------------

docs:  ## Build the docs site (strict: fails on broken links)
	$(BIN)/mkdocs build --strict

docs-serve:  ## Serve docs locally with live reload
	$(BIN)/mkdocs serve

progress:  ## Regenerate progress tables from topics.yml
	$(BIN)/python scripts/gen_progress.py

new-module:  ## Scaffold a module, e.g. make new-module N=14 NAME=data-science
	@test -n "$(N)" -a -n "$(NAME)" || (echo "usage: make new-module N=14 NAME=data-science" && exit 1)
	$(BIN)/python scripts/new_module.py $(N) $(NAME)

## ---- release / cleanup ----------------------------------------------------

build:  ## Build sdist and wheel
	$(BIN)/pip install --quiet build
	$(BIN)/python -m build

clean:  ## Remove caches and build artifacts
	rm -rf build dist site .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name "*.egg-info" -prune -exec rm -rf {} +
