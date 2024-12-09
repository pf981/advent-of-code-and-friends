from aocd import get_data

inp = get_data(day=17, year=2022)

import itertools


def can_move(rock, pos, direction, occupied):
  if pos[0] == 0 and direction == 'v':
    return False

  new_pos = (
    pos[0] - (direction == 'v'),
    pos[1] + (direction == '>') - (direction == '<'),
  )

  for r, c in rock:
    r = r + new_pos[0]
    c = c + new_pos[1]
    if c < 0 or c >= 7 or (r, c) in occupied:
      return False

  return True


rocks = [
  ((0, 0), (0, 1), (0, 2), (0, 3)), # -
  ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)), # +
  ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)), # _|
  ((0, 0), (1, 0), (2, 0), (3, 0)), # |
  ((0, 0), (0, 1), (1, 0), (1, 1)), # o
]
directions = itertools.cycle(inp)
occupied = set()
heights = []
floor = 0
for i, rock in enumerate(itertools.cycle(rocks)):
  if i == 10000:
    break

  heights.append(floor)
  pos = [floor + 3, 2] # Bottom left corner of the rock's bounding box
  while True:
    direction = next(directions)
    if can_move(rock, pos, direction, occupied):
      pos[1] += (direction == '>') - (direction == '<')
        
    if can_move(rock, pos, 'v', occupied):
      pos[0] -= 1
    else:
      for r, c in rock:
        floor = max(floor, r + pos[0] + 1)
        occupied.add((r + pos[0], c + pos[1]))
      break

answer = heights[2022]
print(answer)

def find_period(l):
  for period in range(1, len(l)):
    prev_seq = l[:period]
    for i in range(period, len(l) - period, period):
      cur_seq = l[i:i + period]
      if cur_seq != prev_seq:
        break
      prev_seq = cur_seq
    else:
      return period


deltas = [cur - prev for cur, prev in zip(heights[1:], heights[:-1])]
period = find_period(deltas[3000:])

period_start = 1000000000000 - (1000000000000 - 3000) // period * period
height_per_period = heights[period_start + period] - heights[period_start]
n_periods = (1000000000000 - period_start) // period

answer = heights[period_start] + height_per_period * n_periods
print(answer)
