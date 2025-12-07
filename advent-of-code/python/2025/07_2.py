import functools

from aocd import get_data, submit


inp = get_data(day=7, year=2025)
lines = inp.splitlines()


@functools.cache
def count_ways(r, c):
    if r == len(lines):
        return 1

    if lines[r][c] == "^":
        return count_ways(r, c - 1) + count_ways(r, c + 1)
    return count_ways(r + 1, c)


answer2 = count_ways(0, lines[0].index("S"))
submit(answer2, part="b", day=7, year=2025)
