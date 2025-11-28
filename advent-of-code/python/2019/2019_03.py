from aocd import get_data

inp = get_data(day=3, year=2019)

def get_points(wire):
  points = {}
  x, y, steps = 0, 0, 0
  for direction, d in wire:
    for _ in range(d):
      steps += 1
      x += (direction == 'R') - (direction == 'L')
      y += (direction == 'D') - (direction == 'U')
      if (x, y) not in points:
        points[(x, y)] = steps
  return points

wires = [[(direction, int(''.join(digits))) for direction, *digits in line.split(',')] for line in inp.splitlines()]
points = [get_points(wire) for wire in wires]
intersections = points[0].keys() & points[1].keys()

answer = min(abs(x) + abs(y) for x, y in intersections)
print(answer)

answer = min(points[0][intersection] + points[1][intersection] for intersection in intersections)
print(answer)
