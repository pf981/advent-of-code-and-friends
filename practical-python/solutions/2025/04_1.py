import re

with open("./input/2025/04/input1.txt") as f:
    lines = f.read().splitlines()

xs = []
ys = []
for line in lines:
    m1, x1, y1, m2, x2, y2, m3, x3, y3 = map(int, re.findall(r"-?\d+", line))
    denom = m1 + m2 + m3

    xs.append((m1 * x1 + m2 * x2 + m3 * x3) // denom)
    ys.append((m1 * y1 + m2 * y2 + m3 * y3) // denom)

answer = "".join(map(chr, xs)) + " " + "".join(map(chr, ys))
print(answer)
