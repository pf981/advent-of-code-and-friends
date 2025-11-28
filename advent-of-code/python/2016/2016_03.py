from aocd import get_data

inp = get_data(day=3, year=2016)

import re

triangles = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.split('\n')]
answer = sum(1 for a, b, c in triangles if a < b + c and b < a + c and c < a + b)
answer

valid_count = 0
for values in zip(*triangles):
  while values:
    a, b, c, *values = values
    if a < b + c and b < a + c and c < a + b:
      valid_count += 1
answer = valid_count
answer
