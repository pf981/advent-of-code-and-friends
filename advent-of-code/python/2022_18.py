from aocd import get_data

inp = get_data(day=18, year=2022)

cubes = {tuple(int(x) for x in line.split(',')) for line in inp.splitlines()}

deltas = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
surface_area = 0
for pos in cubes:
  for delta in deltas:
    if tuple(x + dx for x, dx in zip(pos, delta)) not in cubes:
      surface_area += 1

answer = surface_area
print(answer)

bounds = [(min(x), max(x)) for x in zip(*cubes)]
stack = [(0, 0, 0)]
free = set()
while stack:
  pos = stack.pop()
  if pos in free or pos in cubes:
    continue
  free.add(pos)
  
  if any(not (min_bound - 1 <= x <= max_bound + 1) for x, (min_bound, max_bound) in zip(pos, bounds)):
    continue
  
  for delta in deltas:
    stack.append(tuple(x + dx for x, dx in zip(pos, delta)))
  
surface_area = 0
for pos in cubes:
  for delta in deltas:
    if tuple(x + dx for x, dx in zip(pos, delta)) in free:
      surface_area += 1

answer = surface_area
print(answer)
