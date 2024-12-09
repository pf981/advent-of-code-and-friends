from aocd import get_data

inp = get_data(day=1, year=2016)

instructions = [(turn, int(''.join(d))) for turn, *d in inp.split(', ')]
x_coef = [0, 1, 0, -1]
y_coef = [1, 0, -1, 0]

def solve():
  x = y = 0
  heading = 0
  for turn, d in instructions:
    heading += 1 if turn == 'R' else -1
    heading = heading % 4
    x += x_coef[heading] * d
    y += y_coef[heading] * d
  return abs(x) + abs(y)
  
answer = solve()
answer

def solve2():
  visited = set((0, 0))
  x = y = 0
  heading = 0
  for turn, d in instructions:
    heading += 1 if turn == 'R' else -1
    heading = heading % 4
    for _ in range(d):
      x += x_coef[heading]
      y += y_coef[heading]
      if (x, y) in visited:
        return abs(x) + abs(y)
      visited.add((x, y))
  
answer = solve2()
answer
