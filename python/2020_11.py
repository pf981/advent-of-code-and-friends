from aocd import get_data

inp = get_data(day=11, year=2020)

m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
n_rows = max(row for row, _ in m) + 1
n_cols = max(col for _, col in m) + 1
occupied = {pos: c == '#' for pos, c in m.items() if c in '#L'}

def count_adjacent(pos, occupied):
  result = 0
  for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    if occupied.get((pos[0] + dr, pos[1] + dc), False):
      result += 1
  return result

def solve(occupied):
  while True:
    occupied2 = occupied.copy()

    for pos, is_occupied in occupied.items():
      adjacent = count_adjacent(pos, occupied)
      if is_occupied:
        if adjacent >= 4:
          occupied2[pos] = False
      else:
        if adjacent == 0:
          occupied2[pos] = True

    if occupied == occupied2:
      return sum(occupied.values())
    occupied = occupied2

answer = solve(occupied)
print(answer)

adjacency = {}
for row, col in occupied:
  adjacency[(row, col)] = []
  for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
    r = row
    c = col
    while True:
      r += dr
      c += dc
      if not (0 <= r < n_rows) or not (0 <= c < n_cols):
        break
      if (r, c) in occupied:
        adjacency[(row, col)].append((r, c))
        break

def solve2(occupied):
  while True:
    occupied2 = occupied.copy()

    for pos, is_occupied in occupied.items():
      adjacent = 0
      for pos2 in adjacency[pos]:
        if occupied[pos2]:
          adjacent += 1
      
      if is_occupied:
        if adjacent >= 5:
          occupied2[pos] = False
      else:
        if adjacent == 0:
          occupied2[pos] = True

    if occupied == occupied2:
      return sum(occupied.values())
    occupied = occupied2

answer = solve2(occupied)
print(answer)
