import heapq

with open("./input/9.txt") as f:
    text = f.read()

grid = [line.split() for line in text.splitlines()]
g = [[int(c) if c not in "^*" else 0 for c in row] for row in grid]

nrows = len(g)
ncols = len(g[0])

start = next((r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "^")
end = next((r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "*")

seen = set()
heap = [(0, *start)]
answer = None
while heap:
    d, r, c = heapq.heappop(heap)

    if (r, c) == end:
        answer = d
        break

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue

            r2 = r + dr
            c2 = c + dc

            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            if abs(g[r][c] - g[r2][c2]) > 1:
                continue

            d2 = d + 1 + 4 * (g[r2][c2] > g[r][c])
            heapq.heappush(heap, (d2, r2, c2))

assert answer is not None
print(answer)
