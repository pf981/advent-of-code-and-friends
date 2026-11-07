import collections

with open("./2026/input/everybody_codes_e2026_q10_p3.txt") as f:
    lines = f.read().splitlines()
MAX_COLLISIONS = 1000000000000
# lines = """#######################
# ###########.###########
# #######.^>.^.<^.#######
# #####..<.>.v^>>^^<#####
# ####..v<^v.>.>v..^.####
# ###.................###
# ###.................###
# ##.......<...<.<....>##
# ##...v....>....v.v<.^##
# ##........###........##
# ##v......#####.......##
# #.<......#####......>.#
# ##.......#####.......##
# ##........###........##
# ##...................##
# ##...................##
# ###.................###
# ###.................###
# ####...............####
# #####.............#####
# #######....v....#######
# ###########.###########
# #######################""".splitlines()
# MAX_COLLISIONS = 1000000000000
# MAX_COLLISIONS = 20  # FIXME: Test

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


# def pp():
#     for r in range(nrows):
#         for c in range(ncols):
#             ch = "."
#             if (r, c) in walls:
#                 ch = "#"
#             if (r, c) in ghosts:
#                 if len(ghosts[(r, c)]) > 1:
#                     ch = len(ghosts[(r, c)])
#                 else:
#                     ch = ghosts[(r, c)][0][0]
#             print(ch, end="")
#         print()


seen = {}  # ((r, c, dir), ...) -> (round, (collisions, ...))
round = 1
while True:
    h = tuple((r, c, dir) for r, c, dir, _ in ghosts)
    if h in seen:
        print(f"\n{round=} Seen at {seen[h][0]=} {h=}")

        deltas = []
        n_periods = float("inf")
        for collisions_prev, (_, _, _, collisions) in zip(seen[h][1], ghosts):
            delta = collisions - collisions_prev
            deltas.append(delta)
            # collisions + delta * n_periods = MAX_COLLISIONS
            # n_periods = (MAX_COLLISIONS - collisions) // delta
            n_periods = min(n_periods, (MAX_COLLISIONS - collisions - 1) // delta)

        # FIXME: TEST
        # if (n_periods - 1) >= 1:
        #     n_periods -= 1

        assert n_periods >= 1
        assert n_periods != float("inf")

        period_size = round - seen[h][0]
        print(f"{round=} {n_periods=} {period_size=}")
        round += n_periods * period_size

        # You could update the round, but I don't think you need to
        # because you won't use any seen round prior to this
        seen.clear()

        print(
            [
                collisions + n_periods * delta
                for (r, c, dir, collisions), delta in zip(ghosts, deltas)
            ]
        )

        ghosts = [
            (r, c, dir, collisions2)
            for (r, c, dir, collisions), delta in zip(ghosts, deltas)
            if (collisions2 := collisions + n_periods * delta) < MAX_COLLISIONS
        ]

        # FIXME: TEST:
        # round -= 1
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
    # print(f"Round {round}")
    # pp()
    # print()

    if not ghosts:
        break

    round += 1


answer = round
print(answer)

# Example
# Have:      13314695352592
# Should be: 13314695352588
# 4 too many?
