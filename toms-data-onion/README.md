# Tom's Data Onion Solutions

Solutions for [Tom's Data Onion](https://www.tomdalling.com/toms-data-onion/) - "A Programming Puzzle In A Text File".

## ⚙️ Setup

This project uses `uv` to manage the virtual environment and dependencies.

1. Install `uv` from [astral-sh/uv](https://github.com/astral-sh/uv).
2. Sync dependencies:

```bash
uv sync
```

## 📁 Project Structure

*   `data/` - Contains the puzzle input files (layers) as text files (e.g. `00.txt`).
*   `main.py` - The main Python script that solves the layers.

## 🚀 How to Run

To run the solution script using `uv`:

```bash
uv run main.py
```

This will process the available layers in the `data/` directory and output the decrypted next layers.
