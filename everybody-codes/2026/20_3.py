import operator
from collections.abc import Iterator


def to_b_11(dec: int) -> str:
    result = []

    while dec > 0:
        dec, remainder = divmod(dec, 11)
        result.append("0123456789A"[remainder])

    return "".join(reversed(result))


def get_strings(line: str) -> Iterator[str]:
    yield line

    l = list(line)
    for i_take in range(len(line)):
        for take_c, leftover in take_one[l[i_take]]:
            l[i_take] = take_c
            if not leftover:
                yield "".join(l)
                l[i_take] = line[i_take]  # Restore
                continue

            for i_give in range(len(line)):
                if i_take == i_give:
                    continue
                for give_c in give_one[l[i_give]]:
                    l[i_give] = give_c

                    yield "".join(l)

                    l[i_give] = line[i_give]  # Restore

            l[i_take] = line[i_take]  # Restore


def is_valid(line: str) -> bool:
    l_a, l_op, l_b, _, r_a, r_op, r_b = line.split()
    l_a, l_b, r_a, r_b = (int(s, 11) for s in [l_a, l_b, r_a, r_b])
    l_f = {"+": operator.add, "-": operator.sub}[l_op]
    r_f = {"+": operator.add, "-": operator.sub}[r_op]
    return l_f(l_a, l_b) == r_f(r_a, r_b)


with open("./2026/input/everybody_codes_e2026_q20_p3.txt") as f:
    lines = f.read().splitlines()

# c -> [(c2, leftover), ...]
take_one = {
    "0": [("6", 0), ("9", 0), ("A", 0)],
    "1": [],
    "2": [("3", 0)],
    "3": [("2", 0), ("5", 0)],
    "4": [],
    "5": [("3", 0)],
    "6": [("0", 0), ("5", 1), ("9", 0), ("A", 0)],
    "7": [("1", 1)],
    "8": [("0", 1), ("6", 1), ("9", 1), ("A", 1)],
    "9": [("0", 0), ("3", 1), ("5", 1), ("6", 0), ("A", 0)],
    "+": [("-", 1)],
    "-": [],
    "=": [],
    " ": [],
    "A": [("0", 0), ("6", 0), ("9", 0)],
}

# c -> [c2, ...]
give_one = {
    "0": ["8"],
    "1": ["7"],
    "2": [],
    "3": ["9"],
    "4": [],
    "5": ["6", "9"],
    "6": ["8"],
    "7": [],
    "8": [],
    "9": ["8"],
    "+": [],
    "-": ["+"],
    "=": [],
    " ": [],
    "A": ["8"],
}

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

dec = 0
for line in lines:
    for line2 in get_strings(line):
        if is_valid(line2):
            dec += sum(count_segs[c] for c in line)
            break

answer = to_b_11(dec)
print(answer)
