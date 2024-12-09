from aocd import get_data

inp = get_data(day=1, year=2015)

answer = sum(1 if x == '(' else -1 for x in inp)
answer

floor = 0
for position, x in enumerate(inp, 1):
  floor += 1 if x == '(' else -1
  if (floor == -1):
    break
answer = position
answer
