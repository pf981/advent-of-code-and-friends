import collections

with open("./2026/input/everybody_codes_e2026_q10_p3.txt") as f:
    lines = f.read().splitlines()
MAX_COLLISIONS = 1000000000000

nrows = len(lines)
ncols = len(lines[0])

walls = set()
ghosts = []  # [(r, c, dir, collisions), ...]
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] == ".":
            continue
        if lines[r][c] == "#":
            walls.add((r, c))
            continue

        assert lines[r][c] in "^>v<"
        ghosts.append((r, c, lines[r][c], 0))

rot90 = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}
rot180 = {
    "^": "v",
    ">": "<",
    "v": "^",
    "<": ">",
}

seen = {}  # ((r, c, dir), ...) -> (round, (collisions, ...))
round = 1
while True:
    h = tuple((r, c, dir) for r, c, dir, _ in ghosts)
    if h in seen:
        deltas = []
        n_periods = float("inf")
        for collisions_prev, (_, _, _, collisions) in zip(seen[h][1], ghosts):
            delta = collisions - collisions_prev
            deltas.append(delta)
            n_periods = min(n_periods, (MAX_COLLISIONS - collisions - 1) // delta)

        assert n_periods >= 1
        assert n_periods != float("inf")

        period_size = round - seen[h][0]
        round += n_periods * period_size

        # Won't use any seen round prior to this
        seen.clear()

        ghosts = [
            (r, c, dir, collisions2)
            for (r, c, dir, collisions), delta in zip(ghosts, deltas)
            if (collisions2 := collisions + n_periods * delta) < MAX_COLLISIONS
        ]
    else:
        seen[h] = (round, (collisions for _, _, _, collisions in ghosts))

    ghosts2 = []
    positions_counts = collections.Counter()  # (r, c) -> count

    for r, c, dir, collisions in ghosts:
        r2 = r + (dir == "v") - (dir == "^")
        c2 = c + (dir == ">") - (dir == "<")

        if (r2, c2) in walls:
            collisions += 1
            r2, c2 = r, c
            dir = rot90[dir]

        if collisions != MAX_COLLISIONS:
            ghosts2.append((r2, c2, dir, collisions))
            positions_counts[(r2, c2)] += 1

    # Ghost collisions
    ghosts3 = []
    for r, c, dir, collisions in ghosts2:
        if positions_counts[(r, c)] <= 1:
            ghosts3.append((r, c, dir, collisions))
            continue

        collisions += 1
        if collisions != MAX_COLLISIONS:
            ghosts3.append((r, c, rot180[dir], collisions))

    ghosts = ghosts3

    if not ghosts:
        break

    round += 1

answer = round
print(answer)
