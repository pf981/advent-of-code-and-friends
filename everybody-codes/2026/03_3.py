import re


def to_dec(left: list[int], right: list[int]) -> int:
    exponent = len(right) - 1
    num = 0
    for a, b in zip(right, left):
        num += a * (b**exponent)
        exponent -= 1
    return num


def get_smallest(num, left):
    right = 0
    while True:
        right_list = list(map(int, "0" * 20 + str(right)))
        right_list = right_list[-len(left) :]
        if to_dec(left, right_list) == num:
            return right_list
        right += 1


with open("./2026/input/everybody_codes_e2026_q03_p3.txt") as f:
    lines = f.read().splitlines()


answer = 0
for line in lines:
    left, right = re.findall(r"\d+", line)[1:]
    left = list(map(int, left))
    right = list(map(int, right))

    left = left * 20
    left = left[-len(right) :]

    num = to_dec(left, right)

    if right == get_smallest(num, left):
        answer += num

print(answer)
