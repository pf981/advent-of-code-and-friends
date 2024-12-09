from aocd import get_data, submit
import itertools
import re


def get_steps(pos):
    it = itertools.cycle(instructions)
    steps = 0
    while pos[-1] != 'Z':
        pos = m[pos][next(it) == 'R']
        steps += 1

    return steps


inp = get_data(day=8, year=2023)
instructions, m = inp.split('\n\n')
m = {pos: (left, right) for pos, left, right in [re.findall(r'[A-Z0-9]{3}', line) for line in m.splitlines()]}
answer1 = get_steps('AAA')
print(answer1)

submit(answer1, part='a', day=8, year=2023)


# Part 2


import math


steps = [get_steps(start_pos) for start_pos in m if start_pos[-1] == 'A']
answer2 = math.lcm(*steps)
print(answer2)

submit(answer2, part='b', day=8, year=2023)
