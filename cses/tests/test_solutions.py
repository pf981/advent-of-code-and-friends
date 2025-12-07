import pytest
import sys
import subprocess
from pathlib import Path

from _pytest.mark.structures import ParameterSet

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
SOLUTIONS_DIR = PROJECT_ROOT / "solutions"
DATA_DIR = PROJECT_ROOT / "data"


def discover_test_cases() -> list[ParameterSet]:
    test_cases = []

    # Walk through solutions directory
    for solution_file in SOLUTIONS_DIR.rglob("*.py"):
        filename = solution_file.name
        # Match files starting with numbers, e.g. "1068_weird_algorithm.py"
        if not filename[0].isdigit():
            continue

        # Extract problem ID (everything before the first underscore)
        try:
            problem_id = filename.split("_")[0]
        except IndexError:
            continue

        problem_data_dir = DATA_DIR / problem_id

        if not problem_data_dir.exists():
            continue

        # Find all .in files
        for input_file in problem_data_dir.glob("*.in"):
            expected_output_file = input_file.with_suffix(".out")
            if expected_output_file.exists():
                # Provide a nice test ID: problem_id_name-test_number
                # solution_file.stem is "1068_weird_algorithm"
                # input_file.stem is "1" (or "test_1")
                try:
                    test_num = int(input_file.stem)
                    test_suffix = f"{test_num:02d}"
                except ValueError:
                    test_suffix = input_file.stem

                test_id = f"{solution_file.stem}-{test_suffix}"

                test_cases.append(
                    pytest.param(
                        str(solution_file),
                        str(input_file),
                        str(expected_output_file),
                        id=test_id,
                    )
                )

    # Sort by ID for stable order
    return sorted(test_cases, key=lambda x: x.id)


@pytest.mark.parametrize(
    "solution_path, input_path, expected_output_path", discover_test_cases()
)
def test_solution(
    solution_path: str, input_path: str, expected_output_path: str
) -> None:
    # Read input
    with open(input_path, "r") as f:
        input_data = f.read()

    # Read expected output
    with open(expected_output_path, "r") as f:
        expected_output = f.read().strip()

    # Run the solution
    process = subprocess.run(
        [sys.executable, solution_path],
        input=input_data,
        capture_output=True,
        text=True,
        check=True,
    )

    # Verify exact match (stripping trailing whitespace/newlines from both)
    actual_output = process.stdout.strip()

    assert actual_output == expected_output, (
        f"Failed for {solution_path} with input {input_path}.\nExpected: {expected_output}\nActual: {actual_output}"
    )
