import itertools
import math
import re


with open("./story_1/input/everybody_codes_e1_q03_p1.txt") as f:
    lines = f.read().splitlines()

answer1 = 0
for line in lines:
    x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))

    for _ in range(100):
        x += 1
        y -= 1
        if y == 0:
            y = x - y - 1
            x = 1

    answer1 += x + 100 * y

print(answer1)


# Part 2


with open("./story_1/input/everybody_codes_e1_q03_p2.txt") as f:
    lines = f.read().splitlines()


# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


nums = []
remainders = []
for i, line in enumerate(lines):
    x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))

    cycle_start = None
    for day in itertools.count():
        if y == 1:
            if cycle_start is None:
                cycle_start = day
            else:
                break
        x += 1
        y -= 1
        if y == 0:
            y = x - y - 1
            x = 1

    cycle_length = day - cycle_start

    nums.append(cycle_length)
    remainders.append(cycle_start)

answer2 = chinese_remainder(nums, remainders)
print(answer2)


# Part 3


with open("./story_1/input/everybody_codes_e1_q03_p3.txt") as f:
    lines = f.read().splitlines()

nums = []
remainders = []
for i, line in enumerate(lines):
    x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))

    cycle_start = None
    for day in itertools.count():
        if y == 1:
            if cycle_start is None:
                cycle_start = day
            else:
                break
        x += 1
        y -= 1
        if y == 0:
            y = x - y - 1
            x = 1

    cycle_length = day - cycle_start

    nums.append(cycle_length)
    remainders.append(cycle_start)

answer3 = chinese_remainder(nums, remainders)
print(answer3)
