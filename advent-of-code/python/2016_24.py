from aocd import get_data

inp = get_data(day=24, year=2016)

import functools
import heapq
import itertools

@functools.lru_cache(maxsize=None)
def shortest_distance(from_pos, to_pos, visitable):
  visitable = set(visitable)
  states = [(0, *from_pos)]
  
  while states:
    d, x, y = heapq.heappop(states)
    
    if (x, y) not in visitable:
      continue
    
    visitable.remove((x, y))
    
    for direction in ['N', 'E', 'S', 'W']:
      new_d = d + 1
      new_x = x + (direction == 'E') - (direction == 'W')
      new_y = y + (direction == 'S') - (direction == 'N')
      
      if (new_x, new_y) not in visitable:
        continue
        
      if (new_x, new_y) == to_pos:
        return new_d

      heapq.heappush(states, (new_d, new_x, new_y))

def solve(visitable, pois, do_loop = False):
  poi_names = [poi_name for poi_name in pois.keys() if poi_name != '0']
  
  shortest = float('inf')
  for visit_order in itertools.permutations(poi_names):
    if do_loop:
      pairs = zip(('0', *visit_order), (*visit_order, '0'))
    else:
      pairs = zip(('0', *visit_order[:-1]), visit_order)
    d = sum(shortest_distance(pois[from_poi], pois[to_poi], visitable) for from_poi, to_poi in pairs)
    shortest = min(shortest, d)
  return shortest

m = {(x, y): c for y, line in enumerate(inp.split('\n')) for x, c in enumerate(line)}
visitable = frozenset({pos for pos, c in m.items() if c != '#'})
pois = {c: pos for pos, c in m.items() if c not in ['#', '.']}

answer = solve(visitable, pois)
answer

answer = solve(visitable, pois, do_loop=True)
answer
