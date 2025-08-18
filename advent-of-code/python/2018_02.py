from aocd import get_data

inp = get_data(day=2, year=2018)

import collections
import math

box_ids = inp.splitlines()

answer = math.prod(sum(n in collections.Counter(box_id).values() for box_id in box_ids) for n in [2, 3])
print(answer)

import itertools

def solve(box_ids):
  for a, b in itertools.combinations(box_ids, 2):
    matched = [x for x, y in zip(a, b) if x == y]
    if len(matched) == len(a) - 1:
      return matched

answer = ''.join(solve(box_ids))
print(answer)
