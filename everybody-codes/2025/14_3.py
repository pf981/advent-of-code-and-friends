with open("./2025/input/everybody_codes_e2025_q14_p3.txt") as f:
    lines = f.read().splitlines()

# 1_000_000_000

lines = """#......#
..#..#..
.##..##.
...##...
...##...
.##..##.
..#..#..
#......#""".splitlines()


# x = """#......#.#..#..####..#..#.#......#
# .####.#.#......#..#......#.#.####.
# .#.####.###..#.####.#..###.####.#.
# .##..#...##.##.####.##.##...#..##.
# .##....##..##.######.##..##....##.
# ..##.##.#..##.#.##.#.##..#.##.##..
# .##..#.#...#.##....##.#...#.#..##.
# #...#.##..##..#....#..##..##.#...#
# .##.##..###.#........#.###..##.##.
# #.##....##.###.#..#.###.##....##.#
# ..##...##...###....###...##...##..
# ....####.#..#.#....#.#..#.####....
# #..###..######.####.######..###..#
# ..##..#..##.##......##.##..#..##..
# ....####..##...#..#...##..####....
# #####....#..#.##..##.#..#....#####
# #.####......#...##...#......####.#
# #.####......#...##...#......####.#
# #####....#..#.##..##.#..#....#####
# ....####..##...#..#...##..####....
# ..##..#..##.##......##.##..#..##..
# #..###..######.####.######..###..#
# ....####.#..#.#....#.#..#.####....
# ..##...##...###....###...##...##..
# #.##....##.###.#..#.###.##....##.#
# .##.##..###.#........#.###..##.##.
# #...#.##..##..#....#..##..##.#...#
# .##..#.#...#.##....##.#...#.#..##.
# ..##.##.#..##.#.##.#.##..#.##.##..
# .##....##..##.######.##..##....##.
# .##..#...##.##.####.##.##...#..##.
# .#.####.###..#.####.#..###.####.#.
# .####.#.#......#..#......#.#.####.
# #......#.#..#..####..#..#.#......#""".splitlines()

# nrows = len(lines)
# ncols = len(lines[0])
n = 34


def sim(active):
    result = set()
    for r in range(n):
        for c in range(n):
            active_diags = 0

            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                r2 = r + dr
                c2 = c + dc
                active_diags += (r2, c2) in active

            if (r, c) in active:
                if active_diags % 2 == 1:
                    result.add((r, c))
            else:
                if active_diags % 2 == 0:
                    result.add((r, c))

    return result


def does_match_pattern(active):
    # print(active)
    r_start, c_start = (13, 13)
    for dr in range(len(lines)):
        for dc in range(len(lines[0])):
            r = r_start + dr
            c = c_start + dc

            # print(".#"[(r, c) in active], end="")
            # print(r, c)

            if lines[dr][dc] == "#":
                if (r, c) not in active:
                    return False
            else:
                if (r, c) in active:
                    return False
        # print()

    return True


# for r, line in enumerate(x):
#     print(line)

# tmp = {(r, c) for r, line in enumerate(x) for c, ch in enumerate(line) if ch == "#"}
# does_match_pattern(tmp)

active = set()  # {(r, c), ...}
result = []  # [rnd, ...]
sum_active = []

# for rnd in range(1, 125 + 1):
for rnd in range(1, 10_000 + 1):
    active = sim(active.copy())
    if does_match_pattern(active):
        s = len(active)
        print(rnd, s)
        result.append(rnd)
        sum_active.append(s)
print(result)

for a, b in zip(result[:-1], result[1:]):
    print(a, b, a - b)

first_hit = 125
d1 = 892
d2 = 3203
s1 = 552
s2 = 588

target_round = 1000000000

times = (target_round - first_hit) // (d1 + d2)

ans = times * (s1 + s2)  # This is too big!

remaining = target_round - (first_hit + times * (d1 + d2))
if remaining >= d1:
    ans += s1
    remaining -= d1
if remaining >= d2:
    ans += s2
    remaining -= d2

print(ans)

# 278388552
# 278388000

# 278388000 + s1

# answer = 0
# print(answer)
