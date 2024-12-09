from aocd import get_data

inp = get_data(day=2, year=2017)

import re

sheet = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.split('\n')]

answer = sum(max(nums) - min(nums) for nums in sheet)
answer

import itertools

answer = sum(next(a // b for a, b in itertools.permutations(nums, 2) if a % b == 0) for nums in sheet)
answer
