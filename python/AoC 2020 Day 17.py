from aocd import get_data

inp = get_data(day=17, year=2020)

import itertools

def simulate(actives):
  neighbors = {}
  for p in actives:
    for delta in itertools.product(*(((-1, 0, 1),) * len(p))):
      p2 = tuple(x + dx for x, dx in zip(p, delta))
      if p2 == p:
        continue

      neighbors[p2] = neighbors.get(p2, 0) + 1
  
  new_actives = set()
  for p, cnt in neighbors.items():
    if p in actives and cnt in [2, 3]:
      new_actives.add(p)
    elif p not in actives and cnt == 3:
      new_actives.add(p)

  actives.clear()
  actives.update(new_actives)


actives_start = {(x, y, 0) for y, line in enumerate(inp.splitlines()) for x, c in enumerate(line) if c == '#'}

actives = actives_start.copy()
for _ in range(6):
  simulate(actives)

answer = len(actives)
print(answer)

actives = {(x, y, z, 0) for x, y, z in actives_start}
for _ in range(6):
  simulate(actives)

answer = len(actives)
print(answer)
