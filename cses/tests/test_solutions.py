import pytest
import sys
import subprocess
from pathlib import Path
from typing import Any, Callable

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
SOLUTIONS_DIR = PROJECT_ROOT / "solutions"
DATA_DIR = PROJECT_ROOT / "data"


def make_test_function(
    solution_path: str, input_path: str, expected_output_path: str
) -> Callable[[Any], None]:
    """
    Creates a test function that runs the solution against specific input/output.
    """

    def test_func(self: Any) -> None:
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

        actual_output = process.stdout.strip()

        assert actual_output == expected_output, (
            f"Failed for {Path(solution_path).name} with input {Path(input_path).name}.\n"
            f"Expected:\n{expected_output}\n\n"
            f"Actual:\n{actual_output}"
        )

    return test_func


def create_test_class(solution_file: Path, problem_id: str) -> type | None:
    """
    Dynamically create a test class for a specific problem with explicit test methods.
    """
    class_name = f"Test_{solution_file.stem}"

    problem_data_dir = DATA_DIR / problem_id
    if not problem_data_dir.exists():
        return None

    # Collect methods for the class
    class_methods = {}

    found_tests = False

    for input_file in problem_data_dir.glob("*.in"):
        expected_output_file = input_file.with_suffix(".out")
        if expected_output_file.exists():
            found_tests = True
            try:
                test_num = int(input_file.stem)
                test_suffix = f"{test_num:02d}"
            except ValueError:
                test_suffix = input_file.stem

            method_name = f"test_{test_suffix}"

            # Create the test function closure
            test_func = make_test_function(
                str(solution_file), str(input_file), str(expected_output_file)
            )

            # Add to methods dict
            class_methods[method_name] = test_func

    if not found_tests:
        return None

    # Create the class dynamically
    # type(name, bases, dict)
    TestProblem = type(class_name, (), class_methods)

    return TestProblem


# Dynamically generate test classes
for solution_file in SOLUTIONS_DIR.rglob("*.py"):
    filename = solution_file.name
    if not filename[0].isdigit():
        continue

    try:
        problem_id = filename.split("_")[0]
    except IndexError:
        continue

    test_class = create_test_class(solution_file, problem_id)
    if test_class:
        # Inject the class into global namespace so pytest discovers it
        globals()[test_class.__name__] = test_class
