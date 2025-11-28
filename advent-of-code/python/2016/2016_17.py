from aocd import get_data

inp = get_data(day=17, year=2016)

import hashlib
import heapq

def solve(passcode):
  states = [(0, 0, 0, '')]
  while states:
    d, row, col, path = heapq.heappop(states)

    for direction, is_open in enumerate(x in 'bcedf' for x in hashlib.md5((passcode + path).encode()).hexdigest()[:4]):
      if not is_open:
        continue
      new_row = row + (direction == 1) - (direction == 0)
      new_col = col + (direction == 3) - (direction == 2)
      new_path = path + ['U', 'D', 'L', 'R'][direction]
      
      if new_row < 0 or new_col < 0 or new_row > 3 or new_col > 3:
        continue
      
      if new_row == 3 and new_col == 3:
        return new_path

      heapq.heappush(states, (d + 1, new_row, new_col, new_path))

answer = solve(inp)
answer

def longest_path(row, col, s):
  if row == 3 and col == 3:
    return 0
  
  longest = float('-inf')
  for direction, is_open in enumerate(x in 'bcedf' for x in hashlib.md5(s.encode()).hexdigest()[:4]):
    if not is_open:
      continue
    new_row = row + (direction == 1) - (direction == 0)
    new_col = col + (direction == 3) - (direction == 2)
    new_s = s + ['U', 'D', 'L', 'R'][direction]

    if new_row < 0 or new_col < 0 or new_row > 3 or new_col > 3:
      continue
    longest = max(longest, 1 + longest_path(new_row, new_col, new_s))
  return longest

answer = longest_path(0, 0, inp)
answer
