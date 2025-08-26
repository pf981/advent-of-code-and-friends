import functools
from typing import Literal


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
max_slot = len(board[0]) // 2 + 1
answer2 = 0

for i, instructions in enumerate(instructions_list):
    max_coins_won = 0
    for toss_slot in range(1, max_slot + 1):
        max_coins_won = max(max_coins_won, get_coins(instructions, toss_slot, board))
    answer2 += max_coins_won

print(answer2)


# Part 3


with open("./story_2/input/everybody_codes_e2_q01_p3.txt") as f:
    text = f.read()

board_str, instructions_str = text.split("\n\n")
board = tuple(board_str.splitlines())
instructions_list = instructions_str.splitlines()
max_slot = len(board[0]) // 2 + 1
balls = len(instructions_list)


@functools.cache
def get_best_coins(
    i: int, used_slots: int, func_type: Literal["max"] | Literal["min"]
) -> int:
    if i == len(instructions_list):
        return 0

    if func_type == "max":
        f = max
        best_coins = 0
    else:
        f = min
        best_coins = 2 * max_slot * len(instructions_list)

    for toss_slot in range(1, max_slot + 1):
        mask = 1 << toss_slot
        if used_slots & mask == 0:
            best_coins = f(
                best_coins,
                get_coins(instructions_list[i], toss_slot, board)
                + get_best_coins(i + 1, used_slots | mask, func_type),
            )
    return best_coins


max_coins_won = get_best_coins(0, 0, "max")
min_coins_won = get_best_coins(0, 0, "min")

answer3 = f"{min_coins_won} {max_coins_won}"
print(answer3)
