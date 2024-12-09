from aocd import get_data

inp = get_data(day=5, year=2021)

import collections

def count_overlap(segments, include_diagonals):
  points = collections.defaultdict(int)
  for x1, y1, x2, y2 in segments:
    if not include_diagonals and x1 != x2 and y1 != y2:
      continue

    dx = dy = 0
    if x1 != x2:
      dx = 1 if x1 < x2 else -1
    if y1 != y2:
      dy = 1 if y1 < y2 else -1

    x, y = x1, y1
    while True:
      points[(x, y)] += 1
      
      if (x, y) == (x2, y2):
        break

      x += dx
      y += dy
    
  return sum(num >= 2 for num in points.values())

segments = [[int(num) for nums in line.split(' -> ') for num in nums.split(',')] for line in inp.splitlines()]

answer = count_overlap(segments, False)
print(answer)

answer = count_overlap(segments, True)
print(answer)
