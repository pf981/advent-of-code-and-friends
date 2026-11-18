import collections
import re

with open("./2026/input/everybody_codes_e2026_q18_p3.txt") as f:
    lines = f.read().splitlines()
lines = """x=0 y=5 width=1
x=1 y=4 width=3
x=5 y=3 width=2
x=7 y=9 width=1
x=8 y=8 width=1
x=9 y=9 width=3
x=12 y=3 width=1
x=16 y=7 width=1
x=19 y=3 width=5
x=25 y=5 width=1
x=29 y=1 width=2
x=31 y=6 width=1""".splitlines()

hs = collections.Counter()  # x -> h
leftmost = {}  # h -> x
rightmost = {}  # h -> x

for line in lines:
    assert "-" not in line
    x, y, w = map(int, re.findall(r"\d+", line))

    # for dx in range(w):
    #     hs[x + dx] += y
    hs[x] += y
    if w > 1:
        hs[x + w - 1] += y

# stack = [(-1, 0)]  # [(x, h), ...]
max_seen = (-1, 0)  # x, h
answer = 0
for x in sorted(hs):
    dx = max(x - max_seen[0] - 2, 0)
    print(f"{x=} {hs[x]=} {dx=} {max_seen=}")
    print(f"  pillar={hs[x]}; between_h={min(hs[x], max_seen[1])}")

    # Add pillar
    answer += hs[x]

    # Add between pillars
    answer += dx * min(hs[x], max_seen[1])
    if hs[x] > max_seen[1]:
        max_seen = (x, hs[x])


# for x, h in hs.items():
#     for y in range(h):
#         if y not in leftmost:
#             leftmost[y] = rightmost[y] = x
#         leftmost[y] = min(leftmost[y], x)
#         rightmost[y] = max(rightmost[y], x)

# answer = 0
# for h in leftmost:
#     answer += rightmost[h] - leftmost[h] + 1
print(answer)
