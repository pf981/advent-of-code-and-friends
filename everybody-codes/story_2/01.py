with open("./story_2/input/everybody_codes_e2_q01_p1.txt") as f:
    text = f.read()

text = """*.*.*.*.*.*.*.*.*
.*.*.*.*.*.*.*.*.
*.*.*...*.*...*..
.*.*.*.*.*...*.*.
*.*.....*...*.*.*
.*.*.*.*.*.*.*.*.
*...*...*.*.*.*.*
.*.*.*.*.*.*.*.*.
*.*.*...*.*.*.*.*
.*...*...*.*.*.*.
*.*.*.*.*.*.*.*.*
.*.*.*.*.*.*.*.*.

RRRLRLRRRRRL
LLLLRLRRRRRR
RLLLLLRLRLRL
LRLLLRRRLRLR
LLRLLRLLLRRL
LRLRLLLRRRRL
LRLLLLLLRLLL
RRLLLRLLRLRR
RLLLLLRLLLRL"""

board_str, inst = text.split("\n\n")
board = board_str.splitlines()
nrows = len(board)
ncols = len(board[0])
answer1 = 0
for i, line in enumerate(inst.splitlines()):
    c = 2 * i
    r = 0
    for move in line:
        # print(f"{r=} {c=} {move=} {line=}")
        while r < nrows and board[r][c] != "*":
            r += 1
        if r == nrows:
            break
        c += (move == "R") - (move == "L")
        if c == ncols:
            c = ncols - 2
        if c == -1:
            c = 1

    toss_slot = i + 1
    final_slot = c // 2 + 1
    coins_won = max(2 * final_slot - toss_slot, 0)
    answer1 += coins_won
    # print(f"  {r=} {c=} {toss_slot=} {final_slot=} {coins_won=}")

# Coins Won = (final slot number * 2) - toss slot number

print(answer1)


# Part 2

with open("./story_2/input/everybody_codes_e2_q01_p2.txt") as f:
    text = f.read()

# text = """*.*.*.*.*.*.*.*.*.*.*.*.*
# .*.*.*.*.*.*.*.*.*.*.*.*.
# ..*.*.*.*...*.*...*.*.*..
# .*...*.*.*.*.*.*.....*.*.
# *.*...*.*.*.*.*.*...*.*.*
# .*.*.*.*.*.*.*.*.......*.
# *.*.*.*.*.*.*.*.*.*...*..
# .*.*.*.*.*.*.*.*.....*.*.
# *.*...*.*.*.*.*.*.*.*....
# .*.*.*.*.*.*.*.*.*.*.*.*.
# *.*.*.*.*.*.*.*.*.*.*.*.*
# .*.*.*.*.*.*.*.*.*...*.*.
# *.*.*.*.*.*.*.*.*...*.*.*
# .*.*.*.*.*.*.*.*.....*.*.
# *.*.*.*.*.*.*.*...*...*.*
# .*.*.*.*.*.*.*.*.*.*.*.*.
# *.*.*...*.*.*.*.*.*.*.*.*
# .*...*.*.*.*...*.*.*...*.
# *.*.*.*.*.*.*.*.*.*.*.*.*
# .*.*.*.*.*.*.*.*.*.*.*.*.

# RRRLLRRRLLRLRRLLLRLR
# RRRRRRRRRRLRRRRRLLRR
# LLLLLLLLRLRRLLRRLRLL
# RRRLLRRRLLRLLRLLLRRL
# RLRLLLRRLRRRLRRLRRRL
# LLLLLLLLRLLRRLLRLLLL
# LRLLRRLRLLLLLLLRLRRL
# LRLLRRLLLRRRRRLRRLRR
# LRLLRRLRLLRLRRLLLRLL
# RLLRRRRLRLRLRLRLLRRL"""


board_str, inst = text.split("\n\n")
board = board_str.splitlines()
nrows = len(board)
ncols = len(board[0])
answer2 = 0
for i, line in enumerate(inst.splitlines()):
    max_coins_won = 0
    for j in range(ncols // 2 + 1):
        c = 2 * j
        r = 0
        for move in line:
            # print(f"{r=} {c=} {move=} {line=}")
            while r < nrows and board[r][c] != "*":
                r += 1
            if r == nrows:
                break
            c += (move == "R") - (move == "L")
            if c == ncols:
                c = ncols - 2
            if c == -1:
                c = 1

        toss_slot = j + 1
        final_slot = c // 2 + 1
        coins_won = max(2 * final_slot - toss_slot, 0)
        max_coins_won = max(max_coins_won, coins_won)
        # print(f"  {r=} {c=} {toss_slot=} {final_slot=} {coins_won=}")
    # print(f"{i=} {max_coins_won=}")
    answer2 += max_coins_won


print(answer2)

# part 3

import functools
import itertools

with open("./story_2/input/everybody_codes_e2_q01_p3.txt") as f:
    text = f.read()

# text = """*.*.*.*.*.*.*.*.*
# .*.*.*.*.*.*.*.*.
# *.*.*...*.*...*..
# .*.*.*.*.*...*.*.
# *.*.....*...*.*.*
# .*.*.*.*.*.*.*.*.
# *...*...*.*.*.*.*
# .*.*.*.*.*.*.*.*.
# *.*.*...*.*.*.*.*
# .*...*...*.*.*.*.
# *.*.*.*.*.*.*.*.*
# .*.*.*.*.*.*.*.*.

# RRRLRLRRRRRL
# LLLLRLRRRRRR
# RLLLLLRLRLRL
# LRLLLRRRLRLR
# LLRLLRLLLRRL
# LRLRLLLRRRRL"""

board_str, inst = text.split("\n\n")
board = board_str.splitlines()
nrows = len(board)
ncols = len(board[0])
answer3 = 0

slots = ncols // 2 + 1
instructions_list = inst.splitlines()
balls = len(instructions_list)


@functools.cache
def get_coins(instructions, slot):
    j = slot

    c = 2 * j
    r = 0
    for move in instructions:
        # print(f"{r=} {c=} {move=} {line=}")
        while r < nrows and board[r][c] != "*":
            r += 1
        if r == nrows:
            break
        c += (move == "R") - (move == "L")
        if c == ncols:
            c = ncols - 2
        if c == -1:
            c = 1

    toss_slot = j + 1
    final_slot = c // 2 + 1
    coins_won = max(2 * final_slot - toss_slot, 0)
    return coins_won


max_coins_won = 0
min_coins_won = float("inf")
for perm in itertools.permutations(range(slots), balls):
    coins_won = 0
    for i, slot in enumerate(perm):
        coins_won += get_coins(instructions_list[i], slot)
    max_coins_won = max(max_coins_won, coins_won)
    min_coins_won = min(min_coins_won, coins_won)

answer3 = f"{min_coins_won} {max_coins_won}"
print(answer3)
