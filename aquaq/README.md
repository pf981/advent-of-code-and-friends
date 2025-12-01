
# AquaQ Challenge Solutions

This projct contains code (and tests) for solving [AquaQ Challenge](https://challenges.aquaq.co.uk/) questions.

## 🚀 Prerequisites & Setup

This project uses uv to manage the virtual environment and dependencies.

Install uv from https://github.com/astral-sh/uv

```bash
uv sync
````

## Input files

Before running any solution or tests, **download the puzzle input files** and place them under `input/`.

```
input/
  ├── 0.txt
  ├── 1.txt
  ├── ...
  ├── 40.txt
  ├── asciialphabet.txt
  └── words.txt
```

## 🧪 Running Tests

To run all tests with pytest, use:

```bash
uv run pytest
```

## 📁 Project structure

```
aquaq/
├── input/           # — where to put input files (download manually)
├── solutions/       # — python source code
├── tests/           # — pytest test files
└── pyproject.toml   # — project config
```


