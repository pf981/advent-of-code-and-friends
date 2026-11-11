with open("./2026/input/everybody_codes_e2026_q12_p2.txt") as f:
    lines = f.read().splitlines()

seen = set()

nrows = len(lines)
ncols = len(lines[0])


def get_points(r: int, c: int) -> set:
    points = {(r, c)}

    if not (0 <= r < nrows and 0 <= c < ncols) or lines[r][c] != "#" or (r, c) in seen:
        return set()
    seen.add((r, c))

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        points = points | get_points(r2, c2)

    return points


def get_w1_h1_w2_h2(r, c) -> tuple[int, int, int, int]:
    points = get_points(r, c)
    min_r, max_r, min_c, max_c = nrows, 0, ncols, 0

    lines2 = [["."] * ncols for _ in range(nrows)]
    for r in range(nrows):
        for c in range(ncols):
            if (r, c) in points:
                lines2[r][c] = "#"
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)

    if not (min_r <= max_r and min_c <= max_c):
        return 0, 0, 0, 0

    # Single rect
    if all(
        lines2[r2][c2] == "#"
        for r2 in range(min_r, max_r + 1)
        for c2 in range(min_c, max_c + 1)
    ):
        return max_r - min_r + 1, max_c - min_c + 1, 0, 0

    w1 = sum(ch == "#" for ch in lines2[min_r][min_c : max_c + 1])
    w2 = sum(ch == "#" for ch in lines2[max_r][min_c : max_c + 1])
    h1 = 0
    for r in range(min_r, max_r + 1):
        if sum(ch == "#" for ch in lines2[r][min_c : max_c + 1]) != w1:
            break
        h1 += 1
    h2 = max_r - min_r + 1 - h1

    return w1, h1, w2, h2


answer = 0
for r in range(nrows):
    for c in range(ncols):
        w1, h1, w2, h2 = get_w1_h1_w2_h2(r, c)

        options = [h1 + h2, max(w1, w2), w1 + h2, w2 + h1]
        if min(options) == 0:
            continue

        answer += min(options)

print(answer)
