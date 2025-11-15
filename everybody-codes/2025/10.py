with open("./2025/input/everybody_codes_e2025_q10_p1.txt") as f:
    lines = f.read().splitlines()

ss = set()
dragon = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "D":
            dragon = (r, c)
        if ch == "S":
            ss.add((r, c))

seen = {dragon}
for _ in range(4):
    for r, c in list(seen):
        for dr, dc in [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]:
            r2 = r + dr
            c2 = c + dc

            if (r2, c2) in seen:
                continue
            seen.add((r2, c2))

answer = 0
for r, c in ss:
    answer += (r, c) in seen

print(answer)


# Part 2

with open("./2025/input/everybody_codes_e2025_q10_p2.txt") as f:
    lines = f.read().splitlines()
rounds = 20

# lines = """...SSS##.....
# .S#.##..S#SS.
# ..S.##.S#..S.
# .#..#S##..SS.
# ..SSSS.#.S.#.
# .##..SS.#S.#S
# SS##.#D.S.#..
# S.S..S..S###.
# .##.S#.#....S
# .SSS.#SS..##.
# ..#.##...S##.
# .#...#.S#...S
# SS...#.S.#S..""".splitlines()
# rounds = 3

ss = set()
hashes = set()
dragon = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "D":
            dragon = (r, c)
        if ch == "S":
            ss.add((r, c))
        if ch == "#":
            hashes.add((r, c))

import collections

seen = {dragon}
q = collections.deque([dragon])
answer2 = 0
for rnd in range(rounds + 1):
    s = set(q)
    # print(f"{s=}")

    if rnd > 0:
        for r, c in ss.copy():
            if (r + rnd - 1, c) in s:
                if (r + rnd - 1, c) in hashes:
                    continue
                ss.discard((r, c))
                answer2 += 1

    for r, c in ss.copy():
        if (r + rnd, c) in s:
            if (r + rnd, c) in hashes:
                continue
            ss.discard((r, c))
            answer2 += 1

    # print(f"{rnd=} {answer2=}")
    q = collections.deque(s)
    for _ in range(len(q)):
        r, c = q.popleft()
        for dr, dc in [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]:
            r2 = r + dr
            c2 = c + dc

            # if (r2, c2) in seen:
            #     continue
            # seen.add((r2, c2))
            q.append((r2, c2))

print(answer2)


# # Part 3


with open("./2025/input/everybody_codes_e2025_q10_p3.txt") as f:
    lines = f.read().splitlines()

# # Wrong
# lines = """SSS
# ..#
# #.#
# #D.""".splitlines()

# lines = """SSS
# ..#
# ..#
# .##
# .D#""".splitlines()
# lines = """..S..
# .....
# ..#..
# .....
# ..D..""".splitlines()

# # Wrong
# lines = """.SS.S
# #...#
# ...#.
# ##..#
# .####
# ##D.#""".splitlines()

ss = set()
hashes = set()
valid = set()
dragon = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "D":
            dragon = (r, c)
        if ch == "S":
            ss.add((r, c))
        if ch == "#":
            hashes.add((r, c))
        valid.add((r, c))

import functools

target = frozenset(ss)
max_rnds = len(lines) + 5
sheep_cols = [c for _, c in ss]
nrows = len(lines)
# print(f"{target=}")

visiting = set()
visited = {}


# @functools.cache
def count_ways(r, c, sheep_rows):
    t = (r, c, sheep_rows)
    if t in visited:
        return visited[t]
    if t in visiting:
        assert False
        return 0
    visiting.add(t)

    # print(f"{r=} {c=} {sheep_rows=}")

    # Eat
    sheep_rows = list(sheep_rows)
    if (r, c) not in hashes:
        for i, (r2, c2) in enumerate(zip(sheep_rows, sheep_cols)):
            if (r2, c2) == (r, c):
                sheep_rows[i] = None
    sheep_rows = tuple(sheep_rows)

    # Check
    if any(r_sheep == nrows for r_sheep in sheep_rows):
        visited[t] = 0
        return 0
    if all(r_sheep is None for r_sheep in sheep_rows):
        visited[t] = 1
        return 1

    # Sheep move
    next_sheep_rows = []
    for i, (r2, c2) in enumerate(zip(sheep_rows, sheep_cols)):
        if r2 is None:  # Already eaten
            continue
        if (r, c) not in hashes and (r2 + 1, c2) == (r, c):  # Would be eaten
            continue

        nxt = list(sheep_rows)
        nxt[i] += 1
        next_sheep_rows.append(tuple(nxt))
    if not next_sheep_rows:
        next_sheep_rows.append(sheep_rows)

    # D move
    result = 0
    for dr, dc in [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) not in valid:
            continue
        for nxt in next_sheep_rows:
            result += count_ways(r2, c2, nxt)

    # print(f"x")
    visited[t] = result
    return result


answer3 = count_ways(*dragon, tuple([0] * len(sheep_cols)))
print(answer3)

# 50174007498669
# Your answer length is: correct
# The first character of your answer is: correct


# for config, cnt in visited.items():
#     if cnt:
#         print(config, cnt)
