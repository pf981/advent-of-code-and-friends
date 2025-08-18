from aocd import get_data

inp = get_data(day=5, year=2022)

import copy
import re

stack_lines, moves = inp.split('\n\n')

moves = [[int(x) for x in re.findall(r'\d+', line)] for line in moves.splitlines()]

*stack_lines, last = stack_lines.splitlines()
n_stacks = int(last.rstrip(' ').split(' ')[-1])
stacks = [[] for _ in range(n_stacks)]

for s in stack_lines:
  for i_stack, i in enumerate(range(0, len(s), 4)):
    c = s[i+1]
    if c != ' ':
      stacks[i_stack].insert(0, c)

cur_stacks = copy.deepcopy(stacks)
for n, move_from, move_to in moves:
  move_from -= 1
  move_to -= 1
  for _ in range(n):
    cur_stacks[move_to].append(cur_stacks[move_from].pop())

answer = ''.join(stack[-1] for stack in cur_stacks)
print(answer)

cur_stacks = copy.deepcopy(stacks)
for n, move_from, move_to in moves:
  move_from -= 1
  move_to -= 1
  moved = []
  for _ in range(n):
    moved.append(cur_stacks[move_from].pop())
  cur_stacks[move_to].extend(moved[::-1])

answer = ''.join(stack[-1] for stack in cur_stacks)
print(answer)
