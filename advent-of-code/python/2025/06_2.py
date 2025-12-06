from aocd import get_data, submit
import math
import itertools

inp = get_data(day=6, year=2025)
# inp = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   + """

lines = inp.splitlines()
x = []
for line in lines:
    # x.append(line.split())
    x.append(line)
z = list(itertools.zip_longest(*x, fillvalue=" "))

answer2 = 0
cur = []
op = sum
for r in z:
    try:
        num = int("".join(c for c in r if c.isdigit()))
    except ValueError:
        continue
    print(num)
    if r[-1] in "*+":
        answer2 += op(cur)

    if r[-1] == "+":
        op = sum
        cur = []
    elif r[-1] == "*":
        op = math.prod
        cur = []
    cur.append(num)

answer2 += op(cur)
print(answer2)
# answer1 = None
submit(answer2, part="b", day=6, year=2025)
