from aocd import get_data

inp = get_data(day=12, year=2022)

import string
import collections

def find_shortest(starts, target, m):
  queue = collections.deque((start, 0) for start in starts)
  visited = set()
  while queue:
    pos, steps = queue.popleft()
    if pos == target:
      return steps
    
    if pos in visited:
      continue
    visited.add(pos)
    
    for direction in 'NESW':
      pos2 = (
        pos[0] + (direction == 'S') - (direction == 'N'),
        pos[1] + (direction == 'E') - (direction == 'W')
      )
      if pos2 not in m or m[pos2] > m[pos] + 1:
        continue
      queue.append((pos2, steps + 1))

  return float('inf')


grid = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
start = next(p for p, c in grid.items() if c == 'S')
target = next(p for p, c in grid.items() if c == 'E')
m = {p: string.ascii_lowercase.index(c) for p, c in grid.items() if c not in 'SE'}
m[start] = 0
m[target] = 25

answer = find_shortest([start], target, m)
print(answer)

answer = find_shortest([start for start, elevation in m.items() if elevation == 0], target, m)
print(answer)
