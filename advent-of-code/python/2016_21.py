from aocd import get_data

inp = get_data(day=21, year=2016)

import collections
import re

def get_indexes(args, s):
  try:
    inds = [int(x) for x in args]
  except ValueError:
    inds = [s.index(x) for x in args]
  
  return inds + [None] * (2 - len(inds))

def rotate(s, n):
  d = collections.deque(s)
  d.rotate(n)
  return list(d)

def scramble(instructions, s):
  s = list(s)
  for instruction, args in instructions:
    a, b = get_indexes(args, s)
    
    if instruction == 'swap':
      s[a], s[b] = s[b], s[a]
    elif instruction == 'rotate left':
      s = rotate(s, -a)
    elif instruction == 'rotate right':
      s = rotate(s, a)
    elif instruction == 'rotate':
      s = rotate(s, 1 + a + (1 if a >= 4 else 0))
    elif instruction == 'reverse':
      s = s[:a] + list(reversed(s[a:b+1])) + s[b+1:]
    elif instruction == 'move':
      x = s[a]
      del s[a]
      s.insert(b, x)
  return ''.join(s)

instructions = [[re.match(r'(\w+(?: (?:right|left))?)', line).group(), re.findall(r'\b(\w)\b', line)] for line in inp.split('\n')]

answer = scramble(instructions, 'abcdefgh')
answer

import itertools

def unscramble(instructions, s):
  for candidate in itertools.permutations(s):
    if scramble(instructions, candidate) == s:
      return ''.join(candidate)

answer = unscramble(instructions, 'fbgdceah')
answer
