import re


def to_dec(left: list[int], right: list[int]) -> int:
    exponent = len(right) - 1
    num = 0
    for a, b in zip(right, left):
        num += a * (b**exponent)
        exponent -= 1
    return num


with open("./2026/input/everybody_codes_e2026_q03_p2.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    left, right = re.findall(r"\d+", line)
    left = list(map(int, left))
    right = list(map(int, right))

    left = left * 20
    left = left[-len(right) :]

    answer += to_dec(left, right)

print(answer)
