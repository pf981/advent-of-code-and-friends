from aocd import get_data

inp = get_data(day=23, year=2021)

import heapq

goals = {
  'A': 2,
  'B': 4,
  'C': 6,
  'D': 8
}


def is_solved(amphipods):
  return all(x == goals[letter] for (x, y), letter in amphipods.items())


def update_state(amphipod, move_to, energy, amphipods):
  (start_x, start_y), letter = amphipod
  x, y = start_x, start_y
  n_moves = 0
  
  # Go to hall
  while y != 0:
    y -= 1
    n_moves += 1
    if (x, y) in amphipods:
      return None
    
  # Go to x
  dx = 1 if x < move_to[0] else -1
  while x != move_to[0]:
    x += dx
    n_moves += 1
    if (x, y) in amphipods:
      return None
  
  # Go to room
  while y != move_to[1]:
    y += 1
    n_moves += 1
    if (x, y) in amphipods:
      return None
    
  amphipods = amphipods.copy()
  del amphipods[(start_x, start_y)]
  amphipods[(x, y)] = letter

  cost_per_move = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[letter]
  
  return (energy + cost_per_move * n_moves, frozenset(amphipods.items()))


def smallest_energy_path(amphipods):
  rooms_y = sorted(set(y for _, y in amphipods))
  
  states = [(0, frozenset(amphipods.items()))]
  visited = set()

  while states:
    energy, amphipods = heapq.heappop(states)
    
    if amphipods in visited:
      continue
    visited.add(amphipods)
    amphipods = dict(amphipods)
    
    if is_solved(amphipods):
      return energy
    
    # Find if any can move to their target room
    found_goal = False
    invalid_goals = {x for x in [2, 4, 6, 8] for y in rooms_y if (x, y) in amphipods and goals[amphipods[(x, y)]] != x}
    
    for (x, y), letter in amphipods.items():
      goal_x = goals[letter]
      if x == goal_x or goal_x in invalid_goals:
        continue
      
      goal_y = next(y for y in rooms_y[::-1] if (goal_x, y) not in amphipods)
      
      new_state = update_state(((x, y), letter), (goal_x, goal_y), energy, amphipods)
      if new_state:
        heapq.heappush(states, new_state)
        found_goal = True
    
    # Don't bother making other moves if you found a move to a room
    if found_goal:
      continue
      
    # Move from room to hallway
    available_squares = ((x, 0) for x in [0, 1, 3, 5, 7, 9, 10] if (x, 0) not in amphipods)
    for pos in available_squares:
      for (x, y), letter in amphipods.items():
        # Don't move from hallway
        if y == 0:
          continue

        new_state = update_state(((x, y), letter), pos, energy, amphipods)
        if new_state:
          heapq.heappush(states, new_state)

          
amphipods = {(x - 1, y - 1): letter for y, line in enumerate(inp.splitlines()) for x, letter in enumerate(line) if letter not in '.# '}

answer = smallest_energy_path(amphipods)
print(answer)

extended_amphipods = {(x, y if y == 1 else 4): letter for (x, y), letter in amphipods.items()}
extended_amphipods.update({
  (2, 2): 'D',
  (2, 3): 'D',
  (4, 2): 'C',
  (4, 3): 'B',
  (6, 2): 'B',
  (6, 3): 'A',
  (8, 2): 'A',
  (8, 3): 'C'
})

answer = smallest_energy_path(extended_amphipods)
print(answer)
