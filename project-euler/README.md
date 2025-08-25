# 🧮 Project Euler – Solutions

This repository contains Python scripts solving problems from [Project Euler](https://projecteuler.net/).

Each solution is implemented in a self-contained script. You can either run a script directly to print its answer, or run the test suite to verify all solutions.

## 📁 Project Structure

* `data/`: Input files required by certain problems (e.g. `0102_triangles.txt`).
* `solutions/`: Python scripts implementing solutions for individual Project Euler problems.
* `tests/`: Pytest-based tests that:

  * Run the corresponding solution script,
  * Compare the computed answer hash to the expected hash.

## 🚀 Getting Started

### Installation

1. **Install uv:**

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository:**

   ```bash
   git clone https://github.com/pf981/advent-of-code-and-friends.git
   cd advent-of-code-and-friends/project-euler
   ```

3. **Install dependencies:**

   ```bash
   uv sync
   ```

## 🧪 Running Solutions

Run an individual problem script directly, for example:

```bash
uv run solutions/001_multiple_of_3_and_5.py
```

This will print the problem’s answer.

## 🧪 Running Tests

Run all test cases with:

```bash
uv run pytest
```

Run tests in parallel on all available CPU cores:

```bash
uv run pytest -n auto -v --durations=0
```

The `--durations=0` flag shows runtimes.
