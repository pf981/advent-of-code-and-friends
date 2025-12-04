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

answer1 = 0
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
    answer1 += nei < 4
print(answer1)

submit(answer1, part="a", day=4, year=2025)
# 924 not right
