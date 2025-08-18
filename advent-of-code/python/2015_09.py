from aocd import get_data

inp = get_data(day=9, year=2015)

from collections import defaultdict
from itertools import permutations

ds = defaultdict(dict)

for line in inp.split('\n'):
  source, dest, d = line.split(' ')[::2]
  ds[source][dest] = int(d)
  ds[dest][source] = int(d)
  
d_max = float('-inf')
d_min = float('inf')
for path in permutations(ds.keys()):
  d = sum(ds[source][dest] for source, dest in zip(path[:-1], path[1:]))
  d_max = max(d, d_max)
  d_min = min(d, d_min)

answer = d_min
answer

answer = d_max
answer
