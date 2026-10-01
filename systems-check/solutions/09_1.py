import collections

with open("./input/9.txt") as f:
    text = f.read()

grid = [line.split() for line in text.splitlines()]
g = [[int(c) if c not in "^*" else 0 for c in row] for row in grid]

nrows = len(g)
ncols = len(g[0])

start = next((r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "^")
end = next((r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "*")

d = 0
seen = {start}
q = collections.deque([start])
answer = None
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if (r, c) == end:
            answer = d
            break

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
                if (r2, c2) in seen:
                    continue

                seen.add((r2, c2))
                q.append((r2, c2))
    else:
        d += 1
        continue
    break

assert answer is not None
print(answer)
