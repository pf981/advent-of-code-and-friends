from aocd import get_data

inp = get_data(day=10, year=2022)

x = 1
signal_strengths = []
xs = []
cycle = 0
for line in inp.splitlines():
  args = line.split(' ')
  cycle += 1
  signal_strengths.append(x * cycle)
  xs.append(x)
  
  if args[0] == 'noop':
    continue
  
  cycle += 1
  signal_strengths.append(x * cycle)
  xs.append(x)
  x += int(args[1])

answer = sum(signal_strengths[i - 1] for i in [20, 60, 100, 140, 180, 220])
print(answer)

for i, sprite in enumerate(xs):
  pixel_position = i % 40
  if pixel_position == 0:
    print()

  c = '.'
  if sprite - 1 <= pixel_position <= sprite + 1:
    c = '#'
  print(c, end='')

answer = 'EHPZPJGL'
print(answer)
