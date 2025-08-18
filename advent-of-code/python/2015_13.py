from aocd import get_data

inp = get_data(day=13, year=2015)

from collections import defaultdict
from itertools import permutations
import re

ds = defaultdict(lambda: defaultdict(int))

for line in inp.split('\n'):
  source, direction, d, dest = re.search(r'^(\w+).*(lose|gain) (\d+).* (\w+)\.$', line).groups()
  d = int(d) * (-1 if direction == 'lose' else 1)
  ds[source][dest] += d
  ds[dest][source] += d

def max_happiness(ds):
  d_max = float('-inf')
  for order in permutations(ds.keys()):
    order += (order[0], )
    d = sum(ds[source][dest] for source, dest in zip(order[:-1], order[1:]))
    d_max = max(d, d_max)
  return d_max

answer = max_happiness(ds)
answer

ds['Paul']
answer = max_happiness(ds)
answer
