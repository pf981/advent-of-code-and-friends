from aocd import get_data

inp = get_data(day=23, year=2022)

import collections


def needs_to_move(row, col, elves):
  return any(pos in elves for pos in [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)])


def get_proposal(row, col, round_num, elves):
  propose = [None] * 4

  if all(pos not in elves for pos in [(row - 1, col), (row - 1, col + 1), (row - 1, col - 1)]):
    propose[0] = (row - 1, col)

  if all(pos not in elves for pos in [(row + 1, col), (row + 1, col + 1), (row + 1, col - 1)]):
    propose[1] = (row + 1, col)

  if all(pos not in elves for pos in [(row, col - 1), (row - 1, col - 1), (row + 1, col - 1)]):
    propose[2] = (row, col - 1)

  if all(pos not in elves for pos in [(row, col + 1), (row - 1, col + 1), (row + 1, col + 1)]):
    propose[3] = (row, col + 1)

  for _ in range(4):
    if propose[round_num % 4]:
      break
    round_num += 1
  return propose[round_num % 4]
  

def simulate(elves, round_num):
  is_done = True
  proposals = {} # new_pos: old_pos
  for row, col in elves:
    if not needs_to_move(row, col, elves):
      continue
    is_done = False

    if proposal := get_proposal(row, col, round_num, elves):
      proposals[proposal] = (row, col) if proposal not in proposals else None

  new_elves = {new_pos for new_pos, old_pos in proposals.items() if old_pos}
  new_elves.update(elves - set(proposals.values()))

  return frozenset(new_elves), is_done


start_elves = frozenset({(row, col) for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line) if c == '#'})
elves = start_elves
for round_num in range(10):
  elves, _ = simulate(elves, round_num)

side_lengths = [(1 + max(dim) - min(dim)) for dim in zip(*elves)]
answer = side_lengths[0] * side_lengths[1] - len(elves)
print(answer)

import itertools

elves = start_elves
for round_num in itertools.count():
  elves, is_done = simulate(elves, round_num)
  if is_done:
    break

answer = round_num + 1
print(answer) # 12 seconds
