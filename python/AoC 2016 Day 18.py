from aocd import get_data

inp = get_data(day=18, year=2016)

import collections

def count_safe(s, n_rows):
  traps = collections.defaultdict(bool, enumerate(c == '^' for c in s))
  indexes = list(range(len(s)))
  safe_count = sum(not traps[i] for i in indexes)
  
  for _ in range(n_rows - 1):
    new_traps = collections.defaultdict(bool)
    
    for i in indexes:
      neighbors = (traps[i - 1], traps[i], traps[i + 1])
      if neighbors in [(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)]:
        new_traps[i] = True
        
    traps = new_traps
    safe_count += sum(not traps[j] for j in indexes)
  return safe_count

answer = count_safe(inp, 40)
answer

answer = count_safe(inp, 400000)
answer
