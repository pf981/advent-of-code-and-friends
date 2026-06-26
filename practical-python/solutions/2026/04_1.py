import collections
import re
import math

with open("./input/2026/04/input1.txt") as f:
    text = f.read()

lines = text.splitlines()

nrows = len(lines)
ncols = len(lines[0])

# nrows, ncols = 4, 6  # TTEST

dr = nrows / 10_00000
dc = ncols / 10_00000
R = nrows / 100_000000
C = ncols / 100_000000
# r = c = R = C = 0

i = 0
seen = set()
r = R
c = C
while r < nrows + 1 and c < ncols + 1:
    r = math.floor(R + dr * i)
    c = math.floor(C + dc * i)
    i += 1
    if r >= nrows or c >= ncols:
        break
    seen.add((r, c))
print(len(seen))
