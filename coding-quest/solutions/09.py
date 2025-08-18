import collections

import downloader

lines = downloader.get_puzzle(9).splitlines()

grid = lines
nrows = len(grid)
ncols = len(grid[0])

d = 0
q = collections.deque([(0, lines[0].index(" "))])
seen = set()
while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        if r == nrows - 1:
            break

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            if (r2, c2) in seen:
                continue

            if grid[r2][c2] != " ":
                continue

            seen.add((r2, c2))

            q.append((r2, c2))
    d += 1

answer = d
print(answer)
