from aocd import get_data

inp = get_data(day=22, year=2022)

import re


def wrap(row, col, heading, grid):
  if (row, col) in grid:
    return row, col, heading
  
  if heading == '>':
    col = min(c for r, c in grid if r == row)
  elif heading == '<':
    col = max(c for r, c in grid if r == row)
  elif heading == '^':
    row = max(r for r, c in grid if c == col)
  elif heading == 'v':
    row = min(r for r, c in grid if c == col)
  
  return row, col, heading


def get_password(grid, path, wrap_fn):
  turn_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
  }
  turn_left = {
    '^': '<',
    '>': '^',
    'v': '>',
    '<': 'v',
  }

  row = min(r for (r, _), value in grid.items() if value == '.')
  col = min(c for (r, c), value in grid.items() if value == '.' and r == row)
  heading = '>'
  for op in path:
    if op.isdigit():
      for _ in range(int(op)):
        row2, col2, heading2 = wrap_fn(
          row + (heading == 'v') - (heading == '^'),
          col + (heading == '>') - (heading == '<'),
          heading,
          grid
        )
        if grid[(row2, col2)] == '#':
          break
        row, col, heading = row2, col2, heading2
    elif op == 'R':
      heading = turn_right[heading]
    elif op == 'L':
      heading = turn_left[heading]

  return 1000 * (row + 1) + 4 * (col + 1) + '>v<^'.index(heading)


grid, path = inp.split('\n\n')
grid = {(row, col): c for row, line in enumerate(grid.splitlines()) for col, c in enumerate(line) if c != ' '}
path = re.findall(r'\d+|.', path)

answer = get_password(grid, path, wrap)
print(answer)

def wrap_cube(row, col, heading, grid):
  if (row, col) in grid:
    return row, col, heading
  
  if row == -1 and col < 100 and heading == '^':
    return 150 + col - 50, 0, '>'
  
  if col == 49 and row < 50 and heading == '<':
    return 149 - row, 0, '>'
  
  if row == -1 and col >= 100 and heading == '^':
    return 199, col - 100, '^'
  
  if col == 150 and heading == '>':
    return 149 - row, 99, '<'

  if row == 50 and col >= 100 and heading == 'v':
    return 50 + (col - 100), 99, '<'

  if col == 49 and row >= 50 and heading == '<':
    return 100, (row - 50), 'v'

  if col == 100 and row < 100 and heading == '>':
    return 49, 100 + (row - 50), '^'

  if row == 99 and col < 50 and heading == '^':
    return 50 + col, 50, '>'

  if col == -1 and row < 150 and heading == '<':
    return 49 - (row - 100), 50, '>'

  if col == 100 and row >= 100 and heading == '>':
    return 49 - (row - 100), 149, '<'

  if row == 150 and col >= 50 and heading == 'v':
    return 150 + (col - 50), 49, '<'

  if col == -1 and row >= 150 and heading == '<':
    return 0, 50 + (row - 150), 'v'

  if col == 50 and row >= 150 and heading == '>':
    return 149, 50 + (row - 150), '^'

  if row == 200 and heading == 'v':
    return 0, 149 - (col), 'v'


answer = get_password(grid, path, wrap_cube)
print(answer)
