from aocd import get_data, submit


inp = get_data(day=1, year=2025)

p = 50
answer1 = answer2 = 0
for line in inp.splitlines():
    n = int(line[1:])
    sign = 1 if line[0] == "R" else -1
    for _ in range(n):
        p = (p + sign) % 100
        answer2 += p == 0
    answer1 += p == 0

submit(answer1, part="a", day=1, year=2025)


# Part 2

submit(answer2, part="b", day=1, year=2025)
