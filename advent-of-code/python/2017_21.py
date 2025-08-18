from aocd import get_data

inp = get_data(day=21, year=2017)

import numpy as np

def str_to_np(s):
  nrows = s.count('/') + 1
  return np.array([c == '#' for c in s.replace('/', '')]).reshape(nrows, nrows)

def split(grid):
  size = grid.shape[0]
  split_size = size / (2 if size % 2 == 0 else 3)
  return [np.hsplit(g, split_size) for g in np.vsplit(grid, split_size)]

def expand(grid, rules):
  return rules[grid.tobytes()]
  
def combine(grids):
  return np.vstack([np.hstack(row) for row in grids])

def solve(rules, iterations):
  grid = str_to_np('.#./..#/###')
  for _ in range(iterations):
    grid = combine([expand(g, rules) for g in row] for row in split(grid))
  return grid.sum()


rules = {}
for line in inp.split('\n'):
  a, b = (str_to_np(s) for s in line.split(' => '))
  rules[a.tobytes()] = b
  rules[np.flipud(a).tobytes()] = b
  rules[np.fliplr(a).tobytes()] = b
  rules[np.rot90(a, k=1).tobytes()] = b
  rules[np.rot90(a, k=2).tobytes()] = b
  rules[np.rot90(a, k=3).tobytes()] = b
  rules[np.fliplr(np.rot90(a, k=1)).tobytes()] = b
  rules[np.fliplr(np.rot90(a, k=2)).tobytes()] = b
  rules[np.fliplr(np.rot90(a, k=3)).tobytes()] = b


answer = solve(rules, 5)
print(answer)

answer = solve(rules, 18)
print(answer)
