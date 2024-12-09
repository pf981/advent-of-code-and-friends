from aocd import get_data

inp = get_data(day=10, year=2019)

import cmath
import collections
import math

def find_max_asteroids(asteroids):
  distances = collections.defaultdict(lambda: collections.defaultdict(list))
  for x, y in asteroids:
    for x1, y1 in asteroids:
      if (x1, y1) == (x, y):
        continue
      r, theta = cmath.polar(complex(x - x1, y - y1))
      theta = (-math.pi / 2 + theta) % (2 * math.pi)
      distances[(x, y)][theta].append((r, x1, y1))
  return distances

asteroids = {(x, y) for y, line in enumerate(inp.splitlines()) for x, c in enumerate(line) if c == '#'}
distances = find_max_asteroids(asteroids)
best = max(distances.values(), key=lambda x: len(x))

answer = len(best)
print(answer)

objects = sorted([(i, angle, x, y) for angle, objects in best.items() for i, (d, x, y) in enumerate(objects)])
target_object = objects[199]

answer = 100 * target_object[2] + target_object[3]
print(answer)
