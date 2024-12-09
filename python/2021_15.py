from aocd import get_data

inp = get_data(day=15, year=2021)

import heapq


def smallest_risk_path(risk_levels):
  target = max(risk_levels)
  states = [(0, 0, 0)]
  visited = set()

  while states:
    risk, row, col = heapq.heappop(states)

    if (row, col) in visited:
      continue
    visited.add((row, col))
    
    if (row, col) == target:
      return risk

    for direction in ['N', 'S', 'E', 'W']:
      new_row = row + (direction == 'S') -  (direction == 'N')
      new_col = col + (direction == 'E') -  (direction == 'W')

      if (new_row, new_col) not in risk_levels:
        continue

      heapq.heappush(states, (risk + risk_levels[(new_row, new_col)], new_row, new_col))

      
risk_levels = {(row, col): int(risk_level) for row, line in enumerate(inp.splitlines()) for col, risk_level in enumerate(line)}

answer = smallest_risk_path(risk_levels)
print(answer)

max_row, max_col = (pos + 1 for pos in max(risk_levels))
risk_levels_extended = {}

for (row, col), risk in risk_levels.items():
  for tile_row in range(5):
    for tile_col in range(5):
      new_risk = risk + tile_row + tile_col
      new_risk = new_risk % 10 + new_risk // 10
      risk_levels_extended[row + max_row * tile_row, col + max_col * tile_col] = new_risk

answer = smallest_risk_path(risk_levels_extended)
print(answer)
