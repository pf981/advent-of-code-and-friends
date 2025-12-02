import itertools

from aocd import get_data, submit


inp = get_data(day=2, year=2025)
lines = inp.splitlines()


def is_invalid(num: int) -> bool:
    s = str(num)
    w = len(s) // 2

    if len(s) % 2 == 1:
        return False

    return s[:w] == s[w:]


answer1 = 0
for rng in lines[0].split(","):
    a, b = rng.split("-")
    a = int(a)
    b = int(b)
    for num in range(a, b + 1):
        if is_invalid(num):
            answer1 += num

submit(answer1, part="a", day=2, year=2025)


# Part 2


def is_invalid(num: int) -> bool:
    s = str(num)

    for w in range(1, len(s) // 2 + 1):
        if len(s) % w != 0:
            continue

        if len(set(["".join(chars) for chars in itertools.batched(s, w)])) == 1:
            return True

    return False


answer2 = 0
for rng in lines[0].split(","):
    a, b = rng.split("-")
    a = int(a)
    b = int(b)
    for num in range(a, b + 1):
        if is_invalid(num):
            answer2 += num

submit(answer2, part="b", day=2, year=2025)
