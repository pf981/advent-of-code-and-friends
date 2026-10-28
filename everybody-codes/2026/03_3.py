import re

with open("./2026/input/everybody_codes_e2026_q03_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """ISO2-3 23
# ISO2-61 149
# ISO2-978 99
# ISO2-5887 5923
# ISO2-76988 123749
# ISO2-435657 929977
# ISO2-3949 870737""".splitlines()


def calc(left, right):
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
        if calc(left, right_list) == num:
            return right_list
        right += 1


answer = 0
for line in lines:
    left, right = re.findall("\d+", line)[1:]
    left = list(map(int, left))
    right = list(map(int, right))

    left = left * 20
    left = left[-len(right) :]

    num = calc(left, right)

    smallest = get_smallest(num, left)
    if right == smallest:
        answer += num
    print(f"{left=} {right=} {num=} {smallest=}")

print(answer)
