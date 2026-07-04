with open("./input/2026/05/input2.txt") as f:
    text = f.read()
# text = """4150000000
# 2031504150
# 3500316020
# 0200000035
# 4600000002
# 2000000002
# 200000@002
# 2000000002
# 2000000002
# 3111111116"""

grid = text.splitlines()
nrows = len(grid)
ncols = len(grid[0])
start = next((r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "@")

seen = {start}
stack = [start]
while stack:
    r, c = stack.pop()
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            r2 = r + dr
            c2 = c + dc

            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            if grid[r2][c2] != "0":
                continue

            if (r2, c2) in seen:
                continue
            seen.add((r2, c2))
            stack.append((r2, c2))

answer = len(seen)
print(answer)
