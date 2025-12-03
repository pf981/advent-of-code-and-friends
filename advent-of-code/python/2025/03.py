import functools

from aocd import get_data, submit


@functools.cache
def get_max_val(i: int, n: int, word: str) -> int | None:
    if n == 0:
        return 0

    if i == len(word):
        return None

    discard = get_max_val(i + 1, n, word)

    keep = None
    rest = get_max_val(i + 1, n - 1, word)
    if rest is not None:
        keep = int(word[i]) * (10 ** (n - 1)) + rest

    if discard is None or keep is None:
        return discard or keep

    return max(discard, keep)


inp = get_data(day=3, year=2025)

lines = inp.splitlines()

answer1 = sum(get_max_val(0, 2, word) for word in lines)
submit(answer1, part="a", day=3, year=2025)


# Part 2

answer2 = sum(get_max_val(0, 12, word) for word in lines)
submit(answer2, part="b", day=3, year=2025)
