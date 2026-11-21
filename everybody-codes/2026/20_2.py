import operator


def to_b_11(dec: int) -> str:
    result = []

    while dec > 0:
        dec, remainder = divmod(dec, 11)
        result.append("0123456789A"[remainder])

    return "".join(reversed(result))


with open("./2026/input/everybody_codes_e2026_q20_p2.txt") as f:
    lines = f.read().splitlines()

count_segs = {
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
}
op = {"+": operator.add, "-": operator.sub}

dec = 0
for line in lines:
    l_a, l_op, l_b, _, r_a, r_op, r_b = line.split()
    l_a, l_b, r_a, r_b = (int(s, 11) for s in [l_a, l_b, r_a, r_b])
    l_f = op[l_op]
    r_f = op[r_op]
    if l_f(l_a, l_b) == r_f(r_a, r_b):
        dec += sum(count_segs[c] for c in line)

answer = to_b_11(dec)
print(answer)
