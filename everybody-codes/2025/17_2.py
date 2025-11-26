import itertools


with open("./2025/input/everybody_codes_e2025_q17_p2.txt") as f:
    lines = f.read().splitlines()

grid = {
    (r, c): int(ch) if ch not in "@" else 0
    for r, row in enumerate(lines)
    for c, ch in enumerate(row)
}

volcano = next(
    (r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == "@"
)
Yv, Xv = volcano


def get_lava(R: int) -> int:
    lava = 0
    for (r, c), num in grid.items():
        Xc = c
        Yc = r

        if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R and not (
            (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= (R - 1) * (R - 1)
        ):
            lava += num

    return lava


best = (0, 0)  # lava, R
for R in itertools.count(1):
    result = get_lava(R)
    if result == 0:
        break
    best = max(best, (result, R))

answer = best[0] * best[1]
print(answer)
