from aocd import get_data

inp = get_data(day=15, year=2016)

import itertools
import math
import re

def lcm(nums):
  lcm = 1
  for num in nums:
    lcm = lcm * num // math.gcd(lcm, num)
  return lcm

def get_position(disc, t, total_positions):
  disc_id, positions, _, start_position = disc
  step_size = total_positions / positions
  true_start = step_size * (start_position + disc_id)
  return (true_start + step_size * t) % total_positions

def solve(discs):
  total_positions = lcm(position for _, position, _, _ in discs)
  
  for t in itertools.count():
    if all(get_position(disc, t, total_positions) == 0 for disc in discs):
      return t

discs = [[int(x) for x in re.findall(r'\d+', line)] for line in inp.split('\n')]

answer = solve(discs)
answer

discs.append([7, 11, 0, 0])

answer = solve(discs)
answer
