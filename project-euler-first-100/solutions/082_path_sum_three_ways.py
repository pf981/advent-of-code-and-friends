import heapq

with open("data/0082_matrix.txt") as f:
    text = f.read()

grid = [[int(s) for s in line.split(",")] for line in text.splitlines()]
n = len(grid)

heap: list[tuple[int, int, int]] = []  # [(d, r, c), ...]
for r in range(n):
    heapq.heappush(heap, (grid[r][0], r, 0))

seen = set()
while heap:
    d, r, c = heapq.heappop(heap)

    if c == n - 1:
        break

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in [(-1, 0), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if not (0 <= r2 < n):
            continue
        heapq.heappush(heap, (d + grid[r2][c2], r2, c2))

answer = d
print(answer)
