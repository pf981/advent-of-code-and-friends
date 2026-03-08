import importlib
import inspect
import math
import pathlib
import random
import re
import sys
import typing

import pytest

import logic_mill
import template

SOLUTIONS_DIR = pathlib.Path("solutions")


def make_runner(code: str) -> typing.Callable[[str], str]:
    try:
        transition_rules = logic_mill.parse_transition_rules(code)
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

    def run(input: str) -> str:
        try:
            mill = logic_mill.LogicMill(transition_rules, max_states=10_000)
            result, _ = mill.run(input, max_steps=8_000_000)
        except Exception as e:
            pytest.fail(f"Failed to run: {e}")
        return RunResult(result.strip("_"), input)

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
    solution_file = SOLUTIONS_DIR / f"{solution_number}.txt"

    if not solution_file.exists():
        pytest.skip(f"Solution file {solution_file} does not exist")

    with open(solution_file, "r", encoding="utf-8") as f:
        code = f.read()

    try:
        run = make_runner(code)
    except Exception as e:
        pytest.fail(f"Failed to build runner from {solution_file}: {e}")

    return run


@pytest.mark.parametrize(
    "solution_file",
    sorted(SOLUTIONS_DIR.glob("*.py")),
    ids=lambda path: path.as_posix(),
)
def test_codegen(solution_file):
    """
    For each solutions/N.py, run its matching test_solutionN(r).

    Requires each Python file to define a `generate_code()` function.
    """
    if solution_file.stem.endswith("wip"):
        pytest.skip(f"Skipping WIP file: {solution_file!r}")
    if not solution_file.stem.isdigit():
        pytest.fail(
            f"Solution python module, {solution_file!r}, does not have the correct format. Expected '{SOLUTIONS_DIR / '{solution_number}.py'}'. Use '{SOLUTIONS_DIR / '{solution_number}_wip.py'}' for work in progress."
        )
    solution_number = int(solution_file.stem)

    # Find the corresponding test function in this module
    test_func_name = f"test_solution{solution_number}"
    current_module = sys.modules[__name__]
    test_func = getattr(current_module, test_func_name, None)
    if test_func is None:
        pytest.fail(f"No {test_func_name} defined while processing {solution_file}")

    assert test_func

    # Ensure test function takes correct parameters
    sig = inspect.signature(test_func)
    params = list(sig.parameters.keys())
    if params != ["r"]:
        pytest.fail(
            f"Unable to run test for {solution_file} codegen. {test_func_name} "
            f"test function does not have correct parameters. "
            f"Expected only 'r' parameter but signature was {sig}"
        )

    # Load the solution and build runner
    spec = importlib.util.spec_from_file_location(solution_file.stem, solution_file)  # ty:ignore[possibly-missing-attribute]
    module = importlib.util.module_from_spec(spec)  # ty:ignore[possibly-missing-attribute]
    spec.loader.exec_module(module)

    # Ensure generate_code exists, is callable, and has no arguments
    if not hasattr(module, "generate_code"):
        pytest.fail(f"Module {solution_file} does not define generate_code()")

    generate_code = getattr(module, "generate_code")
    if not callable(generate_code):
        pytest.fail(f"generate_code in {solution_file} is not callable")

    gen_sig = inspect.signature(generate_code)
    if len(gen_sig.parameters) != 0:
        pytest.fail(
            f"generate_code in {solution_file} must take no arguments, "
            f"but signature was {gen_sig}"
        )

    code = module.generate_code()
    r = make_runner(code)

    # Run the test
    test_func(r)


@pytest.mark.parametrize(
    "template_file",
    sorted(SOLUTIONS_DIR.glob("*.template")),
    ids=lambda path: path.as_posix(),
)
def test_templates(template_file):
    """
    For each solutions/N.template, translate it to transition rules and run
    its matching test_solutionN(r).
    """
    if not template_file.stem.isdigit():
        pytest.fail(
            f"Template, '{template_file}', does not have correct file name format. Expected '{SOLUTIONS_DIR / '{solution_number}.template'}'"
        )
    solution_number = int(template_file.stem)

    # Find the corresponding test function in this module
    test_func_name = f"test_solution{solution_number}"
    current_module = sys.modules[__name__]
    test_func = getattr(current_module, test_func_name, None)
    if test_func is None:
        pytest.fail(f"No {test_func_name} defined while processing {template_file}")

    assert test_func

    # Ensure test function takes correct parameters
    sig = inspect.signature(test_func)
    params = list(sig.parameters.keys())
    if params != ["r"]:
        pytest.fail(
            f"Unable to run test for {template_file} codegen. {test_func_name} "
            f"test function does not have correct parameters. "
            f"Expected only 'r' parameter but signature was {sig}"
        )

    with open(template_file, "r", encoding="utf-8") as f:
        template_code = f.read()

    code = template.parse(template_code)
    r = make_runner(code)

    # Run the test
    test_func(r)


def tally(num: int) -> str:
    return "|" * num


def test_solution1(r):
    assert r("|||+||||") == "|||||||"
    for lhs in range(1, 10):
        for rhs in range(1, 10):
            input = f"{tally(lhs)}+{tally(rhs)}"
            assert r(input) == tally(lhs + rhs)


def test_solution2(r):
    assert r("|||||||") == "O"
    assert r("||||||") == "E"
    for num in range(1, 10):
        assert r(tally(num)) == "EO"[num % 2], (
            f"Expect {num} is {['even', 'odd'][num % 2]}"
        )


def test_solution3(r):
    assert r("1010") == "1011"
    assert r("0") == "1"
    for num in range(1, 10):
        assert r(f"{num:b}") == f"{num + 1:b}"


def test_solution4(r):
    assert r("||*|||") == "||||||"
    for lhs in range(1, 10):
        for rhs in range(1, 10):
            assert r(f"{tally(lhs)}*{tally(rhs)}") == tally(lhs * rhs)


def test_solution5(r):
    random.seed(0)
    assert r("||:|||,|||||,||||||||,||||") == "|||||"
    for n in range(1, 10):
        nums = [random.randint(1, 10) for _ in range(n)]
        rhs = ",".join(tally(num) for num in nums)
        for i in range(1, n + 1):
            assert r(f"{tally(i)}:{rhs}") == tally(nums[i - 1])


def test_solution6(r):
    assert r("|||||-||") == "|||"
    assert r("||-||") == ""
    for lhs in range(1, 10):
        for rhs in range(1, lhs):
            assert r(f"{tally(lhs)}-{tally(rhs)}") == tally(lhs - rhs)


def test_solution7(r):
    random.seed(0)
    assert (
        r("wõta-wastu-mu-soow-ja-chillitse-toomemäel")
        == "[w]õta-[w]astu-mu-soo[w]-ja-[ch]illitse-toomemäel"
    )
    for n in range(1, 10):
        lhs = "".join(
            random.choice("-abcdefghijklmnopqrstuvwxyzäöõü") for _ in range(n)
        )
        rhs = "".join({"w": "[w]", "ch": "[ch]"}.get(c, c) for c in lhs)
        assert r(lhs) == rhs


def test_solution8(r):
    random.seed(0)
    assert r("hello-world") == "dlrow-olleh"
    for n in range(1, 10):
        lhs = "".join(
            random.choice("-abcdefghijklmnopqrstuvwxyzäöõü") for _ in range(n)
        )
        rhs = lhs[::-1]
        assert r(lhs) == rhs


def test_solution9(r):
    assert r("|||,||||") == "|||<||||"
    assert r("|||,|||") == "|||=|||"
    for lhs in range(1, 10):
        for rhs in range(1, 10):
            if lhs < rhs:
                op = "<"
            elif lhs > rhs:
                op = ">"
            else:
                op = "="
            assert r(f"{tally(lhs)},{tally(rhs)}") == f"{tally(lhs)}{op}{tally(rhs)}"


def test_solution10(r):
    random.seed(0)
    assert r("hello+world+how-are-you") == "|||"
    for n in range(1, 10):
        words = []

        for _ in range(n):
            word_length = random.randint(1, 10)
            word = "".join(
                random.choice("-abcdefghijklmnopqrstuvwxyzäöõü")
                for _ in range(word_length)
            )
            words.append(word)

        lhs = "+".join(words)
        rhs = tally(n)
        assert r(lhs) == rhs


def test_solution11(r):
    assert r("13") == "14"
    for num in range(1, 1000):
        assert r(str(num)) == str(num + 1)


def test_solution12(r):
    random.seed(0)
    assert r("2+5") == "7"

    for _ in range(1000):
        lhs = random.randint(1, 1000)
        rhs = random.randint(1, 1000)
        assert r(f"{lhs}+{rhs}") == str(lhs + rhs)


def test_solution13(r):
    random.seed(0)
    assert r("||,|,|||||,||||||||") == "|,||,|||||,||||||||"

    for _ in range(100):
        n = random.randint(1, 10)
        nums = random.choices(range(1, 10), k=n)

        input_str = ",".join(tally(num) for num in nums)
        expected_output_str = ",".join(tally(num) for num in sorted(nums))
        assert r(input_str) == expected_output_str


def test_solution14(r):
    assert r("1010") == "10"

    for num in range(1000):
        assert r(f"{num:b}") == str(num)


def test_solution15(r):
    assert r("|||||||||") == "|||"

    for num in range(1, 20):
        assert r(tally(num * num)) == tally(num)

    assert r(tally(67 * 67)) == tally(67)
    assert r(tally(80 * 80)) == tally(80)
    assert r(tally(81 * 81)) == tally(81)


def test_solution16(r):
    random.seed(0)
    assert r("IX") == "|||||||||"

    def roman(n: int) -> str:
        values = [
            ("I", 1),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("L", 50),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("D", 500),
            ("CM", 900),
            ("M", 1000),
        ]

        result = ""
        while n:
            while values[-1][1] > n:
                values.pop()
            result += values[-1][0]
            n -= values[-1][1]

        return result

    for num in [
        1,
        4,
        5,
        9,
        10,
        40,
        49,
        50,
        90,
        99,
        100,
        400,
        499,
        500,
        900,
        999,
        1000,
        3999,
    ]:
        assert (r(roman(num))) == tally(num)

    # for num in range(1, 4000):
    for _ in range(100):
        num = random.randint(1, 3999)
        assert (r(roman(num))) == tally(num)


def test_solution17(r):
    random.seed(0)
    assert r("+") == "+++-----+++"

    # Bugged test case which doesn't accept "-----------"
    assert r("-") == ""

    def sim(state: str) -> str:
        for _ in range(5):
            state2 = []
            for i in range(-1, len(state) + 1):
                neighbors = 0
                if i - 1 >= 0 and state[i - 1] == "+":
                    neighbors += 1
                if 0 <= i < len(state) and state[i] == "+":
                    neighbors += 1
                if i + 1 < len(state) and state[i + 1] == "+":
                    neighbors += 1
                state2.append("+" if neighbors == 1 else "-")
            state = "".join(state2)
        return state

    for _ in range(100):
        n = random.randint(1, 100)
        state = "".join(random.choice("+-") for _ in range(n))
        assert r(state).strip("-") == sim(state).strip("-")


def test_solution18(r):
    random.seed(0)
    assert r("||||||÷||||") == "|,||"
    assert r("||||||÷|||") == "||,"
    assert r("|÷|") == "|,"
    assert r(f"{tally(4600)}÷{tally(74)}") == ",".join(
        tally(num) for num in divmod(4600, 74)
    )

    for _ in range(100):
        numerator = random.randint(1, 100)
        denominator = random.randint(1, 100)
        expected = ",".join(tally(num) for num in divmod(numerator, denominator))
        assert r(f"{tally(numerator)}÷{tally(denominator)}") == expected


def test_solution19(r):
    assert (
        r(
            "143|657|028="
            "682|314|579="
            "571|289|346="
            "726|493|851="
            "315|862|497="
            "894|571|263="
            "457|136|982="
            "068|925|734="
            "239|748|615"
        )
        == "N"
    )
    assert (
        r(
            "534|678|912="
            "672|195|348="
            "198|342|567="
            "859|761|423="
            "426|853|791="
            "713|924|856="
            "961|537|284="
            "287|419|635="
            "345|286|119"
        )
        == "N"
    )
    assert (
        r(
            "417|369|852="
            "692|851|493="
            "853|427|196="
            "978|143|265="
            "531|286|947="
            "246|795|318="
            "189|534|627="
            "365|972|481="
            "724|618|539"
        )
        == "N"
    )
    assert (
        r(
            "534|678|912="
            "672|195|348="
            "198|342|567="
            "859|761|423="
            "426|853|791="
            "713|924|856="
            "961|537|284="
            "287|419|635="
            "345|286|179"
        )
        == "Y"
    )
    assert (
        r(
            "295|743|861="
            "836|195|427="
            "471|682|395="
            "168|357|249="
            "357|924|618="
            "924|618|573="
            "589|471|236="
            "612|539|784="
            "743|286|951"
        )
        == "Y"
    )
    assert (
        r(
            "417|369|852="
            "692|851|473="
            "853|427|196="
            "978|143|265="
            "531|286|947="
            "246|795|318="
            "189|534|627="
            "365|972|481="
            "724|618|539"
        )
        == "Y"
    )


def test_solution21(r):
    random.seed(0)
    assert r("|||||||:hello-world-how-are-you") == "hello+world+how-are+you"

    letters = "abcdefghijklmnopqrstuvwxyz"

    for _ in range(50):
        max_word_len = random.randint(1, 10)
        min_words = random.randint(2, 20)
        wrap = random.randint(max_word_len, max_word_len + 15)

        line = ""
        words = []
        rhs = []
        while True:
            word = "".join(random.choices(letters, k=random.randint(1, max_word_len)))
            words.append(word)

            if line:
                next_line = f"{line}-{word}"
                if len(next_line) <= wrap:
                    line = next_line
                else:
                    rhs.append(line)
                    line = word
            else:
                line = word

            if (
                len(words) > min_words
                and sum(len(word) for word in words) + len(words) - 1 > wrap
            ):
                break

        rhs.append(line)

        lhs = f"{tally(wrap)}:{'-'.join(words)}"
        rhs = "+".join(rhs)

        assert r(lhs) == rhs


def test_solution22(r):
    random.seed(0)
    assert r("mdzgstf:thkrg") == "hello"

    letters = "abcdefghijklmnopqrstuvwxyz"

    def decipher(key: str, cipher: str) -> str:
        assert len(key) >= len(cipher)

        result = []
        for k, m in zip(key, cipher):
            result.append(letters[(letters.index(m) - letters.index(k)) % len(letters)])

        return "".join(result)

    assert decipher("mdzgstf", "thkrg") == "hello"

    for _ in range(100):
        message_len = random.randint(1, 30)
        key_len = random.randint(message_len, 40)
        cipher = "".join(random.choices(letters, k=message_len))
        key = "".join(random.choices(letters, k=key_len))

        assert r(f"{key}:{cipher}") == decipher(key, cipher)


def test_solution25(r):
    random.seed(0)
    assert r("vingt-et-un") == "21"

    def int_to_french(n: int) -> str:
        units = [
            "",
            "un",
            "deux",
            "trois",
            "quatre",
            "cinq",
            "six",
            "sept",
            "huit",
            "neuf",
        ]
        teens = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante"]

        def under_hundred(x):
            if x < 10:
                return units[x]
            if 10 <= x <= 16:
                return teens[x - 10]
            if 17 <= x <= 19:
                return "dix-" + units[x - 10]
            if 20 <= x <= 69:
                q, r = divmod(x, 10)
                if r == 1:
                    return tens[q] + "-et-un"
                return tens[q] + "-" + units[r] if r else tens[q]
            if 70 <= x <= 79:
                return under_hundred(60) + "-" + under_hundred(x - 60)
            if 80 <= x <= 99:
                return (
                    "quatre-vingts"
                    if x == 80
                    else "quatre-vingt-" + under_hundred(x - 80)
                )

        def under_thousand(x):
            h, r = divmod(x, 100)
            prefix = "" if h == 0 else ("cent" if h == 1 else units[h] + " cent")
            return (
                prefix
                if r == 0
                else prefix + " " + under_hundred(r)
                if prefix
                else under_hundred(r)
            )

        m, r = divmod(n, 1000)
        prefix = "" if m == 0 else ("mille" if m == 1 else units[m] + " mille")
        if r == 0:
            return prefix
        return prefix + " " + under_thousand(r) if prefix else under_thousand(r)

    for _ in range(100):
        num = random.randint(1, 1100)
        assert r(int_to_french(num)) == str(num)


def test_solution26(r):
    random.seed(0)
    assert r("auatau") == "aut"

    # This is biased but produces reasonable tests
    for _ in range(100):
        target = random.randint(1, 50)
        freqs = []
        total = 0
        while total < target:
            freq = random.randint(1, target - total)
            freqs.append(freq)
            total += freq

        freqs = list(set(freqs))

        letters = random.sample("abcdefghijklmnopqrstuvwxyz", len(freqs))
        lhs = [c for c, freq in zip(letters, freqs) for _ in range(freq)]
        random.shuffle(lhs)

        lhs = "".join(lhs)
        rhs = "".join(sorted(letters, key=lambda c: lhs.count(c), reverse=True))
        assert r(lhs) == rhs


def test_solution27(r):
    random.seed(0)
    assert r("||||/||") == "Y"
    assert r("||||/|||") == "N"

    for _ in range(100):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        assert r(f"{tally(a * b)}/{tally(b)}") == "Y"

    for _ in range(10):
        a = random.randint(1, 10)
        assert r(f"{tally(a)}/{tally(a)}") == "Y"

    for _ in range(100):
        a = random.randint(1, 10)
        b = random.randint(a, 12)
        assert r(f"{tally(a)}/{tally(b)}") == "NY"[a % b == 0]


def test_solution28(r):
    def fib(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    assert r("||||||") == "||||||||"
    for n in range(1, 16):
        assert r(tally(n)) == tally(fib(n))


def test_solution29(r):
    random.seed(0)
    assert r("a@a:c,c:W") == "W"
    assert r("afg@a:W,f:a,g:M") == "WWM"

    for _ in range(50):
        n_parts = random.randint(1, 50)
        freqs = []
        total = 0
        while total < n_parts:
            freq = random.randint(1, n_parts - total)
            freqs.append(freq)
            total += freq

        n_letters = len(freqs)
        letters = random.sample("abcdefghij", n_letters)

        n_edges = random.randint(0, n_letters - 1)
        edge_strs = []
        edges = {}
        for i in range(n_edges):
            a, b = random.sample(range(i, n_letters), 2)
            edges[letters[a]] = letters[b]
            edge_strs.append(f"{letters[a]}:{letters[b]}")
            letters[a], letters[i] = letters[i], letters[a]

        for j in range(n_edges, n_letters):
            material = random.choice("WMP")
            edges[letters[j]] = material
            edge_strs.append(f"{letters[j]}:{material}")

        random.shuffle(letters)
        random.shuffle(edge_strs)

        rhs = []
        for ch in letters:
            while ch not in "WMP":
                ch = edges[ch]
            rhs.append(ch)

        lhs = f"{''.join(letters)}@{','.join(edge_strs)}"

        assert r(lhs) == "".join(rhs)


def test_solution30(r):
    random.seed(0)
    assert r("aba") == "Y"
    assert r("ab") == "N"
    assert r("abccba") == "Y"

    letters = "abcdef"
    for _ in range(100):
        length = random.randint(1, 16)
        half = "".join(random.choices(letters, k=length // 2))
        mid = "" if length % 2 else random.choice(letters)
        lhs = half + mid + half[::-1]
        assert r(lhs) == "Y"

    for _ in range(100):
        length = random.randint(1, 16)
        lhs = random.choices(letters, k=length)
        rhs = "Y" if lhs == lhs[::-1] else "N"
        assert r(lhs) == rhs


def test_solution31(r):
    random.seed(0)
    assert r("||||") == "4"
    for _ in range(10):
        num = random.randint(1, 2000)
        assert r(tally(num)) == str(num)


def test_solution32(r):
    solution_file = SOLUTIONS_DIR / "32.txt"

    if not solution_file.exists():
        pytest.fail(f"Solution file {solution_file} does not exist")

    with open(solution_file, "r", encoding="utf-8") as f:
        code = f.read()

    rules = logic_mill.parse_transition_rules(code)

    # Trim final newline
    code = code.rstrip("\n")

    # Note that this keeps comments
    rules_str = code.replace("\n", "@").replace(" ", "")

    assert r(rules_str) == tally(len(rules))


def test_solution33(r):
    assert r("()") == "Y"
    assert r("()[]") == "Y"
    assert r("{}") == "Y"
    assert r("([{}])") == "Y"
    assert r("((()))") == "Y"
    assert r("{[()]}") == "Y"
    assert r("()(") == "N"
    assert r("(]") == "N"
    assert r("([)]") == "N"
    assert r("((())") == "N"
    assert r("())") == "N"


def test_solution34(r):
    random.seed(0)

    assert r("(1&0)") == "0"
    assert r("((0|1)!1)") == "0"
    assert r("(1!(1!1))") == "1"

    for a in [0, 1]:
        for b in [0, 1]:
            for op in "&|^!":
                lhs = f"({a}{op}{b})"
                if op == "&":
                    rhs = a & b
                elif op == "|":
                    rhs = a | b
                elif op == "^":
                    rhs = (~(a | b)) & 1
                elif op == "!":
                    rhs = a ^ b
                assert r(lhs) == str(rhs)

    Node = int | tuple["Node", typing.Literal["&", "|", "^", "!"], "Node"]

    def build_tree(min_depth: int, max_depth: int) -> Node:
        if max_depth == 0:
            return random.randint(0, 1)

        choices = ["&", "|", "^", "!", "int"]
        if min_depth > 0:
            choices.pop()

        op = random.choice(choices)

        if op == "int":
            return random.randint(0, 1)

        a = build_tree(max(min_depth - 1, 0), max(max_depth - 1, 0))
        b = build_tree(max(min_depth - 1, 0), max(max_depth - 1, 0))

        return (a, op, b)

    def to_str(node: Node) -> str:
        if isinstance(node, int):
            return str(node)
        left, op, right = node
        return f"({to_str(left)}{op}{to_str(right)})"

    def evaluate(node: Node) -> int:
        if isinstance(node, int):
            return node
        left, op, right = node

        a = evaluate(left)
        b = evaluate(right)

        if op == "&":
            return a & b
        elif op == "|":
            return a | b
        elif op == "^":
            return (~(a | b)) & 1
        elif op == "!":
            return a ^ b

    for _ in range(100):
        root = build_tree(1, 5)
        if isinstance(root, int):
            continue

        lhs = to_str(root)
        rhs = evaluate(root)

        assert r(lhs) == str(rhs)


def test_solution35(r):
    random.seed(0)

    assert r("|,||,||,|||,|") == "|,||,|||"

    for _ in range(100):
        n_nums = random.randint(1, 20)
        nums = [random.randint(1, 20) for _ in range(n_nums)]
        lhs = ",".join(tally(num) for num in nums)

        seen = set()
        rhs = []
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            rhs.append(tally(num))
        rhs = ",".join(rhs)

        assert r(lhs) == rhs


def test_solution36(r):
    random.seed(0)

    assert r("||,|||,||") == "||,|,||"

    for _ in range(100):
        n_piles = random.randint(1, 20)
        piles = [random.randint(1, 20) for _ in range(n_piles)]
        lhs = ",".join(tally(pile) for pile in piles)

        while True:
            for i in range(n_piles):
                if piles[i] >= 3:
                    piles[i] -= 2
                    if i:
                        piles[i - 1] += 1
                    if i + 1 < n_piles:
                        piles[i + 1] += 1
                    break
            else:
                break
        rhs = ",".join(tally(pile) for pile in piles)

        assert r(lhs) == rhs


def test_solution37(r):
    random.seed(0)

    assert r("||||||,||||") == "||"

    for _ in range(100):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        lhs = f"{tally(a)},{tally(b)}"
        rhs = tally(math.gcd(a, b))

        assert r(lhs) == rhs

    # Reached 20_000_000 limit with original solution
    hard_input = "||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||,||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
    a, b = map(len, hard_input.split(","))
    assert r(hard_input) == tally(math.gcd(a, b))


def test_solution38(r):
    random.seed(0)

    # assert r("Kb4,Nd5") == "Y"

    letters = "abcdefgh"
    for _ in range(100):
        king = white = (random.randint(0, 7), random.randint(0, 7))
        while white == king:
            white = (random.randint(0, 7), random.randint(0, 7))

        rook_check = king[0] == white[0] or king[1] == white[1]
        bishop_check = (
            king[0] - king[1] == white[0] - white[1]
            or king[0] + king[1] == white[0] + white[1]
        )
        knight_check = any(
            (white[0] + dx, white[1] + dy) == king
            for dx, dy in [(-2, 1), (-2, -1), (-1, -2), (-1, 2), (2, -1), (2, 1)]
        )

        # for piece in "QRBN":
        for piece in "QRB":
            lhs = f"K{letters[king[0]]}{king[1] + 1},{piece}{letters[white[0]]}{white[1] + 1}"
            match piece:
                case "Q":
                    check = rook_check or bishop_check
                case "R":
                    check = rook_check
                case "B":
                    check = bishop_check
                case "N":
                    check = knight_check
            rhs = "NY"[check]
            assert r(lhs) == rhs
