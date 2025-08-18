from aocd import get_data

inp = get_data(day=16, year=2022)

import collections
import functools
import re


@functools.cache
def shortest_path(start, end):
  if start == end:
    return 0
  
  queue = collections.deque([(0, start)])
  visited = set()
  while queue:
    t, pos = queue.pop()
    if pos in visited:
      continue
    visited.add(pos)
    
    if pos == end:
      return t
    
    for new_pos in valves[pos][1]:
      queue.appendleft((t + 1, new_pos))

  return float('inf')


@functools.cache
def maximize_pressure(pos, time_left, available_valves):
  max_pressure = 0

  for destination in available_valves:
    dt = min(shortest_path(pos, destination) + 1, time_left)
    new_time_left = time_left - dt
    pressure = new_time_left * valves[destination][0] + maximize_pressure(destination, new_time_left, available_valves - {destination})
    max_pressure = max(max_pressure, pressure)

  return max_pressure


valves = {}
for line in inp.splitlines():
  valve, *tunnel_to = re.findall(r'[A-Z][A-Z]', line)
  flow = re.findall(r'\d+', line)[0]
  valves[valve] = (int(flow), tunnel_to)

available_valves = frozenset({valve for valve, (pressure, _) in valves.items() if pressure > 0})
  
answer = maximize_pressure('AA', 30, available_valves)
answer # 6 seconds

import itertools


best = 0
for length in range(len(available_valves) // 2 + 1):
  for my_valves in itertools.combinations(available_valves, length):
    my_valves = frozenset(my_valves)
    elephant_valves = available_valves.difference(my_valves)
    total_pressure = maximize_pressure('AA', 26, my_valves) + maximize_pressure('AA', 26, elephant_valves)
    best = max(best, total_pressure)

answer = best
print(answer) # 1 minute
