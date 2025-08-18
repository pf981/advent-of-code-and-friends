from aocd import get_data

inp = get_data(day=25, year=2021)

import itertools

nrows = len(inp.splitlines())
ncols = len(inp.splitlines()[0])


def step(h):
  next_h = h.copy()
  for (row, col), value in h.items():
    if value == '>' and (row, (col + 1) % ncols) not in h:
      next_h[(row, (col + 1) % ncols)] = '>'
      del next_h[(row, col)]
      
  h = next_h
  next_h = h.copy()
  for (row, col), value in h.items():
    if value == 'v' and ((row + 1) % nrows, col) not in h:
      next_h[((row + 1) % nrows, col)] = 'v'
      del next_h[(row, col)]

  return next_h


h = {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line) if value != '.'}

for step_i in itertools.count(1):
  h_prev = h.copy()
  h = step(h)
  if h_prev == h:
    break

answer = step_i
print(answer)

# No puzzle here - just need 49 stars.
