import collections

with open("./2026/input/everybody_codes_e2026_q10_p1.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

walls = set()
ghosts = collections.defaultdict(list)
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] == ".":
            pass
        elif lines[r][c] == "#":
            walls.add((r, c))
        else:
            assert lines[r][c] in "^>v<"
            ghosts[(r, c)].append(lines[r][c])

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

answer = 0
for round in range(10):
    ghosts2 = collections.defaultdict(list)
    collisions = 0

    for p in ghosts:
        for dir in ghosts[p]:
            p2 = (
                p[0] + (dir == "v") - (dir == "^"),
                p[1] + (dir == ">") - (dir == "<"),
            )
            if p2 in walls:
                collisions += 1
                p2 = p
                dir = rot90[dir]

            ghosts2[p2].append(dir)

    # Ghost collisions
    for dirs in ghosts2.values():
        if len(dirs) <= 1:
            continue
        collisions += len(dirs)
        for i in range(len(dirs)):
            dirs[i] = rot180[dirs[i]]

    ghosts = ghosts2

    answer += collisions

print(answer)
