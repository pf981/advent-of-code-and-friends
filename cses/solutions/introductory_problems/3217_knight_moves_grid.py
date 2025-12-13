import collections

n = int(input())

grid = [[None] * n for _ in range(n)]
grid[0][0] = 0
q = collections.deque([(0, 0)])
d = 1
while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        for dr, dc in [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]:
            r2 = r + dr
            c2 = c + dc

            if not (0 <= r2 < n and 0 <= c2 < n):
                continue
            if grid[r2][c2] is not None:
                continue

            grid[r2][c2] = d
            q.append((r2, c2))

    d += 1

for row in grid:
    print(*row)
