import collections

with open("./2026/input/everybody_codes_e2026_q17_p3.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])


def is_set(r: int, c: int) -> bool:
    return 0 <= r < nrows and 0 <= c < ncols and lines[r][c] == "#"


def get_dirs(r: int, c: int, prev_r: int, prev_c: int) -> str:
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
    if tl != tr:
        dirs += "N"
    if br != tr:
        dirs += "E"
    if br != bl:
        dirs += "S"
    if bl != tl:
        dirs += "W"
    return dirs


q = collections.deque()  # [(r, c, prev_r, prev_c), ...]
q.append((0, 0, 0, 0))
seen = {(0, 0, 0, 0)}
d = 0
while q:
    for _ in range(len(q)):
        r, c, prev_r, prev_c = q.popleft()

        if (r, c) == (nrows, ncols):
            break

        for heading in get_dirs(r, c, prev_r, prev_c):
            r2 = r + (heading == "S") - (heading == "N")
            c2 = c + (heading == "E") - (heading == "W")

            if (r2, c2) == (prev_r, prev_c):
                continue
            if (r2, c2, r, c) in seen:
                continue
            seen.add((r2, c2, r, c))

            q.append((r2, c2, r, c))
    else:
        d += 1
        continue
    break

assert (r, c) == (nrows, ncols)
answer = d
print(answer)
