# Markov Algorithm Online Solutions

Solutions to the [Markov Algorithm Online](https://mao.snuke.org/) puzzles. You must solve puzzles in a language where the only operation is string-replacement.

- Language: Python 3.13
- Package manager: [uv](https://github.com/astral-sh/uv)
- Test runner: [pytest](https://pytest.org)

## 🚀 Quick Start

### Prerequisites
Install uv from https://github.com/astral-sh/uv

### Running Tests

```bash
# Test the correctness of all .mao solution files
uv run pytest
```

## 🏗️ Project Structure

```
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── mao.py                # Runner for .mao files
├── solutions/
├── *.mao                 # Solutions
└── tests/
    ├── conftest.py       # pytest configuration
    └── test_solutions.py # Solution validation tests
```