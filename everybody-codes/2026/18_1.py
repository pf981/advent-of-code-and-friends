import collections
import re

with open("./2026/input/everybody_codes_e2026_q18_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """x=0 y=5
# x=5 y=7
# x=6 y=8
# x=7 y=1
# x=8 y=3
# x=10 y=6
# x=15 y=3
# x=18 y=4""".splitlines()

hs = collections.Counter()  # x -> h
leftmost = {}  # h -> x
rightmost = {}  # h -> x

for line in lines:
    assert "-" not in line
    x, y = map(int, re.findall(r"\d+", line))

    hs[x] += y

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
