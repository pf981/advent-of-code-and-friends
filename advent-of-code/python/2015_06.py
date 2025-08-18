from aocd import get_data

inp = get_data(day=6, year=2015)

import re
from collections import defaultdict

lights = defaultdict(bool)
brightness = defaultdict(int)

for line in inp.split('\n'):
  nums = [int(x) for x in re.findall(r'\d+', line)]
  
  for row in range(nums[0], nums[2] + 1):
    for col in range(nums[1], nums[3] + 1):
      if (line.startswith('turn on')):
        lights[(row, col)] = True
        brightness[(row, col)] += 1
      elif (line.startswith('turn off')):
        lights[(row, col)] = False
        brightness[(row, col)] = max(brightness[(row, col)] - 1, 0)
      else:
        lights[(row, col)] = not lights[(row, col)]
        brightness[(row, col)] += 2


answer = sum(lights.values())
answer

answer = sum(brightness.values())
answer
