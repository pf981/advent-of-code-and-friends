import sys

sys.setrecursionlimit(1_000_000)

with open("./story_4/input/everybody_codes_e4_q03_p2.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    if line.startswith("width"):
        width = int(line.split("=")[1])
    elif line.startswith("height"):
        height = int(line.split("=")[1])
    elif line.startswith("horizontal-offsets"):
        horizontal_offs = list(map(int, line.split("=")[1]))
    elif line.startswith("vertical-offsets"):
        vertical_offs = list(map(int, line.split("=")[1]))
    else:
        assert False

nrows = height
ncols = width

isolated = set()
for r in range(nrows):
    for c in range(ncols):
        n = c % 2 == horizontal_offs[r % len(horizontal_offs)]
        e = r % 2 == vertical_offs[(c + 1) % len(vertical_offs)]
        s = c % 2 == horizontal_offs[(r + 1) % len(horizontal_offs)]
        w = r % 2 == vertical_offs[c % len(vertical_offs)]

        is_isolated = n and e and s and w
        if is_isolated:
            isolated.add((r, c))


colors = [[None] * ncols for _ in range(nrows)]


def fill(r: int, c: int, col: bool | None) -> None:
    if not (0 <= r < nrows and 0 <= c < ncols):
        return
    if colors[r][c] is not None:
        return

    if col is None:
        if (r, c) == (0, 0):
            col = True
        else:
            if r > 0:
                col = not colors[r - 1][c]
            else:
                col = not colors[r][c - 1]

    colors[r][c] = col

    n = c % 2 == horizontal_offs[r % len(horizontal_offs)]
    e = r % 2 == vertical_offs[(c + 1) % len(vertical_offs)]
    s = c % 2 == horizontal_offs[(r + 1) % len(horizontal_offs)]
    w = r % 2 == vertical_offs[c % len(vertical_offs)]

    if not n:
        fill(r - 1, c, col)
    if not e:
        fill(r, c + 1, col)
    if not s:
        fill(r + 1, c, col)
    if not w:
        fill(r, c - 1, col)


for r in range(nrows):
    for c in range(ncols):
        fill(r, c, None)

counts = [0, 0]
for r, c in isolated:
    counts[colors[r][c]] += 1

answer = max(counts)
print(answer)
