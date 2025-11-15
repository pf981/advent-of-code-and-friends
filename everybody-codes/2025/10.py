import functools


with open("./2025/input/everybody_codes_e2025_q10_p1.txt") as f:
    lines = f.read().splitlines()

sheep = set()
dragon = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        match ch:
            case "D":
                dragon = (r, c)
            case "S":
                sheep.add((r, c))
assert dragon

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

answer1 = sum((r, c) in seen for r, c in sheep)
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q10_p2.txt") as f:
    lines = f.read().splitlines()
rounds = 20

sheep = set()
hideouts = set()
dragon = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        match ch:
            case "D":
                dragon = (r, c)
            case "S":
                sheep.add((r, c))
            case "#":
                hideouts.add((r, c))
assert dragon

dragons = {dragon}
answer2 = 0
for rnd in range(rounds + 1):
    if rnd > 0:
        for r, c in sheep.copy():
            if (r + rnd - 1, c) in dragons:
                if (r + rnd - 1, c) in hideouts:
                    continue
                sheep.discard((r, c))
                answer2 += 1

    for r, c in sheep.copy():
        if (r + rnd, c) in dragons:
            if (r + rnd, c) in hideouts:
                continue
            sheep.discard((r, c))
            answer2 += 1

    dragons2 = set()
    for r, c in dragons:
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

            dragons2.add((r2, c2))
    dragons = dragons2

print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q10_p3.txt") as f:
    lines = f.read().splitlines()

sheep = set()
hideouts = set()
valid = set()
dragon = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        match ch:
            case "D":
                dragon = (r, c)
            case "S":
                sheep.add((r, c))
            case "#":
                hideouts.add((r, c))
        valid.add((r, c))
assert dragon

target = frozenset(sheep)
sheep_cols = [c for _, c in sheep]
nrows = len(lines)


@functools.cache
def count_ways(r, c, sheep_rows):
    # Eat
    sheep_rows = list(sheep_rows)
    if (r, c) not in hideouts:
        for i, (r2, c2) in enumerate(zip(sheep_rows, sheep_cols)):
            if (r2, c2) == (r, c):
                sheep_rows[i] = None
    sheep_rows = tuple(sheep_rows)

    # Check
    if any(r_sheep == nrows for r_sheep in sheep_rows):
        return 0
    if all(r_sheep is None for r_sheep in sheep_rows):
        return 1

    # Sheep move
    next_sheep_rows = []
    for i, (r2, c2) in enumerate(zip(sheep_rows, sheep_cols)):
        if r2 is None:  # Already eaten
            continue
        if (r, c) not in hideouts and (r2 + 1, c2) == (r, c):  # Would be eaten
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

    return result


answer3 = count_ways(*dragon, tuple([0] * len(sheep_cols)))
print(answer3)
