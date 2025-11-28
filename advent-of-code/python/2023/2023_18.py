from aocd import get_data, submit
from shapely.geometry import Polygon


def get_capacity(instructions):
  pos = (0, 0)
  corners = [(0, 0)]
  dist_sum = 0
  for direction, dist in instructions:
    dist_sum += dist
    pos = (
      pos[0] + dist * ((direction == 'D') - (direction == 'U')),
      pos[1] + dist * ((direction == 'R') - (direction == 'L'))
    )
    corners.append(pos)

  return int(Polygon(corners).area + 1 + dist_sum / 2)


inp = get_data(day=18, year=2023)
instructions = [line.split() for line in inp.splitlines()]
answer1 = get_capacity([(direction, int(dist)) for direction, dist, _ in instructions])
print(answer1)

submit(answer1, part='a', day=18, year=2023)


# Part 2


answer2 = get_capacity([('RDLU'[int(s[-2:-1], 16)], int(s[2:-2], 16)) for _, _, s in instructions])
print(answer2)

submit(answer2, part='b', day=18, year=2023)
