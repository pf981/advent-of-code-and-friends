import operator

with open("./2026/input/everybody_codes_e2026_q20_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """10 + 2A = 13 + 27
# 98 - 54 = 76 - 32
# 10 + 12 = 30 - 9
# 20 - 10 = 5 + 5""".splitlines()


def get_segments(c: str) -> int:
    return {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6,
        "+": 2,
        "-": 1,
        "=": 2,
        " ": 0,
        "A": 6,
    }[c]


def to_b_11(dec: int) -> str:
    result = []

    while dec > 0:
        dec, remainder = divmod(dec, 11)
        result.append("0123456789A"[remainder])

    return "".join(reversed(result))


dec = 0
for line in lines:
    # 5156 + 845 = 7122 - 1232
    l_a, l_op, l_b, _, r_a, r_op, r_b = line.split()
    l_a, l_b, r_a, r_b = (int(s, 11) for s in [l_a, l_b, r_a, r_b])
    l_f = {"+": operator.add, "-": operator.sub}[l_op]
    r_f = {"+": operator.add, "-": operator.sub}[r_op]
    if l_f(l_a, l_b) == r_f(r_a, r_b):
        print(sum(map(get_segments, line)))
        dec += sum(map(get_segments, line))

answer = to_b_11(dec)
print(answer)
# 80354
# Your answer length is: correct
# The first character of your answer is: incorrect
