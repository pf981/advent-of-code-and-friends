from aocd import get_data

inp = get_data(day=24, year=2019)

import collections


def get_biodiversity(bugs):
  biodiversity = 0
  for row in range(5):
    for col in range(5):
      if (row, col) in bugs:
        biodiversity += 2 ** (5 * row + col)
  return biodiversity


def simulate(bugs):
  neighbors = collections.Counter()
  for bug in bugs:
    for delta in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
      pos = tuple(x + dx for x, dx in zip(bug, delta))
      if not all(0 <= x < 5 for x in pos):
        continue
      neighbors[pos] += 1
  
  return {pos for pos, cnt in neighbors.items() if cnt == 1 or (pos not in bugs and cnt == 2)}


bugs_start = {(row, col) for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line) if c == '#'}

bugs = bugs_start
biodiversities = set()
while True:
  biodiversity = get_biodiversity(bugs)
  if biodiversity in biodiversities:
    break
  biodiversities.add(biodiversity)
  
  bugs = simulate(bugs)

answer = biodiversity
print(answer)

def simulate(bugs):
  neighbors = collections.Counter()
  for bug, depth in bugs:
    for delta in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
      pos = tuple(x + dx for x, dx in zip(bug, delta))

      if pos == (2, 2):
        if bug[0] == 1:
          inner_positions = [(0, x) for x in range(5)]
        elif bug[1] == 3:
          inner_positions = [(x, 4) for x in range(5)]
        elif bug[0] == 3:
          inner_positions = [(4, x) for x in range(5)]
        elif bug[1] == 1:
          inner_positions = [(x, 0) for x in range(5)]
        
        for inner_position in inner_positions:
          neighbors[(inner_position, depth + 1)] += 1
      elif not all(0 <= x < 5 for x in pos):
        if pos[0] == -1:
          pos = (1, 2)
        elif pos[1] == 5:
          pos = (2, 3)
        elif pos[0] == 5:
          pos = (3, 2)
        elif pos[1] == -1:
          pos = (2, 1)

        neighbors[(pos, depth - 1)] += 1
      else:
        neighbors[(pos, depth)] += 1

  return {pos for pos, cnt in neighbors.items() if cnt == 1 or (pos not in bugs and cnt == 2)}


bugs = {(pos, 0) for pos in bugs_start}
for _ in range(200):
  bugs = simulate(bugs)

answer = len(bugs)
print(answer)
