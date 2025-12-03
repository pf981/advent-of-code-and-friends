from aocd import get_data, submit


inp = get_data(day=1, year=2015)

answer1 = sum(1 if x == '(' else -1 for x in inp)
submit(str(answer1), part="a", day=1, year=2015)


# Part 2


floor = 0
for position, x in enumerate(inp, 1):
  floor += 1 if x == '(' else -1
  if (floor == -1):
    break
answer2 = position
submit(str(answer2), part="b", day=1, year=2015)
