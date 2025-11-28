from aocd import get_data

inp = get_data(day=2, year=2016)

x_delta = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
y_delta = {'U': -1, 'R': 0, 'D': 1, 'L': 0}

buttons = {
  (0, 0): '1', (1, 0): '2', (2, 0): '3',
  (0, 1): '4', (1, 1): '5', (2, 1): '6',
  (0, 2): '7', (1, 2): '8', (2, 2): '9'
}

def dial(line):
  x, y = (1, 1)
  for direction in line:
    new_pos = (x + x_delta[direction], y + y_delta[direction])
    if new_pos in buttons:
      x, y = new_pos
  return buttons[(x, y)]

answer = ''.join(dial(line) for line in inp.split('\n'))
answer

buttons = {
                            (2, 0): '1',
               (1, 1): '2', (2, 1): '3', (3, 1): '4',
  (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
               (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
                            (2, 4): 'D'
}

answer = ''.join(dial(line) for line in inp.split('\n'))
answer
