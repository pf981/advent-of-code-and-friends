from aocd import get_data

inp = get_data(day=20, year=2017)

import copy
import re

def update(particles):
  for p, v, a in particles:
    v[:] = [x + y for x, y in zip(v, a)]
    p[:] = [x + y for x, y in zip(v, p)]
  

particles = [[[int(x) for x in re.findall(r'-?\d+', group)] for group in line.split(', ')] for line in inp.split('\n')]

parts = copy.deepcopy(particles)
for _ in range(1000):
  update(parts)

answer = parts.index(min(parts, key=lambda x: sum(abs(y) for y in x[0])))
print(answer)

import collections

parts = copy.deepcopy(particles)
for _ in range(1000):
  positions = collections.defaultdict(list)
  for elem in parts:
    positions[tuple(elem[0])].append(elem)
  
  for elems in positions.values():
    if len(elems) > 1:
      for elem in elems:
        parts.remove(elem)

  update(parts)

answer = len(parts)
print(answer)
