from aocd import get_data

inp = get_data(day=18, year=2018)

import collections

def step(m):
  old_m = m.copy()
  for (row, col), c in m.items():
    neighbors = [v for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) for v in old_m[(row+dr, col+dc)]]
    n_trees = sum(v == '|' for v in neighbors)
    n_lumberyards = sum(v == '#' for v in neighbors)

    if c == '.' and n_trees >= 3:
      m[(row, col)] = '|'
    if c == '|' and n_lumberyards >= 3:
      m[(row, col)] = '#'
    if c == '#' and not (n_lumberyards >= 1 and n_trees >= 1):
      m[(row, col)] = '.'
  
  return m

def generate_resource_values(m):
  m = m.copy()
  while True:
    yield sum(v == '|' for v in m.values()) * sum(v == '#' for v in m.values())
    step(m)

m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
m = collections.defaultdict(lambda: '.', m)

answer = next(v for i, v in enumerate(generate_resource_values(m)) if i == 10)
print(answer)

def solve(m):
  seen = {}
  resource_values = {}
  for i, v in enumerate(generate_resource_values(m)):
    if i < 1000:
      continue
    if v in seen:
      period_start = seen[v]
      period_length = i - period_start
      j = period_start + ((1000000000 - period_start) % period_length)
      return resource_values[j]
    seen[v] = i
    resource_values[i] = v

answer = solve(m)
print(answer)
