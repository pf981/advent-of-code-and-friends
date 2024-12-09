from aocd import get_data, submit
import re


def extract_cubes(line):
    return [extract_max(line, color) for color in ['red', 'green', 'blue']]


def extract_max(line, c):
    return max(int(num) for num in re.findall(r'(\d+) ' + c, line))


inp = get_data(day=2, year=2023)
min_cubes = [extract_cubes(line) for line in inp.splitlines()]
answer1 = sum(i * (cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14) for i, cubes in enumerate(min_cubes, 1))
print(answer1)

submit(answer1, part='a', day=2, year=2023)


# Part 2


import math


answer2 = sum(math.prod(cubes) for cubes in min_cubes)
print(answer2)

submit(answer2, part='b', day=2, year=2023)
