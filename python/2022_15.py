from aocd import get_data

inp = get_data(day=15, year=2022)

import re

sensors = [[int(x) for x in re.findall(r'-?\d+', line)] for line in inp.splitlines()]

target_y = 2000000
target_in_range = set()
target_beacons = set()
for x, y, bx, by in sensors:
  if by == target_y:
    target_beacons.add(bx)
    
  d = abs(x - bx) + abs(y - by)
  dx = d - abs(y - target_y)
  for x2 in range(x - dx, x + dx + 1):
    target_in_range.add(x2)
    
answer = len(target_in_range.difference(target_beacons))
print(answer)

import z3

def Abs(X):
  return z3.If(X >= 0, X, -X)

X = z3.Int('X')
Y = z3.Int('Y')

o = z3.Optimize()
o.add(X >= 0)
o.add(Y >= 0)
o.add(X <= 4000000)
o.add(Y <= 4000000)

for x, y, bx, by in sensors:
  d = abs(x - bx) + abs(y - by)
  o.add(Abs(X - x) + Abs(Y - y) > d)

o.check()
answer = o.model().eval(X * 4000000 + Y)
print(answer)
