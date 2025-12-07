# 🏆 CSES Solutions

Solutions to problems from [CSES.fi](https://cses.fi/), implemented in Python.

## 🚀 Getting Started

This project uses `uv` for dependency management and running scripts.

### 📦 Prerequisites

-   Install `uv`: https://docs.astral.sh/uv/getting-started/installation/
-   Python 3.13+

### 🔧 Installation

```bash
uv sync
```

## 🧪 Running Tests

We use `pytest` to automatically verify solutions against local test data.

```bash
uv run pytest
```

This will:
1.  Discover solution files in `solutions/`.
2.  Look for test data in `data/{problem_id}/`.
3.  **Automatically download** missing test data if your session token is configured.
4.  Run the solution against inputs and compare with outputs.

## 📥 Automatic Test Data Downloader

This project includes a downloader that fetches test cases directly from CSES.

### 🔑 Configuration

To enable downloading, you need to provide your CSES session token (`PHPSESSID`) so the script can access the test data.

1.  **Log in** to [cses.fi](https://cses.fi/login) in your browser.
2.  Open Developer Tools (F12) -> **Application** (or Storage) -> **Cookies**.
3.  Copy the value of the `PHPSESSID` cookie.
4.  Save the token to ~/.config/cses/token

### 🎮 Manual Usage

You can also run the downloader manually for a specific problem:

```bash
uv run utils/downloader.py <problem_id>
```

Example:
```bash
uv run utils/downloader.py 1068
```

## 📂 Project Structure

-   `solutions/` - Python solution files (e.g., `1068_weird_algorithm.py`).
-   `tests/` - Pytest configuration and dynamic test runner.
-   `utils/` - Helper scripts (downloader).
-   `data/` - Downloaded test cases (gitignored).
