from aocd import get_data, submit
import heapq


def get_min_heat_loss(m, target, min_streak, max_streak):
  reverse_direction = {
    '<': '>',
    '>': '<',
    '^': 'v',
    'v': '^',
    'x': 'x'
  }
  seen = set()
  h = [(0, (0, 0), 'x')]
  while True:
    heat, pos, streak = heapq.heappop(h)

    if pos == target:
      return heat
    
    if (streak, pos) in seen:
      continue
    seen.add((streak, pos))
    
    for direction in '<>^v':
      if reverse_direction[streak[-1]] == direction:
        continue

      new_pos = pos
      new_heat = heat
      new_streak = streak
      n_moves = 1

      if streak[-1] != direction:
        new_streak = ''
        n_moves = min_streak
      elif len(streak) == max_streak:
        continue
    
      for _ in range(n_moves):
        new_streak += direction
        new_pos = (
          new_pos[0] + (direction == 'v') - (direction == '^'),
          new_pos[1] + (direction == '>') - (direction == '<')
        )
        if new_pos not in m:
          break
        new_heat += m[new_pos]
      else:
        heapq.heappush(h, (new_heat, new_pos, new_streak))


inp = get_data(day=17, year=2023)
lines = inp.splitlines()
m = {(row, col): int(c) for row, line in enumerate(lines) for col, c in enumerate(line)}
target = (len(lines) - 1, len(lines[0]) - 1)

answer1 = get_min_heat_loss(m, target, 1, 3)
print(answer1)

submit(answer1, part='a', day=17, year=2023)

# Part 2


answer2 = get_min_heat_loss(m, target, 4, 10)
print(answer2)

submit(answer2, part='b', day=17, year=2023)
