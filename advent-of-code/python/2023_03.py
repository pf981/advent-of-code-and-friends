from aocd import get_data, submit
import dataclasses


@dataclasses.dataclass(frozen=True)
class Number:
    row: int
    start_col: int
    end_col: int
    value: int


def get_number(pos, digits):
    start_col = pos[1]
    while (pos[0], start_col - 1) in digits:
        start_col -= 1

    end_col = pos[1]
    while (pos[0], end_col + 1) in digits:
        end_col += 1

    return Number(
        row=pos[0],
        start_col=start_col,
        end_col=end_col,
        value=int(''.join(digits[pos[0], col] for col in range(start_col, end_col + 1)))
    )


inp = get_data(day=3, year=2023)
m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
symbols = {pos for pos, c in m.items() if c not in '0123456789.'}
digits = {pos: c for pos, c in m.items() if c in '0123456789'}

numbers = {}
for pos, c in digits.items():
    if pos in numbers:
        continue

    number = get_number(pos, digits)
    for col in range(number.start_col, number.end_col + 1):
        numbers[(number.row, col)] = number

valid_numbers = {numbers[(row + dr, col + dc)] for row, col in symbols for dr in range(-1, 2) for dc in range(-1, 2) if (row + dr, col + dc) in numbers}
answer1 = sum(number.value for number in valid_numbers)
print(answer1)

submit(answer1, part='a', day=3, year=2023)


# Part 2


import math


gears = {pos for pos, c in m.items() if c == '*'}
gear_ratios = 0
for row, col in gears:
    neighbors = {numbers[row + dr, col + dc] for dr in range(-1, 2) for dc in range(-1, 2) if (row + dr, col + dc) in numbers}
    if len(neighbors) == 2:
        gear_ratios += math.prod(number.value for number in neighbors)

answer2 = gear_ratios
print(answer2)

submit(answer2, part='b', day=3, year=2023)
