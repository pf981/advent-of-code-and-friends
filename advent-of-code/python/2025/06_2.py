import math

from aocd import get_data, submit


inp = get_data(day=6, year=2025)

rows = [line for line in inp.splitlines()]
cols = list(zip(*rows))
cols.append(tuple())

answer2 = 0
nums = []
op = None
for col in cols:
    num_str = "".join(c for c in col if c.isdigit())

    if not num_str:
        assert op
        answer2 += op(nums)
        op = None
        nums = []
        continue

    if op is None:
        op = {"+": sum, "*": math.prod}[col[-1]]

    nums.append(int(num_str))

submit(answer2, part="b", day=6, year=2025)
