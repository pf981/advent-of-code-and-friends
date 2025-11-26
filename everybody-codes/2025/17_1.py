with open("./2025/input/everybody_codes_e2025_q17_p1.txt") as f:
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

R = 10
answer = 0
for (r, c), num in grid.items():
    Xc = c
    Yc = r

    if (Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc) <= R * R:
        answer += num

print(answer)
