from aocd import get_data

inp = get_data(day=9, year=2021)

import collections

heatmap = collections.defaultdict(
  lambda: 9,
  {
    (row, col): int(value)
    for row, line in enumerate(inp.splitlines())
    for col, value in enumerate(line)
  }
)

low_points = {
  (row, col): value
  for (row, col), value in heatmap.copy().items()
  if all(heatmap[(row + dr, col + dc)] > value for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)])
}

answer = sum(value + 1 for value in low_points.values())
print(answer)

def get_basin_size(row, col, heatmap, visited):
  if (row, col) in visited or heatmap[(row, col)] == 9:
    return 0
  
  visited.add((row, col))
  return 1 + sum(get_basin_size(row + dr, col + dc, heatmap, visited) for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)])

basin_sizes = [get_basin_size(row, col, heatmap, set()) for row, col in low_points]
largest_basin_sizes = sorted(basin_sizes)[-3:]

answer = largest_basin_sizes[0] * largest_basin_sizes[1] * largest_basin_sizes[2]
print(answer)
