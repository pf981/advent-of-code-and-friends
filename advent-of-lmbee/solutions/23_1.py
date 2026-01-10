import heapq
import math


def get_min_sum(grid: list[str]) -> int:
    nrows = len(grid)
    ncols = len(grid[0])

    heap = [(0, 0, 0)]
    visited = set()
    while heap:
        d, r, c = heapq.heappop(heap)

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if grid[r][c] == "E":
            return d

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc

            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue
            if (r2, c2) in visited:
                continue

            d2 = d
            if grid[r][c].isdigit():
                d2 += int(grid[r][c])
            heapq.heappush(heap, (d2, r2, c2))

    return 0


with open("data/day23.txt") as f:
    text = f.read()

grids = [grid.splitlines() for grid in text.split("\n\n")]

sums = [get_min_sum(grid) for grid in grids]
answer = math.prod(sums)
print(answer)
