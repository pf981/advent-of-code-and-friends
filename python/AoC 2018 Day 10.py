from aocd import get_data

inp = get_data(day=10, year=2018)

import itertools
import numpy as np
import re

def find_smallest_var(points):
  prev_var = float("inf")
  for t in itertools.count():
    positions = [(y + t * dy, x + t * dx) for x, y, dx, dy in points]
    var = np.var(positions)
    if var > prev_var:
      return t - 1, prev_positions
    prev_var = var
    prev_positions = positions

points = [[int(x) for x in re.findall(r'-?\d+', line)] for line in inp.splitlines()]
t, positions = find_smallest_var(points)

rows, cols = zip(*positions)
for row in range(min(rows), max(rows) + 1):
  for col in range(min(cols), max(cols) + 1):
    if (row, col) in positions:
      print('#', end='')
    else:
      print(' ', end='')
  print()

answer = "XPFXXXKL"
print(answer)

answer = t
print(answer)
