from aocd import get_data

inp = get_data(day=11, year=2021)

def step(octopuses):
  for pos in octopuses:
    octopuses[pos] += 1

  flashed = set()
  for _ in range(100):
    for (row, col), energy in octopuses.items():
      if energy > 9 and (row, col) not in flashed:
        flashed.add((row, col))
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
          if (row + dr, col + dc) in octopuses:
            octopuses[(row + dr, col + dc)] += 1

  for (row, col) in flashed:
    octopuses[(row, col)] = 0

  return len(flashed)

def count_flashes(octopuses, n_steps):
  octopuses = octopuses.copy()
  return sum(step(octopuses) for _ in range(n_steps))

octopuses = {(row, col): int(energy) for row, line in enumerate(inp.splitlines()) for col, energy in enumerate(line)}
  
answer = count_flashes(octopuses, 100)
print(answer)

import itertools

def find_all_flash_step(octopuses):
  octopuses = octopuses.copy()
  return next(i + 1 for i in itertools.count() if step(octopuses) == 100)

answer = find_all_flash_step(octopuses)
print(answer)
