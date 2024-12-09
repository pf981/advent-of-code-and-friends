from aocd import get_data

inp = get_data(day=22, year=2016)

import re

nodes = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.split('\n')[2:]]

viable_pairs = 0
for i, (_, _, _, a_used, _, _) in enumerate(nodes):
  for _, _, _, _, b_avail, _ in nodes[:i] + nodes[i+1:]:
    if a_used > 0 and a_used <= b_avail:
      viable_pairs += 1

answer = viable_pairs
answer

cur_y = 0
for i, (x, y, _, used, avail, _) in enumerate(sorted(nodes, key=lambda node: node[1])):
  if y > cur_y:
    print()
    cur_y = y

  if avail == 90:
    symbol = ' '
  elif used > 90:
    symbol = 'X'
  elif x == 32 and y == 0:
    symbol = 'A'
  elif x == 0 and y == 0:
    symbol = 'B'
  else:
    symbol = '.'

  print(symbol, end = '')

# This is a sliding puzzle where you have to slide A to B
answer = 16 + 12 + 22 + 31 * 5
answer
