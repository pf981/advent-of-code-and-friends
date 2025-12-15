# 🏆 FlipFlop Solutions

Solutions to problems from [FlipFlop Codes](https://flipflop.slome.org/), implemented in Python.

## ⚙️ Setup

This project uses `uv` to manage the virtual environment and dependencies.

1. Install `uv` from [astral-sh/uv](https://github.com/astral-sh/uv).
2. Sync dependencies:

```bash
uv sync
```

## 🚀 Running Solutions

Download the input file to `input/`. Named as `{puzzle_number}.txt` (e.g., `01.txt`).

Run the solution with
```bash
uv run solutions/01.py
```

## 📂 Project Structure

-   `solutions/` - Python solution files (e.g., `01.py`)
-   `data/` - Input text files (e.g., `01.txt`) (gitignored)
