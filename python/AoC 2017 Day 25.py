from aocd import get_data

inp = get_data(day=25, year=2017)

import collections
import re

start_info, *states_info = inp.split('\n\n')
start_state = re.search(r'(\w)\.', start_info).group(1)
n_steps = int(re.search(r'\d+', start_info)[0])

states = {}
for state_info in states_info:
  state_name, _, write0, direction0, state0, _, write1, direction1, state1 = re.findall(r'(\w+)[\.:]', state_info)
  states[state_name] = {
    0: (int(write0), 1 if direction0 == 'right' else -1, state0),
    1: (int(write1), 1 if direction1 == 'right' else -1, state1)
  }


def solve(current_state, states, n_steps):
  tape = collections.defaultdict(int)
  cursor = 0
  
  for _ in range(n_steps):
    write, move, state = states[current_state][tape[cursor]]
    tape[cursor] = write
    cursor += move
    current_state = state
  
  return sum(tape.values())

answer = solve(start_state, states, n_steps)
print(answer)

# No puzzle here - just need 49 stars.
