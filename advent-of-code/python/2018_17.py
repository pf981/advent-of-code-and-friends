from aocd import get_data

inp = get_data(day=17, year=2018)

import collections
import re

def simulate(m):
  wall_ys = [y for (_, y), v in m.items() if v == '#']
  min_y = min(wall_ys)
  max_y = max(wall_ys)

  states = [(500, min_y)]
  while states:
    x, y = states.pop()
    
    if y > max_y:
      continue
    
    if m[(x, y)] not in ('|', '.'):
      continue
    m[(x, y)] = '|'
    
    # Down
    if m[(x, y + 1)] == '|':
      continue
    if m[(x, y + 1)] == '.':
      states.append((x, y + 1))
      continue
    
    # Left
    xl = x
    while True:
      xl -= 1
      if m[(xl, y)] == '#':
        break
      m[(xl, y)] = '|'
      if m[(xl, y + 1)] == '.':
        states.append((xl, y + 1))
        break
    
    # Right
    xr = x
    while True:
      xr += 1
      if m[(xr, y)] == '#':
        break
      m[(xr, y)] = '|'
      if m[(xr, y + 1)] == '.':
        states.append((xr, y + 1))
        break
    
    # Up
    if m[(xl, y)] == '#' and m[(xr, y)] == '#':
      for x in range(xl + 1, xr):
        m[(x, y)] = '~'
        if m[(x, y - 1)] == '|':
          states.append((x, y - 1))
          
  return m


m = collections.defaultdict(lambda: '.')
for line in inp.splitlines():
  a, b_start, b_end = [int(x) for x in re.findall(r'\d+', line)]
  for b in range(b_start, b_end + 1):
    x, y = (a, b) if line.startswith('x') else (b, a)
    m[(x, y)] = '#'

result = simulate(m)

answer = sum(v in ('|', '~') for v in m.values())
print(answer)

answer = sum(v == '~' for v in m.values())
print(answer)
