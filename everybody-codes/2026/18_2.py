import collections
import re

with open("./2026/input/everybody_codes_e2026_q18_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """x=0 y=5 width=1
# x=1 y=4 width=3
# x=5 y=3 width=2
# x=7 y=9 width=1
# x=8 y=8 width=1
# x=9 y=9 width=3
# x=12 y=3 width=1
# x=16 y=7 width=1
# x=19 y=3 width=5
# x=25 y=5 width=1
# x=29 y=1 width=2
# x=31 y=6 width=1""".splitlines()

hs = collections.Counter()  # x -> h
leftmost = {}  # h -> x
rightmost = {}  # h -> x

for line in lines:
    assert "-" not in line
    x, y, w = map(int, re.findall(r"\d+", line))

    for dx in range(w):
        hs[x + dx] += y

for x, h in hs.items():
    for y in range(h):
        if y not in leftmost:
            leftmost[y] = rightmost[y] = x
        leftmost[y] = min(leftmost[y], x)
        rightmost[y] = max(rightmost[y], x)

answer = 0
for h in leftmost:
    answer += rightmost[h] - leftmost[h] + 1
print(answer)
