from aocd import get_data

inp = get_data(day=12, year=2021)

import collections


def count_paths(edges, allow_small_cave_visited_twice=False):
  states = [(('start', ), collections.defaultdict(int))]
  full_paths = set()
  partial_paths = set()

  while states:
    path, node_counts = states.pop()
    node_counts = node_counts.copy()
    node = path[-1]
    
    if path in partial_paths:
      continue
    partial_paths.add(path)

    if node == 'end':
      full_paths.add(path)
      continue

    if node.islower():
      if not allow_small_cave_visited_twice and node_counts[node] == 1:
        continue
      if node_counts[node] == 2:
        continue
      if node_counts[node] == 1 and max(node_counts.values()) == 2:
        continue
      node_counts[node] += 1

    for new_node in edges[node]:
      if new_node != 'start':
        states.append((path + (new_node, ), node_counts))
      
  return len(full_paths)


edges = collections.defaultdict(list)
for line in inp.splitlines():
  a, b = line.split('-')
  edges[a].append(b)
  edges[b].append(a)

answer = count_paths(edges)
print(answer)

answer = count_paths(edges, True)
print(answer)
