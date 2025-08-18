# Advent of SQL Solutions

Solutions to [Advent of SQL](https://adventofsql.com/challenges/) using SQLite.

---

## ⚙️ Setup

This project organizes SQL solutions by year and day, with example input data for each challenge.

### Directory Structure

* `solutions/YYYY/DD.sql` – solution SQL files (e.g., `solutions/2024/01.sql`)
* `data/YYYY/advent_of_sql_day_D.sql` – input SQL setup files for each day (e.g., `data/2024/advent_of_sql_day_1.sql`)
* `tests/test_solutions.py` – pytest runner

### Running Solutions Manually

You can run individual solutions in SQLite3 by loading the data and then the solution:

```bash
sqlite3
.read data/2024/01.sql
.read solutions/2024/01.sql
```

---

### Running Tests (Optional)

Pytest is included to automatically verify solutions using sqlite3.

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Run tests:
```bash
uv run pytest
```

* Tests will load the corresponding data SQL, run the solution, and compare the output to the expected result.
* You do not need PostgreSQL; the tests run entirely with SQLite.
