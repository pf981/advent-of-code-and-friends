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
├── add_problem.py        # Utility to fetch problems and generate tests
├── mao.py                # Runner for .mao files
├── solutions/
│   └── *.mao             # Solutions
└── tests/
    ├── conftest.py       # pytest configuration
    └── test_solutions.py # Solution validation tests
```

## 🛠️ Adding New Problems

The project includes a helper script, `add_problem.py`, to streamline the setup of new puzzles. It scrapes the [MAO website](https://mao.snuke.org/) for example cases and generates the necessary files automatically.

The script performs the following actions:

* **Creates Solution:** Generates a new, empty solution file (e.g., `solutions/015.mao`).
* **Generates Tests:** Appends a corresponding test case to `tests/test_solutions.py`, allowing you to immediately verify your solution against the example data using `pytest`.

Run the script without arguments to find the first missing ID in the `solutions/` directory and fetch that problem.

```bash
uv run add_problem.py
```

Or provide a specific integer ID as an argument (e.g., to setup problem #15).

```bash
uv run add_problem.py 15
```
