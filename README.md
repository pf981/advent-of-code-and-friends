# Coding Quest Solutions

Solutions to [https://codingquest.io/](https://codingquest.io/)

---

## ⚙️ Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Prerequisites

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

```bash
git clone https://github.com/pf981/coding-quest-solutions.git
cd coding-quest-solutions
uv sync
```


## 🚀 Usage

### Running Solutions

Run individual solutions:
```bash
uv run solutions/01.py
uv run solutions/02.py
# etc.
```

### Running Tests

Run all tests to verify solutions:
```bash
uv run pytest
```

The tests verify that each solution produces the correct answer by comparing SHA256 hashes.
