import collections
import itertools
import re

from collections.abc import Generator


def die(faces: list[int], seed: int) -> Generator[int, None, None]:
    pulse = seed
    face = 0
    for roll_number in itertools.count(1):
        spin = roll_number * pulse
        pulse += spin
        pulse %= seed
        pulse += 1 + roll_number + seed
        face = (face + spin) % len(faces)
        yield faces[face]


def parse_dice(text: str) -> list[Generator[int, None, None]]:
    dice = []
    for line in text.splitlines():
        match = re.match(r"[0-9]+: faces=\[(.+)\] seed=([0-9]+)", line)
        assert match
        g = match.groups()
        faces = [int(num) for num in g[0].split(",")]
        seed = int(g[1])
        dice.append(die(faces, seed))
    return dice


with open("./story_2/input/everybody_codes_e2_q03_p1.txt") as f:
    text = f.read()

dice = parse_dice(text)

total = answer1 = 0
for group_roll in zip(*dice):
    total += sum(group_roll)
    answer1 += 1
    if total >= 10_000:
        break

print(answer1)


# Part 2


with open("./story_2/input/everybody_codes_e2_q03_p2.txt") as f:
    text = f.read()

dice_str, track_str = text.split("\n\n")
track = [int(x) for x in track_str]
dice = parse_dice(dice_str)

track_pos = [0] * len(dice)
finishes = []  # [(finish_time, dice_i), ...]
for dice_i, cur_die in enumerate(dice, 1):
    finish_time = 0
    for track_value in track:
        while next(cur_die) != track_value:
            finish_time += 1
        finish_time += 1
    finishes.append((finish_time, dice_i))

finishes.sort()
answer2 = ",".join(str(dice_i) for _, dice_i in finishes)
print(answer2)


# Part 3

with open("./story_2/input/everybody_codes_e2_q03_p3.txt") as f:
    text = f.read()

dice_str, grid_str = text.split("\n\n")
grid = [[int(num) for num in line] for line in grid_str.splitlines()]
dice = parse_dice(dice_str)

nrows = len(grid)
ncols = len(grid[0])

nodes = collections.defaultdict(set)  # dice_i -> {(r, c), ...}
for dice_i in range(len(dice)):
    val = next(dice[dice_i])
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == val:
                nodes[dice_i].add((r, c))

good = set()  # {(r, c), ..}
while nodes:
    next_nodes = collections.defaultdict(set)
    for dice_i, positions in nodes.items():
        val = next(dice[dice_i])
        for r, c in positions:
            good.add((r, c))
            for dr, dc in [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc
                if not (0 <= r2 < nrows and 0 <= c2 < ncols) or grid[r2][c2] != val:
                    continue
                next_nodes[dice_i].add((r2, c2))

    nodes = next_nodes

answer3 = len(good)
print(answer3)
