from aocd import get_data

inp = get_data(day=24, year=2022)

import collections
import functools


@functools.cache
def get_blizzards(t):
  if t == 0:
    return blizzards_start
  
  blizzards = {}
  for pos, l in get_blizzards(t - 1).items():
    for c in l:
      new_pos = [
        pos[0] + (c == 'v') - (c == '^'),
        pos[1] + (c == '>') - (c == '<')
      ]
      if tuple(new_pos) not in free:
        if c == '^':
          new_pos[0] = bottom_side
        elif c == '>':
          new_pos[1] = left_side
        elif c == 'v':
          new_pos[0] = top_side
        elif c == '<':
          new_pos[1] = right_side

      blizzards[tuple(new_pos)] = blizzards.get(tuple(new_pos), '') + c
    
  return blizzards


def solve(start, target, t_start):
  seen = set()
  queue = collections.deque([(start, t_start)])
  while queue:
    pos, t = queue.popleft()

    if (pos, t) in seen:
      continue
    seen.add((pos, t))

    if pos == target:
      return t
    
    if pos in get_blizzards(t):
      continue
    
    for d in ['up', 'down', 'left', 'right', 'none']:
      new_pos = (
        pos[0] + (d == 'down') - (d == 'up'),
        pos[1] + (d == 'right') - (d == 'left')
      )
      if new_pos not in free:
        continue
      queue.append((new_pos, t + 1))


grid = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}

free = {pos for pos, c in grid.items() if c != '#'}
left_side = 1
right_side = max(col for row, col in free)
top_side = 1
bottom_side = max(row for row, col in free) - 1

start = (0, 1)
target = (len(inp.splitlines()) - 1, len(inp.splitlines()[0]) - 2)
blizzards_start = {pos: c for pos, c in grid.items() if c in '^>v<'}

time_to_goal = solve(start, target, 0)
answer = time_to_goal
print(answer)

answer = solve(
  start,
  target,
  solve(target, start, time_to_goal)
)
print(answer)
