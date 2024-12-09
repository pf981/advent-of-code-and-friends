from aocd import get_data

inp = get_data(day=13, year=2021)

import collections


def do_fold(dots, along, position):
  result = set()
  max_x, max_y = [max(dim) + 1 for dim in zip(*dots)]
  max_x = position if along == 'x' else max_x
  max_y = position if along == 'y' else max_y
  
  for y in range(max_y):
    for x in range(max_x):
      if (
        (x, y) in dots or
        (along == 'x' and (2 * position - x, y) in dots) or
        (along == 'y' and (x, 2 * position - y) in dots)
      ):
        result.add((x, y))

  return result


dots, folds = inp.split('\n\n')
dots = {tuple(int(coord) for coord in line.split(',')) for line in dots.splitlines()}
folds = [(lhs[-1], int(rhs)) for lhs, rhs in [line.split('=') for line in folds.splitlines()]]

answer = len(do_fold(dots, *folds[0]))
print(answer)

for along, position in folds:
  dots = do_fold(dots, along, position)

max_x, max_y = [max(dim) + 1 for dim in zip(*dots)]
for y in range(max_y):
  for x in range(max_x):
    print('#' if (x, y) in dots else ' ', end='')
  print()

answer = 'UCLZRAZU'
print(answer)
