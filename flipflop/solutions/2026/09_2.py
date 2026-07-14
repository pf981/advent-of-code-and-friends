import collections

with open("./input/2026/09.txt") as f:
    lines = f.read().splitlines()
nrows = len(lines)
ncols = len(lines[0])


def shoot(r: int, c: int, dr: int, dc: int) -> tuple[int, int]:
    for i in range(1, nrows + ncols):
        r2 = r + i * dr
        c2 = c + i * dc
        if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            continue
        if lines[r2][c2] == "#":
            break
    i -= 1
    r2 = r + i * dr
    c2 = c + i * dc
    return r2, c2


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
            # Walk
            if (r + dr, c + dc) not in seen and lines[r + dr][c + dc] != "#":
                seen.add((r + dr, c + dc))
                q.append((r + dr, c + dc))

            # Shoot
            r2, c2 = shoot(r, c, dr, dc)
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue
            if lines[r2][c2] == "#":
                break
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
