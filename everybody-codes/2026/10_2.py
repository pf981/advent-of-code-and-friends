import collections
import itertools

with open("./2026/input/everybody_codes_e2026_q10_p2.txt") as f:
    lines = f.read().splitlines()
MAX_COLLISIONS = 10000
# lines = """###########
# #####.#####
# ###.....###
# ##.......##
# ##.>>.<<.##
# #v...>...v#
# ##...v...##
# ##.......##
# ###.....###
# #####.#####
# ###########""".splitlines()
# MAX_COLLISIONS = 10

nrows = len(lines)
ncols = len(lines[0])

walls = set()
ghosts = collections.defaultdict(list)  # (r, c) -> [(heading, collisions), ...]
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] == ".":
            continue
        if lines[r][c] == "#":
            walls.add((r, c))
            continue

        assert lines[r][c] in "^>v<"
        ghosts[(r, c)].append((lines[r][c], 0))

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


def pp():
    for r in range(nrows):
        for c in range(ncols):
            ch = "."
            if (r, c) in walls:
                ch = "#"
            if (r, c) in ghosts:
                if len(ghosts[(r, c)]) > 1:
                    ch = len(ghosts[(r, c)])
                else:
                    ch = ghosts[(r, c)][0]
            print(ch, end="")
        print()


for round in itertools.count(1):
    ghosts2 = collections.defaultdict(list)

    for p in ghosts:
        for dir, collisions in ghosts[p]:
            p2 = (
                p[0] + (dir == "v") - (dir == "^"),
                p[1] + (dir == ">") - (dir == "<"),
            )
            if p2 in walls:
                collisions += 1
                p2 = p
                dir = rot90[dir]

            if collisions != MAX_COLLISIONS:
                ghosts2[p2].append((dir, collisions))

    # Ghost collisions
    ghosts3 = collections.defaultdict(list)
    for p in ghosts2:
        if len(ghosts2[p]) <= 1:
            ghosts3[p] = ghosts2[p]
            continue

        for dir, collisions in ghosts2[p]:
            collisions += 1
            if collisions != MAX_COLLISIONS:
                ghosts3[p].append((rot180[dir], collisions))

    ghosts = ghosts3
    # print(f"Round {round + 1} {collisions=}")
    # pp()
    # print()

    if all(not l for l in ghosts2.values()):
        break


answer = round
print(answer)
