# Marches and Gnats Solutions

Solutions to the [Marches and Gnats](https://mng.quest/) puzzles.

- Language: Python 3.13
- Package manager: [uv](https://github.com/astral-sh/uv)
- Test runner: [pytest](https://pytest.org)

## 🚀 Quick Start

### Prerequisites
Install uv from https://github.com/astral-sh/uv

### Running Tests

```bash
# Convert all .template files to .txt transition rules
uv run template.py solutions/*.template

# Test the correctness of all .txt transition rules
# Also validates output from .py and .template code generators
uv run pytest
```

## 🎨 Code Formatting

The `format.py` script ensures that Logic Mill transition rules are readable by aligning columns and standardizing comment spacing. It overwrites atomically.

### Usage

Format all `.txt` files in the solutions directory:

```bash
uv run format.py solutions/*.txt

```

Format a specific file and preview via stdout the changes without saving:

```bash
uv run format.py solutions/6.txt --preview
```

```
--- Preview for solutions/6.txt ---
INIT         |  INIT         |  R
INIT         -  INIT         -  R
INIT         _  ERASE_LEFT   _  L
ERASE_LEFT   -  HALT         _  L
ERASE_LEFT   |  SEEK_START   _  L
SEEK_START   |  SEEK_START   |  L
SEEK_START   -  SEEK_START   -  L
SEEK_START   _  ERASE_RIGHT  _  R
ERASE_RIGHT  -  HALT         _  R
ERASE_RIGHT  |  INIT         _  R
```


## 📝 Template Language

Some transition rules are more easily expressed using a **template language**. This repository includes a `template.py` script that performs the translation.

### Using the translator

Convert all `.template` files to `.txt`:
```bash
uv run template.py solutions/*.template
```

Convert a specific template:
```bash
uv run template.py solutions/7.template
```

Output to stdout instead of file:
```bash
uv run template.py solutions/7.template --stdout
```

> **Note**: The translator will refuse to overwrite the input file if the output path resolves to the same location.

### 🎯 Language Features

The template language extends the standard transition rules format with three features:

#### 1. Character Classes

Define reusable character sets:

```
digits  = 0123456789
letters = abcdefghijklmnopqrstuvwxyz
```

Reference them using `$name` or `${name}` anywhere - even in state names:

```
// Replace all digits with X and letters with Y
digits = 0123456789
letters = abc

INIT $digits INIT X R
INIT $letters INIT Y R
INIT _ HALT _ R
```

**Expands to:**
```
INIT 0 INIT X R
INIT 1 INIT X R
INIT 2 INIT X R
...
INIT 9 INIT X R
INIT a INIT Y R
INIT b INIT Y R
INIT c INIT Y R
INIT _ HALT _ R
```

#### 2. Capture Groups

When using multiple character classes, they create a **cross-product**. Capture groups (`$1`, `$2`, etc.) let you reference the specific matched characters:

```
// Rotate a string left containing a's, b's, and c's
chars = abc

COPY $chars APPEND_$1 _ R
APPEND_$chars $chars APPEND_$1 $2 R
APPEND_$chars _ HALT $1 R
```

**Expands to:**
```
COPY a APPEND_a _ R
COPY b APPEND_b _ R
COPY c APPEND_c _ R
APPEND_a a APPEND_a a R
APPEND_a b APPEND_a b R
APPEND_a c APPEND_a c R
...
APPEND_c _ HALT c R
```

#### 3. Movement Shortcuts

Common movement patterns are simplified:
- `> STATE CHARACTER` → `STATE CHARACTER STATE CHARACTER R`
- `< STATE CHARACTER` → `STATE CHARACTER STATE CHARACTER L`

```
digits = 0123456789

> SKIP_NUMS $digits
```

**Expands to:**
```
SKIP_NUMS 0 SKIP_NUMS 0 R
SKIP_NUMS 1 SKIP_NUMS 1 R
...
SKIP_NUMS 9 SKIP_NUMS 9 R
```

## 🏗️ Project Structure

```
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
├── logic_mill.py         # Turing machine simulator from mng.quest
├── template.py           # Template language compiler
├── format.py             # Transition rules formatter
├── solutions/
├── *.py                  # Python code generators
├── *.template            # Template source files
└── *.txt                 # Transition rules
└── tests/
    ├── conftest.py       # pytest configuration
    └── test_solutions.py # Solution validation tests
```

## Acknowledgements

Includes `logic_mill.py` from [mng.quest](https://mng.quest/logic_mill.py), licensed under the MIT License.

Template language inspired by [IsaacG](https://github.com/IsaacG/Advent-of-Code/blob/main/mng.quest/solve.py).