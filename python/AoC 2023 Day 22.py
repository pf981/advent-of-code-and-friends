from aocd import get_data, submit
import re


def get_points(x1, y1, x2, y2):
  s = set()
  for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
      s.add((x, y))
  return s


def get_supports(i, bricks):
  x1, y1, z1, x2, y2, z2 = bricks[i]
  z1 -= 1
  z2 -= 1
  ps = get_points(x1, y1, x2, y2)

  sups = set()
  for i2 in range(i):
    bx1, by1, bz1, bx2, by2, bz2 = bricks[i2]
    if bz2 != z1: # The bottom of the ith brick needs to have the same z as the top of the lower brick
      continue
    if get_points(bx1, by1, bx2, by2).intersection(ps):
      sups.add(i2)
  
  return sups


inp = get_data(day=22, year=2023)
X1, Y1, Z1, X2, Y2, Z2 = range(6)
bricks = [[int(num) for num in re.findall(r'-?[0-9]+', line)] for line in inp.splitlines()]
bricks.sort(key=lambda brick: brick[2])
supports = {}

for i, _ in enumerate(bricks):
  sups = []
  while bricks[i][Z1] > 1 and not (sups := get_supports(i, bricks)):
    bricks[i][Z1] -= 1
    bricks[i][Z2] -= 1
  supports[i] = sups

brick_ids = set(range(len(bricks)))
cannot_remove = {next(iter(s)) for s in supports.values() if len(s) == 1}
can_remove = brick_ids.difference(cannot_remove)
answer1 = len(can_remove)
print(answer1)

submit(answer1, part='a', day=22, year=2023)


# Part 2


fall_counts = []
for candidate in cannot_remove:
  fallen = set([candidate])
  for _ in range(10):
    for i, s in supports.items():
      if bricks[i][Z1] == 1:
        continue
      if not s.difference(fallen):
        fallen.add(i)
  
  fall_counts.append(len(fallen) - 1)

answer2 = sum(fall_counts)
print(answer2)

submit(answer2, part='b', day=22, year=2023)
