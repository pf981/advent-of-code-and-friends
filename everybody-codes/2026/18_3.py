import collections
import re

with open("./2026/input/everybody_codes_e2026_q18_p3.txt") as f:
    lines = f.read().splitlines()

hs = collections.Counter()  # x -> h
leftmost = {}  # h -> x
rightmost = {}  # h -> x

for line in lines:
    assert "-" not in line
    x, y, w = map(int, re.findall(r"\d+", line))

    hs[x] += y
    if w > 1:
        hs[x + w - 1] += y

tallest = 0
for x in sorted(hs):
    h = hs[x]
    if h > tallest:
        for h2 in range(tallest + 1, h + 1):
            leftmost[h2] = x
        tallest = h

tallest = 0
for x in sorted(hs, reverse=True):
    h = hs[x]
    if h > tallest:
        for h2 in range(tallest + 1, h + 1):
            rightmost[h2] = x
        tallest = h

answer = 0
for h in leftmost:
    answer += rightmost[h] - leftmost[h] + 1
print(answer)
