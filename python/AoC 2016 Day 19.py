from aocd import get_data

inp = get_data(day=19, year=2016)

inp = 3014603

import collections

def solve(n_elves):
  elves = collections.deque(range(n_elves))
  
  while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()

  return elves.pop() + 1

answer = solve(inp)
answer

def solve2(n_elves):
  left = collections.deque(range(n_elves // 2))
  right = collections.deque(reversed(range(n_elves // 2, n_elves)))

  while left and right:
    (left if len(left) > len(right) else right).pop()
    right.appendleft(left.popleft())
    left.append(right.pop())
  
  return (left or right).pop() + 1

answer = solve2(inp)
answer
