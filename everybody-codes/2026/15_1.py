import heapq

with open("./2026/input/everybody_codes_e2026_q15_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """#####################################################
# #.@.........#................#.....................##
# #.#########@#.##############.#.###################.##
# #.#.......#.#.##..........##.#.###..@..@......@###.##
# #.#.#####.#.#.##.########.##.#.###@###########.###.##
# #.#.#@@@#.#.#.##.##....##.##@#.###.###.....###.###.##
# #.#.#.#.#.#.#.##.##.##.##.##.#.###.###.###.###.###.##
# S...................................................E
# #.#.#.#.#.#.#.##.##.##.##.##.#.###.###.###.###.###@##
# #.#.#...#.#.#.##@##.@..##.##.#.###.###@....###.###.##
# #.#.#####.#.#.##.########.##.#.###.###########.###.##
# #.#.......#.#.##..@.......##.#.###.............###.##
# #.#########.#.##############.#.###################.##
# #...........#................#................@....##
# #####################################################""".splitlines()

nrows = len(lines)
ncols = len(lines[0])
start = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "S")
to_collect = {(r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "@"}
seen = set()

heap = [(0, *start, -1, -1, frozenset())]  # [(d,r,c,prev_r,prev_c,collected), ...]
while heap:
    d, r, c, prev_r, prev_c, collected = heapq.heappop(heap)
    # print((r, c, prev_r, prev_c, collected))

    if (r, c, prev_r, prev_c, collected) in seen:
        continue
    seen.add((r, c, prev_r, prev_c, collected))

    if lines[r][c] == "E" and len(collected) == len(to_collect):
        break

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if (r2, c2) == (prev_r, prev_c):
            continue

        if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            continue

        if lines[r2][c2] == "#":
            continue

        collected2 = collected
        if (r2, c2) in to_collect:
            collected2 |= {(r2, c2)}
        heapq.heappush(heap, (d + 1, r2, c2, r, c, collected2))

assert lines[r][c] == "E"
answer = d
print(answer)
