import collections
import functools

with open("./input/2026/09.txt") as f:
    lines = f.read().splitlines()
# lines = """#######
# #S....#
# #####.#
# #E#.#.#
# #.###.#
# #.....#
# #######""".splitlines()
# lines = """###########
# #S#.#...#.#
# #.#.#.###.#
# #.#.......#
# #.#.#.#####
# #...#.#..E#
# ###.#.#.###
# #...#.#...#
# #.###.#.#.#
# #.#.....#.#
# ###########""".splitlines()
nrows = len(lines)
ncols = len(lines[0])
r, c = next(
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "S"
)


@functools.cache
def shoot(r, c, dr, dc):
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


q = collections.deque([(r, c, tuple())])
d = 0
seen = {(r, c, tuple())}
while q:
    # print(q)
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
            # print(portals, r, c)
            r2, c2 = next(p for p in portals if p != (r, c))
            if (r2, c2, portals) not in seen:
                q.append((r2, c2, portals))
                seen.add((r2, c2, portals))
                # Remove other portal, if you chose not to portal there
                portals = ((r, c),)

        # Shoot 1
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2, c2 = shoot(r, c, dr, dc)

            # Shoot 1
            t = list(portals[1:])
            t.append((r2, c2))
            t.sort()
            t = tuple(set(t))

            if (r, c, t) not in seen:
                seen.add((r, c, t))
                q.append((r, c, t))

            # Shoot 2
            t = list(portals[:1])
            t.append((r2, c2))
            t.sort()
            t = tuple(set(t))

            # print(f"{r=} {c=} {t=}")
            if (r, c, t) not in seen:
                seen.add((r, c, t))
                q.append((r, c, t))
    else:
        # print(q)
        # break  # FIXME:REMOVE
        d += 1
        continue
    break
answer = d
print(answer)
# 51 too low
# 1338 too high
