# Advent of Lmbee Solutions

Solutions to the [Advent of Lmbee](https://lovemathboy.github.io/) puzzles. These are a fan-made (hard) continuation of Advent of Code 2025 for days 13 to 25.

- Language: Python 3.13
- Package manager: [uv](https://github.com/astral-sh/uv)
- Test runner: [pytest](https://pytest.org)

## 🚀 Quick Start

### Prerequisites
Install uv from https://github.com/astral-sh/uv

### Running Tests

Use `pytest` to run all solutions and check output against correct hash:
```bash
uv run pytest
```

Or run an individual solution:
```bash
uv run solutions/13_1.py
```

## 🏗️ Project Structure

```
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   └── *.txt             # Input files
├── solutions/
│   └── *.py              # Solutions
└── tests/
    └── test_solutions.py # Solution validation tests
```
