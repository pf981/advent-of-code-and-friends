from aocd import get_data

inp = get_data(day=8, year=2022)

def move(pos, direction):
  while True:
    pos = (
      pos[0] + (direction == 'S') - (direction == 'N'),
      pos[1] + (direction == 'E') - (direction == 'W')
    )
    yield pos


def is_visible(pos, direction, trees):
  max_height = trees[pos]
  for pos in move(pos, direction):
    if pos not in trees:
      return True
    if trees[pos] >= max_height:
      return False


trees = {(row, col): int(c) for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}

visible = 0
for pos in trees:
  for direction in 'NESW':
    if is_visible(pos, direction, trees):
      visible += 1
      break

answer = visible
print(answer)

def count_in_direction(pos, direction, trees):
  max_height = trees[pos]
  count = 0
  for pos in move(pos, direction):
    if pos not in trees:
      return count
    count += 1
    if trees[pos] >= max_height:
      return count


best = 0
for pos in trees:
  product = 1
  for direction in 'NESW':
    product *= count_in_direction(pos, direction, trees)
  best = max(best, product)

answer = best
print(answer)
