from aocd import get_data

inp = get_data(day=24, year=2020)

import collections
import re


dx = {
  'e': 2,
  'se': 1,
  'sw': -1,
  'w': -2,
  'nw': -1,
  'ne': 1,
}
dy = {
  'e': 0,
  'se': -1,
  'sw': -1,
  'w': 0,
  'nw': 1,
  'ne': 1,
}

tiles = [re.findall(r'e|se|sw|w|nw|ne', line) for line in inp.splitlines()]
flips = collections.Counter(tuple(sum(x) for x in zip(*[(dx[direction], dy[direction]) for direction in directions])) for directions in tiles)
black = {pos for pos, n_flips in flips.items() if n_flips % 2 == 1}

answer = len(black)
print(answer)

def simulate(black):
  neighbors = collections.Counter()
  for pos in black:
    neighbors[pos] += 0
    for direction in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
      neighbors[(pos[0] + dx[direction], pos[1] + dy[direction])] += 1
  
  result = set()
  for pos, cnt in neighbors.items():
    if cnt == 2 or (pos in black and cnt == 1):
      result.add(pos)
  return result


for _ in range(100):
  black = simulate(black)

answer = len(black)
print(answer)
