from aocd import get_data

inp = get_data(day=19, year=2017)

import collections
import string

def get_path(m, letters, start_col):
  possible_directions = {
    'up': ('up', 'left', 'right'),
    'down': ('down', 'left', 'right'),
    'left': ('left', 'up', 'down'),
    'right': ('right', 'up', 'down')
  }
  
  row = -1
  col = start_col
  directions = list(possible_directions['down'])
  path = ''

  while directions:
    direction = directions.pop(0)
    new_row = row + (direction == 'down') - (direction == 'up')
    new_col = col + (direction == 'right') - (direction == 'left')

    if m[(new_row, new_col)]:
      path += letters[(new_row, new_col)] 
      row = new_row
      col = new_col
      directions = list(possible_directions[direction])
  return path


letters = collections.defaultdict(lambda: '-')
m = collections.defaultdict(bool)
start_col = None

for row, line in enumerate(inp.split('\n')):
  for col, c in enumerate(line):
    if c != ' ':
      start_col = start_col or col
      m[(row, col)] = True
      if c in string.ascii_uppercase:
        letters[(row, col)] = c
        
path = get_path(m, letters, start_col)

answer = path.replace('-', '')
print(answer)

answer = len(path)
answer
