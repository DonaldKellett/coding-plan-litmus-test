# coding-plan-litmus-test

Litmus test for your AI coding plan

## How to use this project

Purchase a coding plan or deploy your AI agent locally, then hook it to your harness and drop it to this codebase. Ask the agent to figure out why our program isn't working and fix it.

If it can't find and fix the issue independently then you got ripped off!

Conversely, if you can't find and fix the issue independently without AI then forget about vibe coding and go do something more productive ;-\)

## Dependencies

1. Python 3.14
1. [mypy](https://www.mypy-lang.org/) 1.20.1
1. [pytest](https://docs.pytest.org/en/stable/) 9.0.3
1. [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) 7.1.0

## Quick start

Isolate your dependencies in a [virtual environment](https://docs.python.org/3/library/venv.html). We recommend using a Python version manager such as [pymanager](https://github.com/python/pymanager), [pyenv](https://github.com/pyenv/pyenv) or [uv](https://github.com/astral-sh/uv).

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the program

The program displays a hello world message.

```bash
python main.py
```

### Type-checking

```bash
mypy .
```

### Quality assurance

Ensure unit tests pass and the coverage is at least 80%.

```bash
pytest -v --cov=. --cov-fail-under=80
```

## Continuous Integration

All the checkmarks are green but the program does not work. Why?

## License

[Apache 2.0](./LICENSE)
