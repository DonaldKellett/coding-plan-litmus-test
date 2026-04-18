# AGENTS.md

## Commands

- Install dependencies: `pip install -r requirements.txt`
- Run program: `python main.py`
- Type check: `mypy .`
- Run tests with coverage: `pytest -v --cov=. --cov-fail-under=80`

The program displays a hello world message to the screen.

## Key files

- `main.py`: Entry point
- `common.py`: Contains greet function
- `test_common.py`: Unit tests

## Requirements

- Python 3.14
- mypy 1.20.1
- pytest 9.0.3
- pytest-cov 7.1.0

## Non-Negotiable Terms

1. **NEVER** edit the unit tests directly, i.e. files with name of form `test_*.py`! Tests must be defined solely by human operators
1. **NEVER** perform Git operations directly! Git operations must be invoked solely by human operators
1. **ALWAYS** run `mypy .` to ensure the codebase type-checks after a change
1. **ALWAYS** run `pytest -v --cov=. --cov-fail-under=80` to ensure unit tests pass with at least 80% codebase coverage after a change
