import re

with open("./story_4/input/everybody_codes_e4_q03_p1.txt") as f:
    text = f.read()
# text = """width=30
# height=10
# horizontal-offsets=10011
# vertical-offsets=11011"""

ncols, nrows, horizontal_offsets, vertical_offsets = map(
    int, re.findall(r"-?\d+", text)
)
horizontal_offsets = list(map(int, str(horizontal_offsets)))
vertical_offsets = list(map(int, str(vertical_offsets)))

# NESW
N = 0
E = 1
S = 2
W = 3
grid = [[[False, False, False, False] for _ in range(ncols)] for _ in range(nrows)]

for r in range(nrows + 1):
    off = horizontal_offsets[r % len(horizontal_offsets)]
    print(f"{r=} {off=}")
    for c in range(off, ncols, 2):
        if r - 1 >= 0:
            grid[r - 1][c][S] = True
        if r < nrows:
            grid[r][c][N] = True

for c in range(ncols + 1):
    off = vertical_offsets[c % len(vertical_offsets)]
    print(f"{c=} {off=}")
    for r in range(off, nrows, 2):
        if c - 1 >= 0:
            grid[r][c - 1][E] = True
        if c < ncols:
            grid[r][c][W] = True

for r in range(nrows):
    for c in range(ncols):
        if grid[r][c][N]:
            if r - 1 >= 0:
                assert grid[r - 1][c][S]
        if grid[r][c][E]:
            if c + 1 < ncols:
                assert grid[r][c + 1][W]
        if grid[r][c][S]:
            if r + 1 < nrows:
                # print(f"{r=} {c=}")
                assert grid[r + 1][c][N]
        if grid[r][c][W]:
            if c - 1 >= 0:
                assert grid[r][c - 1][E]

for r in range(nrows):
    for c in range(ncols):
        ch = " -" if grid[r][c][N] else "  "
        print(ch, end="")
    print()
    for c in range(ncols):
        w = "|" if grid[r][c][W] else " "
        m = "X" if all(grid[r][c]) else " "
        # e = "|" if grid[r][c][E] else " "
        # e = ""
        e = "|" if c == ncols - 1 and grid[r][c][E] else ""
        ch = f"{w}{m}{e}"
        print(ch, end="")
    print()
for c in range(ncols):
    ch = " -" if grid[r][c][S] else "  "
    print(ch, end="")
print()

answer = sum(all(grid[r][c]) for r in range(nrows) for c in range(ncols))
print(answer)
# 282 wrong
# Your answer length is: correct
# The first character of your answer is: correct
