import heapq

with open("data/0083_matrix.txt") as f:
    text = f.read()

grid = [[int(num) for num in line.split(",")] for line in text.splitlines()]
nrows = len(grid)
ncols = len(grid[0])

heap = [(grid[0][0], 0, 0)]  # [(d, r, c), ...]
seen = set()
while heap:
    d, r, c = heapq.heappop(heap)

    if (r, c) == (nrows - 1, ncols - 1):
        break

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if not (0 <= r2 < nrows and 0 <= c2 < ncols) or (r2, c2) in seen:
            continue

        heapq.heappush(heap, (d + grid[r2][c2], r2, c2))

answer = d
print(answer)
