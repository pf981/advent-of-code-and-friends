import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://mao.snuke.org"
SOLUTIONS_DIR = Path("solutions")
TEST_FILE = Path("tests/test_solutions.py")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_next_id(skip: tuple[int] = (21,)) -> int:
    """Finds the first missing ID based on files in solutions/."""
    if not SOLUTIONS_DIR.exists():
        SOLUTIONS_DIR.mkdir()
        return 1

    existing_ids = set(skip)
    for f in SOLUTIONS_DIR.glob("*.mao"):
        match = re.match(r"^(\d+)", f.stem)
        if match:
            existing_ids.add(int(match.group(1)))

    if not existing_ids:
        return 1

    i = 1
    while i in existing_ids:
        i += 1
    return i


def fetch_input_output(problem_id: int) -> tuple[str, str]:
    """Extracts #input_0 and #output_0 value from problem page"""
    print(f"Fetching data for Problem #{problem_id}...")

    r = requests.get(f"{BASE_URL}/tasks/{problem_id}", headers=HEADERS)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    ex_in = soup.find("input", {"id": "input_0"})["value"]
    ex_out = soup.find("input", {"id": "output_0"})["value"]

    return ex_in, ex_out


def main():
    if len(sys.argv) > 1:
        target_id = int(sys.argv[1])
    else:
        target_id = get_next_id()

    try:
        ex_in, ex_out = fetch_input_output(target_id)
        id_str = f"{target_id:03d}"

        sol_file = SOLUTIONS_DIR / f"{id_str}.mao"
        if not sol_file.exists():
            boilerplate = ""
            sol_file.write_text(boilerplate)
            print(f"Created solution: {sol_file}")
        else:
            print(f"Solution {sol_file} already exists.")

        with TEST_FILE.open("a") as f:
            f.write(
                f'\n\ndef test_solution{id_str}(r):\n    assert r("{ex_in}") == "{ex_out}"\n'
            )
        print(f"Added test case to {TEST_FILE}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
