import math

with open("./input/2026/04/input1.txt") as f:
    text = f.read()

lines = text.splitlines()

nrows = len(lines)
ncols = len(lines[0])

dr = nrows / 100_000
dc = ncols / 100_000
r = R = nrows / 100_000_000
c = C = ncols / 100_000_000

i = 0
seen = set()
while True:
    r = math.floor(R + dr * i)
    c = math.floor(C + dc * i)
    if r >= nrows or c >= ncols:
        break
    seen.add((r, c))
    i += 1

answer = len(seen)
print(answer)
