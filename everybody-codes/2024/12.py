import collections


def shoot(power: int) -> collections.abc.Generator[int]:
    y = 0
    yield y
    for _ in range(power):
        y += 1
        yield y
    for _ in range(power):
        yield y
    while True:
        y -= 1
        yield y


def get_y(target_x: int, power: int) -> int:
    return next((y for x, y in enumerate(shoot(power)) if x == target_x))


def power_to_hit(x: int, y: int) -> int | None:
    l = 0
    r = x
    while l <= r:
        m = (l + r) // 2
        cur_y = get_y(x, m)
        if cur_y == y:
            return m
        elif cur_y < y:
            l = m + 1
        else:
            r = m - 1
    return None


def min_ranking_to_hit(x: int, y: int) -> int:
    return min(power * (start_y + 1) for start_y in range(3) if (power := power_to_hit(x, y - start_y)) is not None)


with open("./2024/input/everybody_codes_e2024_q12_p1.txt") as f:
    lines = f.read().splitlines()

targets = [(x - 1, y - 1) for y, line in enumerate(reversed(lines)) for x, c in enumerate(line) if c == 'T']
answer1 = sum(min_ranking_to_hit(x, y) for x, y in targets)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q12_p2.txt") as f:
    lines = f.read().splitlines()

targets = []
for y, line in enumerate(reversed(lines)):
    for x, c in enumerate(line):
        if c == 'T':
            targets.append((x - 1, y - 1))
        elif c == 'H':
            targets.append((x - 1, y - 1))
            targets.append((x - 1, y - 1))

answer2 = sum(min_ranking_to_hit(x, y) for x, y in targets)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q12_p3.txt") as f:
    lines = f.read().splitlines()

meteors = [[int(num) for num in line.split()] for line in lines]

answer3 = 0
for meteor_x, meteor_y in meteors:
    x_hit = meteor_x // 2
    y_hit = meteor_y - (meteor_x - x_hit)
    answer3 += min_ranking_to_hit(x_hit, y_hit)

print(answer3)
