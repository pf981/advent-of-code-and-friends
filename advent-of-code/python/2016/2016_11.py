from aocd import get_data

inp = get_data(day=11, year=2016)

import collections
import copy
import heapq
import itertools

def comb(l, take_min, take_max):
  return itertools.chain.from_iterable(itertools.combinations(l, r) for r in range(take_min, take_max+1))

def is_valid(floors):
  for floor in floors:
    contains_generator = False
    contains_exposed_microchip = False
    
    for element, object_type in floor:
      if object_type == 'generator':
        contains_generator = True
      if object_type == 'microchip' and (element, 'generator') not in floor:
        contains_exposed_microchip = True
      
    if contains_generator and contains_exposed_microchip:
      return False
  
  return True

def hashable_floors(floors):
  d = collections.defaultdict(lambda: [None]*2)
  for i, floor in enumerate(floors):
    for element, object_type in floor:
      d[element][object_type == 'microchip'] = i
  return tuple(sorted(tuple(x) for x in d.values()))

def solve(start_floors):
  visited = set((hashable_floors(start_floors), 0))
  states = [(0, copy.deepcopy(start_floors), 0)]
  
  while states:
    n_moves, floors, elevator = heapq.heappop(states)

    for new_elevator in (elevator - 1, elevator + 1):
      if new_elevator < 0 or new_elevator >= len(floors):
        continue
      
      for items in comb(floors[elevator], 1, 2):
        new_floors = copy.deepcopy(floors)
        for item in items:
          new_floors[elevator].remove(item)
          new_floors[new_elevator].add(item)
        
        if not is_valid(new_floors):
          continue
          
        h = hashable_floors(new_floors)
        if (h, new_elevator) in visited:
          continue
        visited.add((h, new_elevator))
        
        if all(len(floor) == 0 for floor in new_floors[:-1]):
          return n_moves + 1
        
        heapq.heappush(states, (n_moves + 1, new_floors, new_elevator))

import re

start_floors = [set(re.findall(r'([\w+-]+?)(?:-compatible)?(?: )(microchip|generator)', line)) for line in inp.split('\n')]

answer = solve(start_floors)
answer

start_floors[0].add(('elerium', 'generator'))
start_floors[0].add(('elerium', 'microchip'))
start_floors[0].add(('dilithium', 'generator'))
start_floors[0].add(('dilithium', 'microchip'))

answer = solve(start_floors)
answer
