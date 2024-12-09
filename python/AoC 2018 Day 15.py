from aocd import get_data

inp = get_data(day=15, year=2018)

import copy
import heapq

def move(unit, open_squares, enemies):
  targets = {(row+dr, col+dc) for (row, col), _ in enemies for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)) if (row+dr, col+dc) in open_squares}
  
  if unit[0] in {(row+dr, col+dc) for (row, col), _ in enemies for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0))}:
    return
  
  min_d = float("inf")
  solutions = []
  
  visited = set()
  states = [(0, unit[0], None)]

  while states:
    d, pos, first_move = heapq.heappop(states)
    
    if d > min_d:
      break
      
    if pos in visited:
      continue
    visited.add(pos)
    
    if pos in targets:
      solutions.append((pos, first_move or pos))
      min_d = d

    for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
      new_pos = (pos[0] + dr, pos[1] + dc)
      
      if new_pos not in open_squares or new_pos in visited:
        continue
      
      heapq.heappush(states, (d + 1, new_pos, first_move or new_pos))
  
  if solutions:
    l1 = len(open_squares)
    first_move = min(solutions)[1]
    open_squares.add(unit[0])
    open_squares.remove(first_move)
    unit[0] = first_move

def attack(unit, open_squares, enemies, extra_damage=0):
  adjacent = {(unit[0][0]+dr, unit[0][1]+dc) for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0))}
  targets = [e for e in enemies if e[0] in adjacent]
  if targets:
    target = min(targets, key=lambda x: (x[1], x[0]))
    target[1] -= 3 + extra_damage
    if target[1] <= 0:
      open_squares.add(target[0])
      enemies.remove(target)

def solve(open_squares, elves, goblins):
  open_squares = copy.deepcopy(open_squares)
  elves = copy.deepcopy(elves)
  goblins = copy.deepcopy(goblins)
  
  rounds = 0
  while elves and goblins:
    for unit in sorted(elves + goblins):
      if not unit in elves + goblins:
        continue

      enemies = goblins if unit in elves else elves
      if len(enemies) == 0:
        rounds -= 1
        break
      move(unit, open_squares, enemies)
      attack(unit, open_squares, enemies)
    rounds += 1

  return (rounds) * (sum(hp for _, hp in elves + goblins))


m = {(row, col): value for row, line in enumerate(inp.splitlines()) for col, value in enumerate(line)}
open_squares = {pos for pos, value in m.items() if value == '.'}
elves = [[pos, 200] for pos, value in m.items() if value == 'E']
goblins = [[pos, 200] for pos, value in m.items() if value == 'G']

answer = solve(open_squares, elves, goblins)
print(answer)

import itertools

def elves_win(open_squares, elves, goblins, extra_damage):
  open_squares = copy.deepcopy(open_squares)
  elves = copy.deepcopy(elves)
  goblins = copy.deepcopy(goblins)
  
  n_elves = len(elves)
  rounds = 0
  while elves and goblins:
    for unit in sorted(elves + goblins):
      if not unit in elves + goblins:
        continue

      enemies = goblins if unit in elves else elves
      if len(enemies) == 0:
        rounds -= 1
        break
      move(unit, open_squares, enemies)
      attack(unit, open_squares, enemies, extra_damage=extra_damage if unit in elves else 0)
      if len(elves) < n_elves:
        return None
    rounds += 1

  return (rounds) * (sum(hp for _, hp in elves + goblins))

def solve2(open_squares, elves, goblins):
  for extra_damage in itertools.count():
    result = elves_win(open_squares, elves, goblins, extra_damage)
    if result:
      return result

answer = solve2(open_squares, elves, goblins)
print(answer)
