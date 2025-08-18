from aocd import get_data

inp = get_data(day=8, year=2016)

import numpy as np
import re

screen = np.zeros((6, 50), bool)

for line in inp.split('\n'):
  command = re.findall(r'\w+(?: [a-z]+)?', line)[0]
  args = [int(x) for x in re.findall(r'\d+', line)]
  
  if command == 'rect':
    screen[:args[1], :args[0]] = True
  elif command == 'rotate row':
    screen[args[0], :] = np.roll(screen[args[0], :], args[1])
  elif command == 'rotate column':
    screen[:, args[0]] = np.roll(screen[:, args[0]], args[1])

answer = screen.sum()
answer

for line in screen:
  print(''.join('#' if x else ' ' for x in line))

answer = 'CFLELOYFCS'
answer
