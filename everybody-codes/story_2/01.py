import functools
import itertools


@functools.cache
def get_coins(instructions: str, toss_slot: int, board: tuple[str]) -> int:
    nrows = len(board)
    ncols = len(board[0])

    c = 2 * (toss_slot - 1)
    r = 0
    for move in instructions:
        while r < nrows and board[r][c] != "*":
            r += 1
        if r == nrows:
            break
        c += (move == "R") - (move == "L")
        if c == ncols:
            c = ncols - 2
        if c == -1:
            c = 1

    final_slot = c // 2 + 1
    coins_won = max(2 * final_slot - toss_slot, 0)
    return coins_won


with open("./story_2/input/everybody_codes_e2_q01_p1.txt") as f:
    text = f.read()

board_str, instructions_str = text.split("\n\n")
board = tuple(board_str.splitlines())
instructions_list = instructions_str.splitlines()
answer1 = 0

for toss_slot, instructions in enumerate(instructions_list, 1):
    answer1 += get_coins(instructions, toss_slot, board)

print(answer1)


# Part 2


with open("./story_2/input/everybody_codes_e2_q01_p2.txt") as f:
    text = f.read()

board_str, instructions_str = text.split("\n\n")
board = tuple(board_str.splitlines())
instructions_list = instructions_str.splitlines()
max_slot = len(board[0]) // 2 + 2
answer2 = 0

for i, instructions in enumerate(instructions_list):
    max_coins_won = 0
    for toss_slot in range(1, max_slot):
        max_coins_won = max(max_coins_won, get_coins(instructions, toss_slot, board))
    answer2 += max_coins_won

print(answer2)


# Part 3


with open("./story_2/input/everybody_codes_e2_q01_p3.txt") as f:
    text = f.read()

board_str, instructions_str = text.split("\n\n")
board = tuple(board_str.splitlines())
instructions_list = instructions_str.splitlines()
max_slot = len(board[0]) // 2 + 2
balls = len(instructions_list)

max_coins_won = 0
min_coins_won = float("inf")
for perm in itertools.permutations(range(1, max_slot), balls):
    coins_won = 0
    for i, slot in enumerate(perm):
        coins_won += get_coins(instructions_list[i], slot, board)
    max_coins_won = max(max_coins_won, coins_won)
    min_coins_won = min(min_coins_won, coins_won)

answer3 = f"{min_coins_won} {max_coins_won}"
print(answer3)
