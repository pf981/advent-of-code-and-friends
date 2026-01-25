# Eldarverse Solutions

Solutions to the [Eldarverse](https://www.eldarverse.com/) puzzles.

- Language: Python 3.14
- Package manager: [uv](https://github.com/astral-sh/uv)

## 🚀 Quick Start

### Prerequisites
Install uv from https://github.com/astral-sh/uv

### Running Solution

To run a solution, download the input file (e.g. `problem-decryption-contest-1-A-input.txt`) and place it in the `input/` folder.

Then run the corresponding python script using `uv`.

```bash
uv run solutions/decryption-contest-1/A.py
```

## 🏗️ Project Structure

```
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── solutions/
│   ├── decryption-contest-1/
│   │   ├── A.py
│   │   ├── B.py
│   │   ├── C.py
│   │   └── D.py
│   └── */
│       └── *.py
├── input/
│   └── *.txt             # Input files (gitignored) - need to be downloaded
└── output/
    └── *.txt             # Output files (gitignored)
```
