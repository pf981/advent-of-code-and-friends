import collections
import itertools
import math
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
        steps: list[str]

        def __new__(cls, value: str, input_str: str, steps: list[str]):
            obj = super().__new__(cls, value)
            obj.input_str = input_str
            obj.steps = steps
            return obj

        def __repr__(self):
            return f"<output={super().__repr__()} for input={self.input_str!r}>"

    def run(input_: str) -> str:
        try:
            result, steps = mao.run(input_, rules)
        except Exception as e:
            pytest.fail(f"Failed to run: {e}")
        return RunResult(result, input_, steps)

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
    random.seed(0)
    assert r("BCABBA") == "AABBBC"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("ABC", k=length))
        rhs = "".join(sorted(lhs))
        assert r(lhs) == rhs


def test_solution007(r):
    random.seed(0)
    assert r("ooooo") == "odd"

    for _ in range(100):
        length = random.randint(1, 20)
        lhs = "o" * length
        rhs = "odd" if length % 2 else "even"
        assert r(lhs) == rhs


def test_solution008(r):
    assert r("bb") == "bbs"


def test_solution009(r):
    random.seed(0)
    assert r("00101") == "11010"

    for _ in range(100):
        length = random.randint(1, 20)
        lhs = "".join(random.choices("01", k=length))
        rhs = "".join("0" if ch == "1" else "1" for ch in lhs)
        assert r(lhs) == rhs


def test_solution010(r):
    random.seed(0)
    assert r("11001") == "11010"
    assert r("1") == "10"

    upper = 2**30
    for _ in range(100):
        num = random.randint(1, upper)
        lhs = f"{num:0b}"
        rhs = f"{num + 1:0b}"
        assert r(lhs) == rhs


def test_solution011(r):
    assert r("oooooooooooooooo") == "16"

    for length in range(1, 123 + 1):
        lhs = "o" * length
        rhs = str(length)
        assert r(lhs) == rhs


def test_solution012(r):
    assert r("16") == "oooooooooooooooo"

    for length in range(1, 200 + 1):
        lhs = str(length)
        rhs = "o" * length
        assert r(lhs) == rhs


def test_solution013(r):
    random.seed(0)
    assert r("00101") == "10100"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("01", k=length))
        rhs = lhs[::-1]
        assert r(lhs) == rhs


def test_solution014(r):
    random.seed(0)
    assert r("00101") == "0010100101"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("01", k=length))
        rhs = lhs + lhs
        assert r(lhs) == rhs


def test_solution015(r):
    random.seed(0)
    assert r("1001") == "yes"

    for _ in range(100):
        length = random.randint(1, 15)
        left = "".join(random.choices("01", k=math.ceil(length / 2)))
        right = left[::-1][length % 2 :]
        lhs = left + right
        assert r(lhs) == "yes"


def test_solution016(r):
    assert r("ooooooo") == "ooooo"

    for length in range(1, 15 + 1):
        lhs = "o" * length
        rhs = "o" * min(length, 5)
        assert r(lhs) == rhs


def test_solution017(r):
    assert r("oo") == "ooooo"

    for length in range(1, 15 + 1):
        lhs = "o" * length
        rhs = "o" * max(length, 5)
        assert r(lhs) == rhs


def test_solution018(r):
    random.seed(0)
    assert r("xoxoo") == "win"

    for _ in range(100):
        length = random.randint(1, 50)
        lhs = "".join(random.choices("xo", k=length))

        o_count = lhs.count("o")
        x_count = length - o_count

        if o_count > x_count:
            rhs = "win"
        elif o_count < x_count:
            rhs = "lose"
        else:
            rhs = "draw"

        assert r(lhs) == rhs


def test_solution019(r):
    assert r("31425") == "12345"

    for perm in itertools.permutations("12345"):
        lhs = "".join(perm)
        assert r(lhs) == "12345"


def test_solution020(r):
    random.seed(0)
    assert r("3141592") == "3.1.4.1.5.9.2"

    for _ in range(100):
        length = random.randint(2, 50)
        lhs = "".join(random.choices("1234567890", k=length))
        rhs = ".".join(lhs)
        assert r(lhs) == rhs


# 021 doesn't exist


def test_solution022(r):
    random.seed(0)
    assert r("abbacbc") == "b"

    for _ in range(100):
        length = random.randint(2, 16)
        rhs = random.choice("abc")
        lhs = list(random.choices("abc", k=length))

        # Very inefficient but good enough
        counts = collections.Counter(lhs)
        while counts[rhs] <= max(
            (count for ch, count in counts.items() if ch != rhs), default=0
        ):
            lhs[random.randint(0, length - 1)] = rhs
            counts = collections.Counter(lhs)

        lhs = "".join(lhs)
        assert r(lhs) == rhs


def test_solution023(r):
    random.seed(0)
    assert r("01210") == "1"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("012", k=length))
        rhs = str(sum(int(ch) for ch in lhs) % 3)
        assert r(lhs) == rhs


def test_solution024(r):
    random.seed(0)
    assert r("554323325") == "2"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("12345", k=length))
        rhs = min(lhs)
        assert r(lhs) == rhs


def test_solution025(r):
    assert r("(()(()()))()") == "yes"
    assert r("()") == "yes"
    assert r("()()") == "yes"
    assert r("(())()") == "yes"
    assert r(")") == "no"
    assert r("(") == "no"
    assert r(")(") == "no"
    assert r("()(()") == "no"


def test_solution026(r):
    assert r("01101000") == "0110|1000"

    for _ in range(100):
        half = random.randint(1, 8)
        lhs = "".join(random.choices("01", k=2 * half))
        rhs = f"{lhs[:half]}|{lhs[half:]}"
        assert r(lhs) == rhs


def test_solution027(r):
    assert r("2513") == "4"

    for perm in itertools.permutations("1234"):
        lhs = "".join(perm)
        assert r(lhs) == "5"

        for rhs in "1234":
            assert r(lhs.replace(rhs, "5")) == rhs


def test_solution028(r):
    assert r("5+9") == "14"

    for a in range(1, 9 + 1):
        for b in range(1, 9 + 1):
            lhs = f"{a}+{b}"
            rhs = f"{a + b}"
            assert r(lhs) == rhs


def test_solution029(r):
    random.seed(0)
    assert r("101110+110001") == "1011111"

    for _ in range(100):
        a = random.randint(1, 63)
        b = random.randint(1, 63)
        lhs = f"{a:b}+{b:b}"
        rhs = f"{a + b:b}"
        assert r(lhs) == rhs


def test_solution030(r):
    random.seed(0)
    assert r("10110+1011101") == "1110011"

    for _ in range(100):
        a = random.randint(1, 777)
        b = random.randint(1, 777)
        lhs = f"{a:b}+{b:b}"
        rhs = f"{a + b:b}"
        assert r(lhs) == rhs

    a = b = 777
    lhs = f"{a:b}+{b:b}"
    rhs = f"{a + b:b}"
    assert r(lhs) == rhs


def test_solution031(r):
    random.seed(0)
    assert r("10110+1011101") == "1110011"

    for _ in range(100):
        a = random.randint(1, 65535)
        b = random.randint(1, 65535)
        lhs = f"{a:b}+{b:b}"
        rhs = f"{a + b:b}"
        assert r(lhs) == rhs

    a = b = 65535
    lhs = f"{a:b}+{b:b}"
    rhs = f"{a + b:b}"
    assert r(lhs) == rhs
