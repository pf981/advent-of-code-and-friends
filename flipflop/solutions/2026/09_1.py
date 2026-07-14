import collections

with open("./input/2026/09.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])
r, c = next(
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "S"
)

q = collections.deque([(r, c)])
d = 0
seen = {(r, c)}
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if lines[r][c] == "E":
            break
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc

            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue
            if lines[r2][c2] == "#":
                continue

            if (r2, c2) in seen:
                continue
            seen.add((r2, c2))

            q.append((r2, c2))
    else:
        d += 1
        continue
    break

answer = d
print(answer)
