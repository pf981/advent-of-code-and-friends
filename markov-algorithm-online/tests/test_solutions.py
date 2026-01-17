import collections
import functools
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

    rules = None

    def run(
        input_: str,
        code_length_limit: int = 1000,
        step_limit: int = 50000,
        string_length_limit: int = 1000,
    ) -> str:
        nonlocal rules
        if rules is None:
            try:
                rules = mao.parse(code, code_length_limit)
            except Exception as e:
                pytest.fail(f"Failed to parse code: {e}")

        try:
            result, steps = mao.run(input_, rules, step_limit, string_length_limit)
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
        pytest.skip(f"Solution file {solution_file} does not exist")

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
    random.seed(0)
    assert r("oooooooooooooooo") == "16"

    for _ in range(10):
        length = random.randint(1, 123)
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
    random.seed(0)
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


def test_solution032(r):
    assert r("ooooo") == "2"

    for num in range(1, 32 + 1):
        lhs = "o" * num
        rhs = str(math.floor(math.log2(num)))
        assert r(lhs) == rhs


def test_solution033(r):
    random.seed(0)
    assert r("oooooo|ooooooooooooooo") == "ooo"

    for _ in range(20):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        lhs = f"{'o' * a}|{'o' * b}"
        rhs = "o" * math.gcd(a, b)
        assert r(lhs) == rhs


def test_solution034(r):
    assert r("ooo*oooo") == "oooooooooooo"

    for a in range(1, 10 + 1):
        for b in range(1, 10 + 1):
            lhs = f"{'o' * a}*{'o' * b}"
            rhs = "o" * (a * b)
            assert r(lhs) == rhs


def test_solution035(r):
    assert r("oooo") == "ooxo"

    for length in range(3, 10 + 1):
        lhs = "o" * length
        rhs = "oox" + ("o" * (length - 3))
        assert r(lhs) == rhs


def test_solution036(r):
    assert r("oooooo") == "oooxoo"

    for length in range(3, 10 + 1):
        lhs = "o" * length
        rhs = ("o" * (length - 3)) + "xoo"
        assert r(lhs) == rhs


def test_solution037(r):
    random.seed(0)
    assert r("ma??o?") == "markov"

    rhs = "markov"
    for _ in range(100):
        lhs = "".join(random.choice([ch, "?"]) for ch in rhs)
        assert r(lhs) == rhs


def test_solution038(r):
    random.seed(0)
    assert r("bbobooobobob") == "ooo"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("bo", k=length))
        bob_count = sum(
            a + b + c == "bob" for a, b, c in zip(lhs[:-2], lhs[1:-1], lhs[2:])
        )
        rhs = "o" * bob_count
        assert r(lhs) == rhs


def test_solution039(r):
    random.seed(0)
    assert r("1ll1l1") == "1oloolooo1oooolooooo1"

    for _ in range(100):
        length = random.randint(1, 6)
        lhs = "".join(random.choices("1l", k=length))
        rhs = "".join(("o" * i) + ch for i, ch in enumerate(lhs))
        assert r(lhs) == rhs


def test_solution040(r):
    random.seed(0)
    assert r("1ll1l1") == "1oooooloooolooo1oolo1"

    for _ in range(100):
        length = 6
        lhs = "".join(random.choices("1l", k=length))
        rhs = "".join(ch + ("o" * (5 - i)) for i, ch in enumerate(lhs))
        assert r(lhs) == rhs


def test_solution041(r):
    assert r("PSP") == "1"

    wins = {"R": "S", "P": "R", "S": "P"}
    loses = {v: k for k, v in wins.items()}

    for comb in itertools.product("RPS", repeat=3):
        lhs = "".join(comb)
        winners = sum(wins[c] in lhs and loses[c] not in lhs for c in lhs)
        rhs = str(winners)
        assert r(lhs) == rhs


def test_solution042(r):
    r = functools.partial(r, step_limit=420)
    random.seed(0)
    assert r("0010110") == "0000111"

    for _ in range(10):
        length = random.randint(1, 200)
        lhs = "".join(random.choices("01", k=length))
        rhs = "".join(sorted(lhs))
        assert r(lhs) == rhs


def test_solution043(r):
    assert r("ooooooooo") == "ooo"

    for num in range(1, 14 + 1):
        lhs = "o" * (num * num)
        rhs = "o" * num
        assert r(lhs) == rhs


def test_solution044(r):
    assert r("oooooooo") == "oooo|oooo"

    for half_length in range(1, 15 + 1):
        half = "o" * half_length
        lhs = f"{half}{half}"
        rhs = f"{half}|{half}"
        assert r(lhs) == rhs


def test_solution045(r):
    assert r("-45") == "45"

    for num in range(100 + 1):
        lhs = rhs = str(num)
        assert r(lhs) == rhs

        lhs = str(-num)
        assert r(lhs) == rhs


def test_solution046(r):
    random.seed(0)
    assert r("01011") == "1"

    for _ in range(100):
        lhs = "".join(random.choices("01", k=5))
        rhs = lhs[3]
        assert r(lhs) == rhs


def test_solution047(r):
    random.seed(0)
    assert r("132968") == "yes"

    upper = 10**15 - 1

    for _ in range(100):
        num = random.randint(0, upper)
        lhs = str(num)
        rhs = "no" if num % 11 else "yes"
        assert r(lhs) == rhs

    for _ in range(100):
        num = 11 * random.randint(0, upper // 1)
        lhs = str(num)
        rhs = "yes"
        assert r(lhs) == rhs


def test_solution048(r):
    assert r("oooooooooooooooo") == "oofobfoofbofoozo"

    for num in range(1, 100 + 1):
        lhs = "o" * num
        rhs = "".join(
            {(True, False): "f", (False, True): "b", (True, True): "z"}.get(
                (i % 3 == 0, i % 5 == 0), "o"
            )
            for i in range(1, num + 1)
        )
        assert r(lhs) == rhs


def test_solution049(r):
    assert r("bbbb") == "baba"

    for num in range(6 + 1):
        lhs = "b" * (2 * num)
        rhs = "ba" * num
        assert r(lhs) == rhs


def test_solution050(r):
    assert r("aaaa") == "baba"

    for num in range(8 + 1):
        lhs = "a" * (2 * num)
        rhs = "ba" * num
        assert r(lhs) == rhs


def test_solution051(r):
    assert r("abab") == "baba"

    for num in range(10 + 1):
        lhs = "ab" * num
        rhs = "ba" * num
        assert r(lhs) == rhs


def test_solution052(r):
    assert r("ooo") == "ooooooo"

    for num in range(1, 9 + 1):
        lhs = "o" * num
        rhs = "o" * (10 - num)
        assert r(lhs) == rhs


def test_solution053(r):
    assert r("oooooooo") == "oooo"

    for num in range(1, 25 + 1):
        lhs = "o" * (2 * num)
        rhs = "o" * num
        assert r(lhs) == rhs


def test_solution054(r):
    random.seed(0)
    assert r("abab?abb") == "<"

    for _ in range(100):
        length1 = random.randint(1, 10)
        length2 = random.randint(1, 10)
        s1 = "".join(random.choices("ab", k=length1))
        s2 = "".join(random.choices("ab", k=length2))
        lhs = f"{s1}?{s2}"
        rhs = "<" if s1 < s2 else ">" if s1 > s2 else "="
        assert r(lhs) == rhs


def test_solution055(r):
    random.seed(0)
    assert r("1523545") == "4"

    for _ in range(100):
        length = random.choice(range(1, 15 + 1, 2))
        lhs = "".join(random.choices("12345", k=length))
        rhs = sorted(lhs)[length // 2]
        assert r(lhs) == rhs


def test_solution056(r):
    random.seed(0)
    assert r("41259687899993") == "7"

    def lis(s: str) -> int:
        smallest = []  # subseq_len -> smallest_last_el
        for num in map(int, s):
            ll = 0
            r = len(smallest) - 1
            i = len(smallest)
            while ll <= r:
                m = (ll + r) // 2
                if smallest[m] >= num:
                    i = m
                    r = m - 1
                else:
                    ll = m + 1

            if i == len(smallest):
                smallest.append(num)
            else:
                smallest[i] = num

        return len(smallest)

    for _ in range(50):
        length = random.randint(1, 27)
        lhs = "".join(random.choices("123456789", k=length))
        rhs = str(lis(lhs))
        assert r(lhs) == rhs


def test_solution057(r):
    assert r("oxoxo|xoxxo|oooox|xxxox|ooxoo") == "BINGO!"
    assert r("oxxxx|xoxxx|xxoxx|xxxox|xxxxo") == "BINGO!", "diagonal TL-BR"
    assert r("xxxxo|xxxox|xxoxx|xoxxx|oxxxx") == "BINGO!", "diagonal TR-BL"
    assert r("ooooo|xxxxx|xxxxx|xxxxx|xxxxx") == "BINGO!", "horizontal bingo"
    assert r("oxxxx|oxxxx|oxxxx|oxxxx|oxxxx") == "BINGO!", "vertical bingo col 1"
    assert r("xxoxx|xxoxx|xxoxx|xxoxx|xxoxx") == "BINGO!", "vertical bingo col 3"
    assert r("ooooo|ooooo|ooooo|ooooo|ooooo") == "BINGO!", "everything bingo"
    assert r("oooox|xxxxx|xxxxx|xxxxx|xxxxx") == ";_;"
    assert r("xxoxo|xoxxo|oooox|xxxox|ooxoo") == ";_;"
