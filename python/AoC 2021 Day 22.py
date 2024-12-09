from aocd import get_data

inp = get_data(day=22, year=2021)

import re


def cube_subtract(c1, c2):
  c1x1, c1x2, c1y1, c1y2, c1z1, c1z2 = c1
  c2x1, _, c2y1, _, c2z1, _ = (max(a, b) for a, b in zip(c1, c2))
  _, c2x2, _, c2y2, _, c2z2 = (min(a, b) for a, b in zip(c1, c2))
  
  if (c1x1 > c2x2 or c1x2 < c2x1) or (c1y1 > c2y2 or c1y2 < c2y1) or (c1z1 > c2z2 or c1z2 < c2z1):
    return [c1]
  
  result = [
    (c1x1  , c1x2  ,   c1y1  , c1y2  ,   c1z1  , c2z1-1), # top
    (c1x1  , c1x2  ,   c1y1  , c1y2  ,   c2z2+1, c1z2  ), # bottom
    (c1x1  , c2x1-1,   c1y1  , c1y2  ,   c2z1  , c2z2  ), # left part
    (c2x2+1, c1x2  ,   c1y1  , c1y2  ,   c2z1  , c2z2  ), # right part
    (c2x1  , c2x2  ,   c1y1  , c2y1-1,   c2z1  , c2z2  ), # front part
    (c2x1  , c2x2  ,   c2y2+1, c1y2  ,   c2z1  , c2z2  )  # back part
  ]
  return [(x1, x2, y1, y2, z1, z2) for x1, x2, y1, y2, z1, z2 in result if x1 <= x2 and y1 <= y2 and z1 <= z2]


def get_cubes(ops):
  cubes = []
  for op, c2 in ops:
    old_cubes = cubes
    cubes = []
    for c1 in old_cubes:
      cubes.extend(cube_subtract(c1, c2))
    if op == 'on':
      cubes.append(c2)
      
  return cubes

      
def area(cube, initialization):
  x1, x2, y1, y2, z1, z2 = cube
  
  if initialization:
    x1, y1, z1 = (max(d, -50) for d in (x1, y1, z1))
    x2, y2, z2 = (min(d, 50) for d in (x2, y2, z2))
    
    if x1 > x2 or y1 > y2 or z1 > z2:
      return 0

  return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


ops = [(line.split(' ')[0], [int(g) for g in re.findall(r'-?\d+', line)]) for line in inp.splitlines()]
cubes = get_cubes(ops)
    
answer = sum(area(cube, True) for cube in cubes)
print(answer)

answer = sum(area(cube, False) for cube in cubes)
print(answer)
