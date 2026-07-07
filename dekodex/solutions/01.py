import collections

with open("input/01.txt") as f:
    text = f.read()

n_m, *lines = text.splitlines()
nrows, ncols = map(int, n_m.split())

assert len(lines) == nrows
assert len(lines[0]) == ncols

grid = [list(line) for line in lines]

q = collections.deque(
    (r, c) for r in range(nrows) for c in range(ncols) if grid[r][c] == "A"
)
seen = {(q[0])}
d = 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if grid[r][c] == "B":
            break

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc

            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            if (r2, c2) in seen:
                continue
            seen.add((r2, c2))

            if grid[r2][c2] not in ".B":
                continue

            q.append((r2, c2))

    else:
        d += 1
        continue
    break
else:
    raise ValueError("Cannot find B")

answer = d
print(answer)
