import collections

with open("./input/2026/05/input1.txt") as f:
    text = f.read()
# text = """71717
# 20002
# 70417
# 20700
# 71600"""

lines = text.splitlines()
nrows = len(lines)
ncols = len(lines[0])
grid = collections.defaultdict(
    int, {(r, c): int(lines[r][c]) for r in range(nrows) for c in range(ncols)}
)

counts = [None, 0, 0, 0, 0, 0, 0]
for (r, c), val in list(grid.items()):
    if val != 7:
        continue
    n = grid[(r - 1, c)] in (2, 4, 5)
    e = grid[(r, c + 1)] in (1, 5, 6)
    s = grid[(r + 1, c)] in (2, 3, 6)
    w = grid[(r, c - 1)] in (1, 3, 4)

    assert n + e + s + w == 2
    if e and w:
        wall = 1
    elif n and s:
        wall = 2
    elif n and e:
        wall = 3
    elif e and s:
        wall = 4
    elif s and w:
        wall = 5
    elif n and w:
        wall = 6

    counts[wall] += 1

answer = "".join(str(count) for count in counts[1:])
print(answer)
