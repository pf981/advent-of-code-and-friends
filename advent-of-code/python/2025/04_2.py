from aocd import get_data, submit


inp = get_data(day=4, year=2025)

# inp = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

lines = inp.splitlines()
ats = {(r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "@"}
dots = {
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "."
}

answer2 = 0
while True:
    # print("X")
    l = len(ats)
    to_pop = []
    for r, c in ats:
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
            nei += (r2, c2) in ats
        if nei < 4:
            to_pop.append((r, c))
        answer2 += nei < 4

    # print(to_pop)
    for p in to_pop:
        ats.discard(p)
    if len(ats) == l:
        break
print(answer2)

submit(answer2, part="b", day=4, year=2025)
# 924 not right
