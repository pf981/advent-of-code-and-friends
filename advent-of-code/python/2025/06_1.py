import math

from aocd import get_data, submit


inp = get_data(day=6, year=2025)

rows = [line.split() for line in inp.splitlines()]
cols = list(zip(*rows))

answer1 = 0
for col in cols:
    nums = [int(x) for x in col[:-1]]
    op = {"+": sum, "*": math.prod}[col[-1]]
    answer1 += op(nums)

submit(answer1, part="a", day=6, year=2025)
