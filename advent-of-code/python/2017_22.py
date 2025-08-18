from aocd import get_data

inp = get_data(day=22, year=2017)

import collections

nodes = collections.defaultdict(bool)
for row, line in enumerate(inp.splitlines()):
  for col, s in enumerate(line):
    nodes[(row, col)] = s == '#'
    
def solve(nodes):
  nodes = nodes.copy()
  direction = 'N'
  row = col = max(nodes)[0] // 2
  infected_count = 0
  
  for _ in range(10000):
    if nodes[(row, col)]:
      direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]
      nodes[(row, col)] = False
    else:
      direction = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}[direction]
      nodes[(row, col)] = True
      infected_count += 1

    row += (direction == 'S') - (direction == 'N')
    col += (direction == 'E') - (direction == 'W')
  return infected_count

answer = solve(nodes)
print(answer)

def solve2(nodes):
  nodes = nodes.copy()
  direction = 'N'
  row = col = max(nodes)[0] // 2
  infected_count = 0
  
  for _ in range(10000000):
    if nodes[(row, col)] == 0:
      direction = {'N': 'W', 'E': 'N', 'S': 'E', 'W': 'S'}[direction]
    elif nodes[(row, col)] == 2:
      direction = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]
    elif nodes[(row, col)] == 3:
      direction = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}[direction]
      
    nodes[(row, col)] = (nodes[(row, col)] + 1) % 4
    if nodes[(row, col)] == 2:
      infected_count += 1

    row += (direction == 'S') - (direction == 'N')
    col += (direction == 'E') - (direction == 'W')
  return infected_count

answer = solve2(collections.defaultdict(int, {k: v*2 for k, v in nodes.items()}))
print(answer)
