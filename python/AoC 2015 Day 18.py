from aocd import get_data

inp = get_data(day=18, year=2015)

start_on = set()
for i, line in enumerate(inp.split('\n')):
  for j, c in enumerate(line):
    if c == '#':
      start_on.add((i, j))

def step(on, persist = []):
  new_on = set()
  
  for p in persist:
    on.add(p)
    new_on.add(p)

  for i in range(100):
    for j in range(100):
      neighbors = int((i-1, j-1) in on) + int((i-1, j) in on) + int((i-1, j+1) in on) + int((i, j-1) in on) + int((i, j+1) in on) + int((i+1, j-1) in on) + int((i+1, j) in on) + int((i+1, j+1) in on)
      if (i, j) in on and neighbors in (2, 3):
        new_on.add((i, j))
      elif (i, j) not in on and neighbors == 3:
        new_on.add((i, j))
  return new_on

on = start_on
for _ in range(100):
  on = step(on)

answer = len(on)
answer

on = start_on
for _ in range(100):
  on = step(on, persist = [(0, 0), (0, 99), (99, 0), (99, 99)])

answer = len(on)
answer
