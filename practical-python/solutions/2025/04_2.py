with open("./input/2025/04/input2.txt") as f:
    lines = f.read().splitlines()

grid = [list(map(int, line.split(","))) for line in lines]

nrows = len(grid)
ncols = len(grid[0])
seen = set()


def dfs(r: int, c: int) -> tuple[int, int, int, int]:
    m = grid[r][c]
    mass = m
    numerator_x = c * m
    numerator_y = r * m
    for r2, c2 in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
        if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            continue
        if (r2, c2) in seen:
            continue
        seen.add((r2, c2))
        if not grid[r2][c2]:
            continue
        m2, nx2, ny2 = dfs(r2, c2)
        mass += m2
        numerator_x += nx2
        numerator_y += ny2
    return mass, numerator_x, numerator_y


best = (0, 0, 0)  # mass, r, c
for r in range(nrows):
    for c in range(ncols):
        if (r, c) in seen:
            continue
        seen.add((r, c))

        mass, numerator_x, numerator_y = dfs(r, c)
        if not mass:
            continue
        best = max(best, (mass, numerator_x // mass, numerator_y // mass))

answer = f"{best[1]},{best[2]}"
print(answer)
