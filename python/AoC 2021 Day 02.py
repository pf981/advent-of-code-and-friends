from aocd import get_data

inp = get_data(day=2, year=2021)

depth = horizontal = 0
instructions = [(direction, int(value)) for direction, value in [line.split(' ') for line in inp.splitlines()]]

for direction, value in instructions:
  if direction == 'forward':
    horizontal += value
  elif direction == 'up':
    depth -= value
  elif direction == 'down':
    depth += value
    
answer = depth * horizontal
print(answer)

depth = horizontal = aim = 0

for direction, value in instructions:
  if direction == 'forward':
    horizontal += value
    depth += aim * value
  elif direction == 'up':
    aim -= value
  elif direction == 'down':
    aim += value

answer = depth * horizontal
print(answer)
