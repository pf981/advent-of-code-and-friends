# Python Programming Problems (P3) Solutions
Solutions to [Python Programming Puzzles (P3)](https://github.com/microsoft/PythonProgrammingPuzzles). In these puzzles, you must find an input that makes the given function return `True`.

- Language: Python 3.13
- Package manager: [uv](https://github.com/astral-sh/uv)
- Test runner: [pytest](https://pytest.org)

## 🚀 Quick Start

### Prerequisites

Install uv from https://github.com/astral-sh/uv

### Running Tests

Each test is a puzzle solution. A passing test means you've found an input that satisfies the puzzle's function.

Run all tests:
```bash
uv run pytest
```

Run a specific module:
```bash
uv run pytest tests/test_study.py
```

Run a single puzzle:
```bash
uv run pytest tests/test_study.py::test_study1
```

## 🏗️ Project Structure

```
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── puzzles.json            # Puzzle specifications from PythonProgrammingPuzzles (MIT)
├── generate_puzzles.py     # Utility to regenerate test boilerplate from puzzles.json
├── third_party_licenses/
|   └── PythonProgrammingPuzzles-LICENSE
└── tests/
    └── test_*.py           # Puzzle functions and solutions using pytest
```

## 🧩 Generating Puzzles

`generate_puzzles.py` reads `puzzles.json` and generates one `tests/test_<module>.py` file per
puzzle module, each containing a skipped pytest test stub per puzzle.

> **Note:** This repo contains my solutions. If you want a clean slate to solve the puzzles
> yourself, run:
> ```bash
> uv run python generate_puzzles.py
> ```
> This will overwrite the `tests/` files, replacing all solutions with fresh stubs.

### Generated Code

Each puzzle is generated as a skipped test stub:

```python
from typing import List

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_study1():
    def sat(s: str):
        return s.count("o") == 1000 and s.count("oo") == 0

    assert sat(...)
```

### Solving a Puzzle

To solve a puzzle, remove the `@pytest.mark.skip` decorator and replace the `...` in
`assert sat(...)` with an expression that satisfies the function:

```python
def test_study1():
    def sat(s: str):
        return s.count("o") == 1000 and s.count("oo") == 0

    assert sat("o " * 1000)
```

Then run the tests to verify your solution:

```bash
uv run pytest tests/test_study.py::test_study1
```
