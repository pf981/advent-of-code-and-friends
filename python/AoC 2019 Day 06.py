from aocd import get_data

inp = get_data(day=6, year=2019)

import collections

def count_orbits(node, orbits):
  if node not in orbits:
    return 1
  return 1 + sum(count_orbits(child, orbits) for child in orbits[node])

orbits = collections.defaultdict(list)
transfers = collections.defaultdict(list)
nodes = set()

for line in inp.splitlines():
  from_node, to_node = line.split(')')
  orbits[from_node].append(to_node)
  transfers[from_node].append(to_node)
  transfers[to_node].append(from_node)
  nodes.add(from_node)
  nodes.add(to_node)

answer = sum(count_orbits(node, orbits) for node in nodes) - len(nodes)
print(answer)

import heapq

def solve(transfers):
  visited = set()
  states = [(0, 'YOU')]
  
  while True:
    d, node = heapq.heappop(states)
    
    if node in visited:
      continue
    visited.add(node)

    if node == 'SAN':
      return d - 2
    
    for new_node in transfers[node]:
      heapq.heappush(states, (d + 1, new_node))

answer = solve(transfers)
answer
