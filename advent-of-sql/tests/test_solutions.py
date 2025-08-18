import sqlite3
import pathlib
import pytest
import re


def pg_to_sqlite(sql: str) -> str:
    """Naive translator to make Postgres SQL work on SQLite."""

    # DROP TABLE ... CASCADE → DROP TABLE IF EXISTS ...
    sql = re.sub(
        r"DROP TABLE IF EXISTS (\w+) CASCADE;", r"DROP TABLE IF EXISTS \1;", sql
    )

    return sql


@pytest.fixture
def run_sql():
    """Fixture to run a data + solution SQL and return the query result."""

    def _runner(year: int, day: int, expected: list[tuple]):
        db = sqlite3.connect(":memory:")
        cursor = db.cursor()

        data_file = pathlib.Path(f"data/{year}/advent_of_sql_day_{day}.sql")
        setup_sql = pg_to_sqlite(data_file.read_text())
        cursor.executescript(setup_sql)

        solution_file = pathlib.Path(f"solutions/{year}/{day:02}.sql")
        solution_sql = solution_file.read_text()
        cursor.execute(solution_sql)
        result = cursor.fetchall()

        result_str = "\n".join(",".join(str(col) for col in row) for row in result)

        assert result_str == expected, f"Expected {expected}, got {result_str}"

        db.close()

    return _runner


test_cases = [
    (
        2024,
        1,
        """Abagail,Building sets,LEGO blocks,Blue,1,Complex Gift,Learning Workshop
Abbey,Barbie dolls,Play-Doh,Purple,1,Moderate Gift,General Workshop
Abbey,Stuffed animals,Teddy bears,White,4,Complex Gift,General Workshop
Abbey,Toy trains,Toy trains,Pink,2,Complex Gift,General Workshop
Abbey,Yo-yos,Building blocks,Blue,5,Simple Gift,General Workshop""",
    ),
    (
        2024,
        2,
        "Dear Santa, I hope this letter finds you well in the North Pole! I want a SQL course for Christmas!",
    ),
    (2024, 14, "2024-12-22"),
]


@pytest.mark.parametrize("year,day,expected", test_cases)
def test_solution(run_sql, year, day, expected):
    run_sql(year, day, expected)
