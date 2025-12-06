from aocd import get_data, submit
import math

inp = get_data(day=6, year=2025)
# inp = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   + """

lines = inp.splitlines()
x = []
for line in lines:
    x.append(line.split())
z = list(zip(*x))

answer1 = 0
for r in z:
    if r[-1] == "+":
        answer1 += sum(int(f) for f in r[:-1])
    elif r[-1] == "*":
        answer1 += math.prod(int(f) for f in r[:-1])

print(answer1)
# answer1 = None
submit(answer1, part="a", day=6, year=2025)
