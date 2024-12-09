from aocd import get_data

inp = get_data(day=3, year=2017)

inp = 289326

def coords():
  x, y = (1, 0)
  while True:
    yield (x, y)
    dx = (y <= -x and x >= y) - (y > -x and y >= x)
    dy = (y > -x and x > y) - (y <= -x and x < y)
    x += dx
    y += dy

def solve(target):
  num = 1
  for x, y in coords():
    num += 1
    if num == target:
      return abs(x) + abs(y)

answer = solve(inp)
answer

import collections

def solve2(target):
  nums = collections.defaultdict(int)
  nums[(0, 0)] = 1

  for x, y in coords():
    num = sum(nums[(x+dx, y+dy)] for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)))
    nums[(x, y)] = num
    
    if num > target:
      return num

answer = solve2(inp)
answer
