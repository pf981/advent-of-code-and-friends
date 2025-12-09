from aocd import get_data, submit


inp = get_data(day=9, year=2025)
lines = inp.splitlines()
nums = [[int(x) for x in line.split(",")] for line in lines]

answer1 = 0
for a in nums:
    for b in nums:
        w = abs(b[0] - a[0]) + 1
        h = abs(b[1] - a[1]) + 1
        answer1 = max(answer1, (w * h))

submit(answer1, part="a", day=9, year=2025)
