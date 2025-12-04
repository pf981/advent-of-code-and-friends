from aocd import get_data, submit


inp = get_data(day=4, year=2025)

lines = inp.splitlines()
rolls = {
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "@"
}

answer2 = 0
while True:
    to_remove = []
    for r, c in rolls:
        nei = 0
        for dr, dc in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]:
            r2 = r + dr
            c2 = c + dc
            nei += (r2, c2) in rolls
        if nei < 4:
            to_remove.append((r, c))
            answer2 += 1

    if not to_remove:
        break

    for pos in to_remove:
        rolls.discard(pos)

submit(answer2, part="b", day=4, year=2025)
