from aocd import get_data

inp = get_data(day=18, year=2019)

import collections
import heapq
import string

def solve(coords):
  visited = set()
  target_n_keys = sum(key in string.ascii_lowercase for key in coords.values())
  states = [(0, next(pos for pos, value in coords.items() if value == '@'), '@', frozenset())]
  
  while states:
    d, (row, col), value, keys = heapq.heappop(states)
    
    if (row, col, keys) in visited:
      continue
    visited.add((row, col, keys))
    
    # Key
    if value in string.ascii_lowercase:
      keys = keys.union({value})
      if len(keys) == target_n_keys:
        return d
    
    # Lock
    if value in string.ascii_uppercase:
      if value.lower() not in keys:
        continue
        
    for direction in 'NESW':
      new_row = row + (direction == 'S') - (direction == 'N')
      new_col = col + (direction == 'E') - (direction == 'W')
      new_value = coords[(new_row, new_col)]

      if new_value != '#':
        heapq.heappush(states, (d + 1, (new_row, new_col), new_value, keys))


coords = collections.defaultdict(lambda: '#', {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line)})

answer = solve(coords)
print(answer)

from operator import le, ge

coords2 = coords.copy()
mid = [dimension // 2 for dimension in max(coords2.keys())]

for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
  coords2[(mid[0] + dr, mid[1] + dc)] = '@'

for dr, dc in ((-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)):
  coords2[(mid[0] + dr, mid[1] + dc)] = '#'

quadrants = [{(row, col): value for (row, col), value in coords2.items() if f_row(row, mid[0]) and f_col(col, mid[1])}
             for f_row, f_col in [(le, le), (le, ge), (ge, le), (ge, ge)]]

# Remove locks where the key is in a different quadrant
quadrants = [{pos: value if value.lower() in quadrant.values() else '.' for pos, value in quadrant.items()}
             for quadrant in quadrants]

answer = sum(solve(quadrant) for quadrant in quadrants)
print(answer)
