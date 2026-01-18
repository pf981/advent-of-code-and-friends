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
    assert r("1" * 200) == "1" * 200

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
    assert r("oxoxo|xoxxo|oooox|xxxox|ooxoo") == "BINGO!", "diagonal TL-BR"
    assert r("xxxxo|xxxox|xxoxx|xoxxx|oxxxx") == "BINGO!", "diagonal TR-BL"
    assert r("ooooo|xxxxx|xxxxx|xxxxx|xxxxx") == "BINGO!", "horizontal bingo"
    assert r("oxxxx|oxxxx|oxxxx|oxxxx|oxxxx") == "BINGO!", "vertical bingo"
    assert r("xxoxo|xoxxo|oooox|xxxox|ooxoo") == ";_;"


def test_solution058(r):
    assert r("27182818284590452353") == "01122223344555788889"

    for _ in range(50):
        length = random.randint(1, 27)
        lhs = "".join(random.choices("0123456789", k=length)).lstrip("0")
        rhs = "".join(sorted(lhs))
        assert r(lhs) == rhs


def test_solution059(r):
    assert r("000n000n") == "00n00n00n"

    for nrows in range(1, 7 + 1):
        for ncols in range(1, 7 + 1):
            lhs = "n".join("0" * ncols for _ in range(nrows)) + "n"
            rhs = "n".join("0" * nrows for _ in range(ncols)) + "n"
            assert r(lhs) == rhs


def test_solution060(r):
    random.seed(0)
    assert r("101011n111110n110010n") == "111n011n110n010n111n100n"

    for _ in range(20):
        nrows = random.randint(1, 7)
        ncols = random.randint(1, 7)
        lhs = (
            "n".join("".join(random.choices("01", k=ncols)) for _ in range(nrows)) + "n"
        )

        rhs = "n".join("".join(row) for row in zip(*lhs[:-1].split("n"))) + "n"
        assert r(lhs) == rhs


def test_solution061(r):
    assert r(":(") == "(:"


def test_solution062(r):
    assert r("22:00:00") == "22:00:01"


def test_solution063(r):
    assert r("") == " "


def test_solution064(r):
    random.seed(0)
    assert r("a b c b c") == "abcbc"

    for _ in range(100):
        n = random.randint(2, 5)
        lhs = " ".join(random.choices("abc", k=n))
        rhs = lhs.replace(" ", "")
        assert r(lhs) == rhs


def test_solution065(r):
    random.seed(0)
    assert r("abcdd") == "a b c d d"

    for _ in range(100):
        n = random.randint(2, 5)
        lhs = "".join(random.choices("abcd", k=n))
        rhs = " ".join(lhs)
        assert r(lhs) == rhs


def test_solution066(r):
    assert r("|   |") == "|  |"

    for n in range(1, 10 + 1):
        lhs = f"|{' ' * n}|"
        rhs = lhs.replace(" ", "", 1)
        assert r(lhs) == rhs


def test_solution067(r):
    random.seed(0)
    assert (
        r("reco?ered:r?c?v?r?d:?????????:recovered")
        == "recovered:recovered:recovered:recovered"
    )

    for _ in range(20):
        n_words = random.randint(1, 199 // 10)
        words = []
        for _ in range(n_words):
            n_holes = random.randint(0, 9)
            hole_positions = random.sample(range(9), k=n_holes)
            word = "".join(
                "?" if i in hole_positions else ch for i, ch in enumerate("recovered")
            )
            words.append(word)

        lhs = ":".join(words)
        rhs = ":".join(["recovered"] * n_words)
        assert r(lhs) == rhs


def test_solution068(r):
    random.seed(0)
    assert r("wiwwiii") == "iwiwiwi"
    assert r("iiiww:wiwwiii:iwi") == "iwiwi:iwiwiwi:iwi"

    for _ in range(50):
        n_words = random.randint(1, 10)
        words = []
        n_chars = 0  # Not counted precisely, but good enough
        for _ in range(n_words):
            n_i = random.randint(1, 10)

            if n_chars + 2 * n_i > 50:
                continue
            n_chars += 2 * n_i

            word = ["i"] * n_i + ["w"] * (n_i - 1)
            random.shuffle(word)

            word = "".join(word)
            words.append(word)

        lhs = ":".join(words)
        rhs = ":".join("iw" * (len(word) // 2) + "i" for word in words)
        assert r(lhs) == rhs


def test_solution069(r):
    assert r("tttttt") == "testtesttest"

    for n in range(2, 15):
        lhs = "t" * 2 * n
        rhs = "test" * n
        assert r(lhs) == rhs


def test_solution070(r):
    random.seed(0)
    assert r("seetssttet") == "testestest"

    # Important test case
    assert r("t") == "t"

    for _ in range(100):
        length = random.randint(1, 15)
        lhs = "".join(random.choices("tes", k=length))
        rhs = (
            "t" + "est" * (length // 3)
            if lhs.count("s") == lhs.count("e") == lhs.count("t") - 1
            else "no"
        )
        assert r(lhs) == rhs

    for _ in range(1, 100):
        n_est = random.randint(1, 4)
        rhs = "t" + ("est" * n_est)
        lhs = "".join(random.sample(rhs, len(rhs)))
        assert r(lhs) == rhs


def test_solution071(r):
    random.seed(0)
    assert r("ooo+oooo-oo=ooooo") == "yes"

    # Not specified, but I'm assuming LHS can't start with "+" or end with an operator
    for _ in range(50):
        n_ops = random.randint(0, 5)
        ops = random.choices("+-", k=n_ops + 1)
        nums = [random.randint(1, 6) for _ in range(n_ops)]

        lhs = ""
        rhs = 0
        for op, num in zip(ops, nums):
            lhs += op + "o" * num
            rhs += (-1 if op == "-" else 1) * num
        lhs.lstrip("+")

        if rhs <= 0:
            continue

        rhs = "o" * rhs

        assert r(f"{lhs}={rhs}") == "yes"
        assert r(f"{lhs}={rhs}o") == "no"
        assert r(f"{lhs}o={rhs}") == "no"


def test_solution072(r):
    random.seed(0)
    assert r("ooooooooo,ooooo,oooooo,ooo") == "ooo"

    for _ in range(50):
        n_words = random.randint(1, 5)
        words = ["o" * random.randint(0, 10) for _ in range(n_words)]
        lhs = ",".join(words)
        rhs = min(words)
        assert r(lhs) == rhs


def test_solution073(r):
    assert r("ooooooo") == "yes"

    for n in range(1, 30 + 1):
        lhs = "o" * n
        rhs = "yes" if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] else "no"
        assert r(lhs) == rhs


def test_solution074(r):
    random.seed(0)
    assert r("oooooo:ooooooooooo:oooo") == "yes:no:yes"

    for _ in range(50):
        n_words = random.randint(1, 12)
        words = ["o" * random.randint(4, 25) for _ in range(n_words)]
        lhs = ":".join(words)
        rhs = ":".join(
            "yes"
            if len(word)
            in [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25]
            else "no"
            for word in words
        )
        assert r(lhs) == rhs


def test_solution075(r):
    random.seed(0)
    assert r("|         |,|  |,|    |,|     |") == "|  |"

    for _ in range(50):
        n_words = random.randint(1, 5)
        words = [f"|{' ' * random.randint(0, 10)}|" for _ in range(n_words)]
        lhs = ",".join(words)
        rhs = max(words)
        assert r(lhs) == rhs


def test_solution076(r):
    assert r("a<b&c>b&b>a") == "c"

    assert r("a>b&a>c") == "a"
    assert r("a>b&a<c") == "c"
    assert r("a>b&b>c") == "a"
    assert r("a>b&c>a") == "c"
    assert r("a>b&c<a") == "a"
    assert r("a>b&c<b") == "a"
    assert r("a<b&a>c") == "b"
    assert r("a<b&b>c") == "b"
    assert r("a<b&b<c") == "c"
    assert r("a<b&c<a") == "b"
    assert r("a<b&c>b") == "c"
    assert r("a<b&c<b") == "b"
    assert r("a>c&b>a") == "b"
    assert r("a>c&b<a") == "a"
    assert r("a>c&b<c") == "a"
    assert r("a>c&c>b") == "a"
    assert r("a<c&b<a") == "c"
    assert r("a<c&b>c") == "b"
    assert r("a<c&b<c") == "c"
    assert r("a<c&c>b") == "c"
    assert r("a<c&c<b") == "b"
    assert r("b>a&b>c") == "b"
    assert r("b>a&b<c") == "c"
    assert r("b>a&c<a") == "b"
    assert r("b>a&c>b") == "c"
    assert r("b>a&c<b") == "b"
    assert r("b<a&b>c") == "a"
    assert r("b<a&c>a") == "c"
    assert r("b<a&c<a") == "a"
    assert r("b<a&c<b") == "a"
    assert r("b>c&c>a") == "b"
    assert r("b<c&c>a") == "c"
    assert r("b<c&c<a") == "a"
    assert r("c>a&c>b") == "c"
    assert r("c>a&c<b") == "b"
    assert r("c<a&c>b") == "a"
    assert r("a>b&a>c&b<a") == "a"
    assert r("a>b&a>c&b>c") == "a"
    assert r("a>b&a>c&b<c") == "a"
    assert r("a>b&a>c&c<a") == "a"
    assert r("a>b&a>c&c>b") == "a"
    assert r("a>b&a>c&c<b") == "a"
    assert r("a>b&a<c&b<a") == "c"
    assert r("a>b&a<c&b<c") == "c"
    assert r("a>b&a<c&c>a") == "c"
    assert r("a>b&a<c&c>b") == "c"
    assert r("a>b&b<a&b>c") == "a"
    assert r("a>b&b<a&c>a") == "c"
    assert r("a>b&b<a&c<a") == "a"
    assert r("a>b&b<a&c<b") == "a"
    assert r("a>b&b>c&c<a") == "a"
    assert r("a>b&b>c&c<b") == "a"
    assert r("a>b&b<c&c>a") == "c"
    assert r("a>b&b<c&c<a") == "a"
    assert r("a>b&c>a&c>b") == "c"
    assert r("a>b&c<a&c>b") == "a"
    assert r("a>b&c<a&c<b") == "a"
    assert r("a<b&a>c&b>a") == "b"
    assert r("a<b&a>c&b>c") == "b"
    assert r("a<b&a>c&c<a") == "b"
    assert r("a<b&a>c&c<b") == "b"
    assert r("a<b&a<c&b>c") == "b"
    assert r("a<b&a<c&b<c") == "c"
    assert r("a<b&a<c&c>b") == "c"
    assert r("a<b&a<c&c<b") == "b"
    assert r("a<b&b>a&b>c") == "b"
    assert r("a<b&b>a&b<c") == "c"
    assert r("a<b&b>a&c<a") == "b"
    assert r("a<b&b>a&c>b") == "c"
    assert r("a<b&b>a&c<b") == "b"
    assert r("a<b&b>c&c>a") == "b"
    assert r("a<b&b>c&c<a") == "b"
    assert r("a<b&b>c&c<b") == "b"
    assert r("a<b&b<c&c>a") == "c"
    assert r("a<b&b<c&c>b") == "c"
    assert r("a<b&c>a&c>b") == "c"
    assert r("a<b&c>a&c<b") == "b"
    assert r("a<b&c<a&c<b") == "b"
    assert r("a>c&b>a&b>c") == "b"
    assert r("a>c&b>a&c<a") == "b"
    assert r("a>c&b>a&c<b") == "b"
    assert r("a>c&b<a&b>c") == "a"
    assert r("a>c&b<a&b<c") == "a"
    assert r("a>c&b<a&c<a") == "a"
    assert r("a>c&b<a&c>b") == "a"
    assert r("a>c&b<a&c<b") == "a"
    assert r("a>c&b<c&c<a") == "a"
    assert r("a>c&b<c&c>b") == "a"
    assert r("a>c&c<a&c>b") == "a"
    assert r("a<c&b>a&b>c") == "b"
    assert r("a<c&b>a&b<c") == "c"
    assert r("a<c&b>a&c>b") == "c"
    assert r("a<c&b>a&c<b") == "b"
    assert r("a<c&b<a&b<c") == "c"
    assert r("a<c&b<a&c>a") == "c"
    assert r("a<c&b<a&c>b") == "c"
    assert r("a<c&b>c&c>a") == "b"
    assert r("a<c&b>c&c<b") == "b"
    assert r("a<c&b<c&c>a") == "c"
    assert r("a<c&b<c&c>b") == "c"
    assert r("a<c&c>a&c>b") == "c"
    assert r("a<c&c>a&c<b") == "b"
    assert r("b>a&b>c&c>a") == "b"
    assert r("b>a&b>c&c<a") == "b"
    assert r("b>a&b>c&c<b") == "b"
    assert r("b>a&b<c&c>a") == "c"
    assert r("b>a&b<c&c>b") == "c"
    assert r("b>a&c>a&c>b") == "c"
    assert r("b>a&c>a&c<b") == "b"
    assert r("b>a&c<a&c<b") == "b"
    assert r("b<a&b>c&c<a") == "a"
    assert r("b<a&b>c&c<b") == "a"
    assert r("b<a&b<c&c>a") == "c"
    assert r("b<a&b<c&c<a") == "a"
    assert r("b<a&c>a&c>b") == "c"
    assert r("b<a&c<a&c>b") == "a"
    assert r("b<a&c<a&c<b") == "a"
    assert r("b>c&c>a&c<b") == "b"
    assert r("b<c&c>a&c>b") == "c"
    assert r("b<c&c<a&c>b") == "a"


def test_solution077(r):
    random.seed(0)
    assert r("ooooo|ooo|oooooo") == "2nd"

    for _ in range(50):
        n_piles = random.randint(2, 10)
        piles = [random.randint(1, 8) for _ in range(n_piles)]
        lhs = "|".join("o" * pile for pile in piles)

        if len(lhs) > 50:
            continue

        xor = 0
        for pile in piles:
            xor ^= pile

        rhs = "1st" if xor else "2nd"
        assert r(lhs) == rhs
