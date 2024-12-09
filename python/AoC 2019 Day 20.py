from aocd import get_data

inp = get_data(day=20, year=2019)

import collections
import heapq
import string


def parse_input(inp):
  coords = collections.defaultdict(str, {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line)})

  for (row, col), value in coords.copy().items():
    side, affix = next(
      ((side, coords[(row+dr, col+dc)])
       for side, (dr, dc) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)])
       if
        value in string.ascii_uppercase and
        coords[(row+dr, col+dc)] in string.ascii_uppercase and 
        coords[(row-dr, col-dc)] == '.'),
      (None, None)
    )
    if affix:
      coords[(row, col)] = affix + value if side < 2 else value + affix

  portals = {}
  for pos, value in coords.items():
    portals[pos] = pos, 0
    if len(value) != 2:
      continue
    for pos2, value2 in coords.items():
      if value2 == value and pos2 != pos:
        is_outer = any(min(x, edge - x) <= 3 for x, edge in zip(pos, (max(x) for x in zip(*coords))))
        depth_change = -1 if is_outer else 1
        portals[pos] = pos2, depth_change

  coords = collections.defaultdict(str, {k: v for k, v in coords.items() if v == '.' or len(v) == 2})
  return portals, coords


def solve(portals, coords):
  start = next((row, col) for (row, col), value in coords.items() if value == 'AA')
  
  states = [(0, start)]
  visited = set()
  
  while states:
    d, (row, col) = heapq.heappop(states)

    if (row, col) in visited:
      continue
    visited.add((row, col))
    
    for direction in 'NESW':
      new_row = row + (direction == 'S') - (direction == 'N')
      new_col = col + (direction == 'E') - (direction == 'W')
      if not coords[(new_row, new_col)]:
        continue
      (new_row, new_col), _ = portals[(new_row, new_col)]
      
      if coords[(new_row, new_col)] == 'ZZ':
        return d - 1
      
      if coords[(new_row, new_col)]:
        new_d = d + 1 if coords[(new_row, new_col)] == '.' else d
        heapq.heappush(states, (new_d, (new_row, new_col)))


portals, coords = parse_input(inp)

answer = solve(portals, coords)
print(answer)

def solve2(portals, coords):
  start = next((row, col) for (row, col), value in coords.items() if value == 'AA')
  
  states = [(0, 0, start)]
  visited = set()
  
  while states:
    d, depth, (row, col) = heapq.heappop(states)

    if (row, col, depth) in visited or depth < 0:
      continue
    visited.add((row, col, depth))
    
    for direction in 'NESW':
      new_row = row + (direction == 'S') - (direction == 'N')
      new_col = col + (direction == 'E') - (direction == 'W')
      
      if not coords[(new_row, new_col)]:
        continue
      (new_row, new_col), depth_change = portals[(new_row, new_col)]

      if coords[(new_row, new_col)] == 'ZZ' and depth == 0:
        return d - 1
      
      if coords[(new_row, new_col)] not in ['', 'ZZ', 'AA']:
        new_d = d + 1 if coords[(new_row, new_col)] == '.' else d
        heapq.heappush(states, (new_d, depth + depth_change, (new_row, new_col)))


answer = solve2(portals, coords)
print(answer)
