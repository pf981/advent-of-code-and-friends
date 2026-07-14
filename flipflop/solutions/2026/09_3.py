import collections
import functools
import heapq
import itertools

with open("./input/2026/09.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])


@functools.cache
def shoot(r: int, c: int, dr: int, dc: int) -> tuple[int, int] | None:
    if not (0 <= r < nrows and 0 <= c < ncols) or lines[r][c] == "#":
        return None
    nxt = shoot(r + dr, c + dc, dr, dc)
    return nxt if nxt else (r, c)


naive_steps = {}
end = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "E")
naive_steps[end] = 0
seen = {end}
d = 1
q = collections.deque([end])
while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            # Walk
            r2, c2 = r + dr, c + dc
            if (r2, c2) not in naive_steps and lines[r2][c2] != "#":
                naive_steps[(r2, c2)] = d
                q.append((r2, c2))

            # Simplified shoot
            if lines[r2][c2] == "#":
                for i in itertools.count(1):
                    r2 = r - i * dr
                    c2 = c - i * dc
                    if lines[r2][c2] == "#":
                        break
                    if (r2, c2) in naive_steps:
                        continue
                    else:
                        naive_steps[(r2, c2)] = d
                        q.append((r2, c2))
        d += 1

start = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "S")
q = collections.deque([(*start, tuple())])
d = 0
seen = {q[0]}
CAP = 100
while q:
    if len(q) > CAP:
        q = collections.deque(
            heapq.nsmallest(CAP, q, key=lambda x: naive_steps[(x[0], x[1])])
        )

    for _ in range(len(q)):
        r, c, portals = q.popleft()
        if lines[r][c] == "E":
            break

        # Walk
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (r + dr, c + dc, portals) not in seen and lines[r + dr][c + dc] != "#":
                seen.add((r + dr, c + dc, portals))
                q.append((r + dr, c + dc, portals))

        # Portal
        if len(portals) == 2 and (r, c) in portals:
            r2, c2 = next(p for p in portals if p != (r, c))
            if (r2, c2, portals) not in seen:
                seen.add((r2, c2, portals))
                q.append((r2, c2, portals))

        # Shoot
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2, c2 = shoot(r, c, dr, dc)

            # Shoot 1
            portals2 = tuple(sorted(set(portals[1:]) | {(r2, c2)}))
            if (r, c, portals2) not in seen:
                seen.add((r, c, portals2))
                q.append((r, c, portals2))

            # Shoot 2
            portals2 = tuple(sorted(set(portals[:1]) | {(r2, c2)}))
            if (r, c, portals2) not in seen:
                seen.add((r, c, portals2))
                q.append((r, c, portals2))
    else:
        d += 1
        continue
    break

answer = d
print(answer)
