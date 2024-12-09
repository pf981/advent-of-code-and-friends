from aocd import get_data

inp = get_data(day=16, year=2017)

import re
import string

def dance(letters, moves):
  for move, (a, b) in moves:
    if move == 's':
      letters[:] = letters[-a:] + letters[:-a]
    elif move == 'x':
      letters[a], letters[b] = letters[b], letters[a]
    elif move == 'p':
      a, b = (letters.index(x) for x in [a, b])
      letters[a], letters[b] = letters[b], letters[a]

moves = [(move, [x if move == 'p' else int(x) for x in ''.join(args).split('/')] + [None]*(move=='s')) for move, *args in inp.split(',')]

letters = list(string.ascii_lowercase[:16])
dance(letters, moves)

answer = ''.join(letters)
print(answer)

import itertools

letters = list(string.ascii_lowercase[:16])

done = set()
results = {}

for i in itertools.count():
  if (t := tuple(letters)) in done:
    break
  done.add(t)
  results[i] = t
  dance(letters, moves)

answer = ''.join(results[1000000 % len(results)])
print(answer)
