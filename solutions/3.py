with open("data/3/2d-grid-of-particles.txt") as f:
    grid = f.read().splitlines()

nrows = len(grid)
ncols = len(grid[0])
center_r, center_c = next(
    (r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "C"
)

assert f"(X:{center_c}, y:{center_r})" == "(X:51, y:26)"

answer = 0
for r in range(nrows):
    for c in range(ncols):
        if grid[r][c] != "•":
            continue

        d = abs(r - center_r) + abs(c - center_c)
        answer += d

print(answer)
