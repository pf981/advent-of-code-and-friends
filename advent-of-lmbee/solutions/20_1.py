import math
import re


def does_overlap(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> bool:
    d = math.dist((x1, y1), (x2, y2))
    return d < r1 + r2


with open("data/day20.txt") as f:
    text = f.read()

circles = [[int(x) for x in re.findall(r"\d+", line)] for line in text.splitlines()]
n = len(circles)
best = 0, 0, 0
for i in range(n):
    overlap = sum(does_overlap(*circles[i], *circles[j]) for j in range(n) if i != j)
    best = max(best, (overlap, circles[i][0], circles[i][1]))

answer = best[1] * best[2] + best[0]
print(answer)
