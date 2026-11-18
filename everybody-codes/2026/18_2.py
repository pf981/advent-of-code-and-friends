import collections
import re

with open("./2026/input/everybody_codes_e2026_q18_p2.txt") as f:
    lines = f.read().splitlines()

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
