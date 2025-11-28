from aocd import get_data

inp = get_data(day=20, year=2018)

import collections

def get_paths(s):
  positions = []
  paths = collections.defaultdict(list)
  prev_x, prev_y = x, y = 0, 0
  
  for c in s:
    if c in ('^', '$'):
      continue

    if c == '(':
      positions.append((x, y))
    elif c == ')':
      x, y = positions.pop()
    elif c == '|':
      x, y = positions[-1]
    else:
      x += (c == 'E') - (c == 'W')
      y += (c == 'S') - (c == 'N')
      paths[(prev_x, prev_y)].append((x, y))

    prev_x, prev_y = x, y
  
  return paths

def get_distances(paths):
  distances = {}
  states = [(0, (0, 0))]
  
  while states:
    d, pos = states.pop()
    
    if pos in distances:
      continue
    
    distances[pos] = d
    
    for path in paths[pos]:
      states.append((d + 1, (path)))
  return distances


paths = get_paths(inp)
distances = get_distances(paths)

answer = max(distances.values())
print(answer)

answer = sum(d >= 1000 for d in distances.values())
print(answer)
