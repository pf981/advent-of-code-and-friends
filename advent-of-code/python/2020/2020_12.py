from aocd import get_data

inp = get_data(day=12, year=2020)

instructions = [(line[0], int(line[1:])) for line in inp.splitlines()]

turn = {
  'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
  'R': {'N': 'E', 'W': 'N', 'S': 'W', 'E': 'S'}
}

row = 0
col = 0
direction = 'E'
for c, d in instructions:
  if c in 'LR':
    for _ in range(d // 90):
      direction = turn[c][direction]
    continue

  if c == 'F':
    c = direction
  for _ in range(d):
    row += (c == 'S') - (c == 'N')
    col += (c == 'E') - (c == 'W')

answer = abs(row) + abs(col)
print(answer)

ship = [0, 0]
waypoint = [-1, 10]
direction = 'E'
for c, d in instructions:
  if c == 'F':
    ship[0] += d * waypoint[0]
    ship[1] += d * waypoint[1]
  elif c == 'L':
    for _ in range(d // 90):
      waypoint = [-waypoint[1], waypoint[0]]
  elif c == 'R':
    for _ in range(d // 90):
      waypoint = [waypoint[1], -waypoint[0]]
  else:
    for _ in range(d):
      waypoint[0] += (c == 'S') - (c == 'N')
      waypoint[1] += (c == 'E') - (c == 'W')

answer = abs(ship[0]) + abs(ship[1])
print(answer)
