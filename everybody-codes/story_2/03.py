import re
import sys


sys.setrecursionlimit(150000)


def parse_rolls(text: str, n_rolls: int) -> list[list[int]]:
    all_rolls = []
    for line in text.splitlines():
        match = re.match(r"[0-9]+: faces=\[(.+)\] seed=([0-9]+)", line)
        assert match
        g = match.groups()
        dice = [int(num) for num in g[0].split(",")]
        pulse = seed = int(g[1])

        face = 0
        rolls = []

        for roll_number in range(1, n_rolls + 1):
            spin = roll_number * pulse
            pulse = pulse + spin
            pulse = pulse % seed
            pulse = pulse + 1 + roll_number + seed
            face = (face + spin) % len(dice)
            rolls.append(dice[face])

        all_rolls.append(rolls)

    return all_rolls


with open("./story_2/input/everybody_codes_e2_q03_p1.txt") as f:
    text = f.read()

all_rolls = parse_rolls(text, 1_000)
total = answer1 = 0
for group_roll in zip(*all_rolls):
    total += sum(group_roll)
    answer1 += 1
    if total >= 10000:
        break

print(answer1)


# Part 2


with open("./story_2/input/everybody_codes_e2_q03_p2.txt") as f:
    text = f.read()

dice_str, track_str = text.split("\n\n")
track = [int(x) for x in track_str]
all_rolls = parse_rolls(dice_str, 50_000)

track_pos = [0] * len(all_rolls)
finishes = []  # [(finish_time, dice_i), ...]
for dice_i, rolls in enumerate(all_rolls, 1):
    finish_time = 0
    for track_value in track:
        while rolls[finish_time] != track_value:
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

nrows = len(grid)
ncols = len(grid[0])

all_rolls = parse_rolls(dice_str, nrows * ncols * 3)

good = set()  # {(r, c), ..}
seen = set()  # {(r, c, dice_i, roll_i), ...}


def dfs(r: int, c: int, dice_i: int, roll_i: int) -> None:
    if (r, c, dice_i, roll_i) in seen:
        return
    seen.add(((r, c, dice_i, roll_i)))
    if not (0 <= r < nrows and 0 <= c < ncols):
        return

    assert roll_i != len(all_rolls[dice_i])

    if grid[r][c] != all_rolls[dice_i][roll_i]:
        return

    good.add((r, c))
    roll_i += 1
    dfs(r + 1, c, dice_i, roll_i)
    dfs(r - 1, c, dice_i, roll_i)
    dfs(r, c + 1, dice_i, roll_i)
    dfs(r, c - 1, dice_i, roll_i)
    dfs(r, c, dice_i, roll_i)


for dice_i in range(len(all_rolls)):
    for r in range(nrows):
        for c in range(ncols):
            dfs(r, c, dice_i, 0)

answer3 = len(good)
print(answer3)
