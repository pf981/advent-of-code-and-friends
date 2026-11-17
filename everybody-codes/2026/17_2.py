import collections

with open("./2026/input/everybody_codes_e2026_q17_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """####.######
# #.#.##..#..
# ##.##.##..#
# #.#.###.###
# #.###.###.#
# ###.##.#.##""".splitlines()

nrows = len(lines)
ncols = len(lines[0])


def is_set(r, c):
    return 0 <= r < nrows and 0 <= c < ncols and lines[r][c] == "#"


def get_dirs(r, c, prev_r, prev_c):
    if r == c == 0:
        return "ES"  # Hard code start
    tl, tr, bl, br = (
        is_set(r - 1, c - 1),
        is_set(r - 1, c),
        is_set(r, c - 1),
        is_set(r, c),
    )

    dr = r - prev_r
    dc = c - prev_c
    heading = {(-1, 0): "N", (0, 1): "E", (1, 0): "S", (0, -1): "W"}[(dr, dc)]

    # Diagonal special cases
    # X-
    # -X
    if (tl, tr, bl, br) == (True, False, False, True):
        match heading:
            case "N":
                return "E"
            case "E":
                return "N"
            case "S":
                return "W"
            case "W":
                return "S"

    # -X
    # X-
    if (tl, tr, bl, br) == (False, True, True, False):
        match heading:
            case "N":
                return "W"
            case "E":
                return "S"
            case "S":
                return "E"
            case "W":
                return "N"

    dirs = ""
    # if bl == tl and tl != tr:
    if tl != tr:
        dirs += "N"
    if br != tr:
        dirs += "E"
    if br != bl:
        dirs += "S"
    if bl != tl:
        dirs += "W"
    return dirs


q = collections.deque()  # [(r, c, prev_r, prev_c, hit_end), ...]
q.append((0, 0, 0, 0, False))
seen = {(0, 0, 0, 0, False)}
d = 0
while q:
    for _ in range(len(q)):
        r, c, prev_r, prev_c, hit_end = q.popleft()
        print(r, c, prev_r, prev_c, hit_end)

        if (r, c) == (nrows, ncols):  # FIXME: Not the target
            hit_end = True

        if (r, c) == (0, 0) and hit_end:
            break

        for heading in get_dirs(r, c, prev_r, prev_c):
            r2 = r + (heading == "S") - (heading == "N")
            c2 = c + (heading == "E") - (heading == "W")

            if (r2, c2) == (prev_r, prev_c):
                continue
            # if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            #     continue
            if (r2, c2, r, c, hit_end) in seen:
                continue

            tl, tr, bl, br = (
                is_set(r - 1, c - 1),
                is_set(r - 1, c),
                is_set(r, c - 1),
                is_set(r, c),
            )

            seen.add((r2, c2, r, c, hit_end))

            q.append((r2, c2, r, c, hit_end))
    else:
        d += 1
        continue
    break

assert (r, c) == (0, 0) and hit_end
answer = d
print(answer)


# # 4,7 N not working
# def get_dirs(r, c):
#     tl, tr, bl, br = (
#         is_set(r - 1, c - 1),
#         is_set(r - 1, c),
#         is_set(r, c - 1),
#         is_set(r, c),
#     )
#     dirs = ""
#     if br == tr and tl != tr:
#         dirs += "N"
#     if br != tr:
#         dirs += "E"
#     if br != bl:
#         dirs += "S"
#     if bl != tl:
#         dirs += "W"
#     return dirs
# get_dirs(4,7)
