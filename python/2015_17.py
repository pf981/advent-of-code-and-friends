from aocd import get_data

inp = get_data(day=17, year=2015)

from collections import defaultdict

ways_to_fill = defaultdict(int)

def compute_ways_to_fill(items, capacity, n_containers = 0):
  if capacity == 0:
    ways_to_fill[n_containers] += 1
    return
  if capacity < 0:
    return
  
  remaining_items = items.copy()
  for item in items:
    remaining_items.remove(item)
    compute_ways_to_fill(remaining_items, capacity - item, n_containers + 1)

compute_ways_to_fill([int(x) for x in inp.split('\n')], 150)

answer = sum(ways_to_fill.values())
answer

answer = ways_to_fill[min(ways_to_fill.keys())]
answer
