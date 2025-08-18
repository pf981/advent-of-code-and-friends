from aocd import get_data

inp = get_data(day=5, year=2018)

import re
import string

r = re.compile('|'.join(''.join(letters) for letters in zip(string.ascii_lowercase + string.ascii_uppercase, string.ascii_uppercase + string.ascii_lowercase)))

def react(s):
  prev_s = ''
  while len(prev_s) != len(s):
    prev_s = s
    s = r.sub('', s)
  return len(s)

answer = react(inp)
print(answer)

shortest_polymer = float('inf')
for letter in string.ascii_lowercase:
  length = react(inp.replace(letter, '').replace(letter.upper(), ''))
  shortest_polymer = min(shortest_polymer, length)

answer = shortest_polymer
print(answer)
