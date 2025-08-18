from aocd import get_data

inp = get_data(day=20, year=2021)

import collections
import copy


def step(img, algorithm):
  img = copy.deepcopy(img)
  
  (min_row, max_row), (min_col, max_col) = [(min(dim), max(dim)) for dim in zip(*img)]
  
  new_default = '#' if img.__missing__(None) == '.' else '.'
  new_img = collections.defaultdict(lambda: new_default)
  
  for row in range(min_row - 3, max_row + 4):
    for col in range(min_col - 3, max_col + 4):
      binary = ''.join(
        '0' if img[(row + dr, col + dc)] == '.' else '1'
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
      )
      new_img[(row, col)] = algorithm[int(binary, 2)]
      
  return new_img


def count_lit(img, algorithm, n_steps):
  for _ in range(n_steps):
    img = step(img, algorithm)
  return sum(value == '#' for value in img.values())


algorithm, input_img = inp.split('\n\n')
input_img = collections.defaultdict(
  lambda: '.',
  {(row, col): value for row, line in enumerate(input_img.splitlines()) for col, value in enumerate(line)}
)

answer = count_lit(input_img, algorithm, 2)
print(answer)

answer = count_lit(input_img, algorithm, 50)
print(answer)
