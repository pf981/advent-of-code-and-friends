from aocd import get_data

inp = get_data(day=13, year=2016)

inp = 1364

from heapq import heappop, heappush

def is_open(x, y):
  if x < 0 or y < 0:
    return False
  
  num = x*x + 3*x + 2*x*y + y + y*y + inp
  return bin(num).count('1') % 2 == 0

def solve():
  visited = set()
  states = [(0, 1, 1)] # d, x, y
  
  while states:
    d, x, y = heappop(states)
    visited.add((x, y))
    
    for direction in ['N', 'E', 'S', 'W']:
      new_d = d + 1
      new_x = x + (direction == 'E') - (direction == 'W')
      new_y = y + (direction == 'S') - (direction == 'N')
      
      if is_open(new_x, new_y) and (new_x, new_y) not in visited:
        if new_x == 31 and new_y == 39:
          return new_d
        
        heappush(states, (new_d, new_x, new_y))

answer = solve()
answer

def solve2():
  visited = set()
  states = [(0, 1, 1)] # d, x, y
  
  while states:
    d, x, y = heappop(states)
    visited.add((x, y))
    
    for direction in ['N', 'E', 'S', 'W']:
      new_d = d + 1
      new_x = x + (direction == 'E') - (direction == 'W')
      new_y = y + (direction == 'S') - (direction == 'N')
      
      if new_d <= 50 and is_open(new_x, new_y) and (new_x, new_y) not in visited:        
        heappush(states, (new_d, new_x, new_y))
  return len(visited)

answer = solve2()
answer
