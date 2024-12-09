from aocd import get_data

inp = get_data(day=9, year=2017)

import collections

def solve(s):
  l = collections.deque(s)
  depth = 0
  total_score = 0
  garbage_letters = 0
  
  while l:
    letter = l.popleft()
    if letter == '{':
      depth += 1
    elif letter == '}':
      total_score += depth
      depth -= 1
    elif letter == '<':
      while l and (letter := l.popleft()) != '>':
        if letter == '!':
          l.popleft()
        else:
          garbage_letters += 1
  return total_score, garbage_letters

total_score, garbage_letters = solve(inp)

answer = total_score
print(answer)

answer = garbage_letters
print(answer)
