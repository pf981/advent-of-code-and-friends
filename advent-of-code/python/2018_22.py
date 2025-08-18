from aocd import get_data

inp = get_data(day=22, year=2018)

import re

def get_regions(depth, target_x, target_y):
  extra = 20
  geologic_index = {}
  erosion_level = {}
  region_type = {}
  for x in range(target_x + extra):
    for y in range(target_y + extra):
      if (x, y) in ((0, 0), (target_x, target_y)):
        geologic_index[(x, y)] = 0
      elif y == 0:
        geologic_index[(x, y)] = x * 16807
      elif x == 0:
        geologic_index[(x, y)] = y * 48271
      else:
        geologic_index[(x, y)] = erosion_level[(x-1, y)] * erosion_level[(x, y-1)]
      erosion_level[(x, y)] = (geologic_index[(x, y)] + depth) % 20183
      region_type[(x, y)] = erosion_level[(x, y)] % 3
  return region_type

depth, target_x, target_y = (int(x) for x in re.findall(r'\d+', inp))
regions = get_regions(depth, target_x, target_y)

answer = sum(risk_level for (x, y), risk_level in regions.items() if 0 <= x <= target_x and 0 <= y <= target_y)
print(answer)

import heapq

def solve(regions, target_x, target_y):
  tools = {
    0: ('climbing gear', 'torch'),
    1: ('climbing gear', 'neither'),
    2: ('torch', 'neither')
  }
  
  states = [(0, 0, 0, 'torch')]
  visited = set()
  
  while states:
    d, x, y, tool = heapq.heappop(states)
    
    if (x, y, tool) in visited:
      continue
    visited.add((x, y, tool))
    
    heapq.heappush(states, (d + 7, x, y, next(new_tool for new_tool in tools[regions[(x, y)]] if new_tool != tool)))
    
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
      new_x = x + dx
      new_y = y + dy

      if not (0 <= new_x < target_x + 20 and 0 <= new_y < target_y + 20):
        continue
      if tool not in tools[regions[(new_x, new_y)]]:
        continue
      if (new_x, new_y, tool) == (target_x, target_y, 'torch'):
        return d + 1
      heapq.heappush(states, (d + 1, new_x, new_y, tool))

answer = solve(regions, target_x, target_y)
print(answer)
