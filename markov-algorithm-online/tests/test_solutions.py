import pathlib
import random
import re
import typing

import pytest

import mao

SOLUTIONS_DIR = pathlib.Path("solutions")


def make_runner(code: str) -> typing.Callable[[str], str]:
    try:
        rules = mao.parse(code)
    except Exception as e:
        pytest.fail(f"Failed to parse code: {e}")

    class RunResult(str):
        input_str: str

        def __new__(cls, value: str, input_str: str):
            obj = super().__new__(cls, value)
            obj.input_str = input_str
            return obj

        def __repr__(self):
            return f"<output={super().__repr__()} for input={self.input_str!r}>"

    def run(input_: str) -> str:
        try:
            result = mao.run(input_, rules)
        except Exception as e:
            pytest.fail(f"Failed to run: {e}")
        return RunResult(result, input_)

    return run


@pytest.fixture
def r(request: pytest.FixtureRequest) -> typing.Callable[[str], str]:
    """Auto runner fixture - short name for convenience"""
    test_name = request.node.name
    match = re.search(r"test_solution(\d+)", test_name)

    if not match:
        pytest.fail(f"Could not extract solution number from test name: {test_name}")

    assert match
    solution_number = int(match.group(1))
    solution_file = SOLUTIONS_DIR / f"{solution_number:>03}.mao"

    if not solution_file.exists():
        pytest.fail(f"Solution file {solution_file} does not exist")

    with open(solution_file, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        run = make_runner(code)
    except Exception as e:
        pytest.fail(f"Failed to build runner from {solution_file}: {e}")

    return run


def test_solution001(r):
    assert r("Hello,") == "World!"


def test_solution002(r):
    assert r("sample_Ss") == "ample_S"


def test_solution003(r):
    assert r("uzuki") == "suzuki"


def test_solution004(r):
    assert r("R") == "P"
    assert r("P") == "S"
    assert r("S") == "R"


def test_solution005(r):
    assert r("iii") == "iwiwi"


def test_solution006(r):
    assert r("BCABBA") == "AABBBC"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("ABC", k=length))
        rhs = "".join(sorted(lhs))
        assert r(lhs) == rhs


def test_solution007(r):
    assert r("ooooo") == "odd"

    for _ in range(100):
        length = random.randint(1, 20)
        lhs = "o" * length
        rhs = "odd" if length % 2 else "even"
        assert r(lhs) == rhs
