from aocd import get_data

inp = get_data(day=6, year=2018)

import collections
import re

def solve(pois):
  (min_row, max_row), (min_col, max_col) = ((min(x), max(x)) for x in zip(*pois))

  poi_areas = collections.defaultdict(int)
  safe_count = 0

  for row in range(min_row, max_row):
    for col in range(min_col, max_col):
      ds = sorted((abs(row - poi_row) + abs(col - poi_col), (poi_row, poi_col)) for poi_row, poi_col in pois)
      if ds[0][0] != ds[1][0]:
        poi_areas[ds[0][1]] += 1
      if sum(d for d, _ in ds) < 10000:
        safe_count += 1
  
  largest_finite_area = max(area for area in poi_areas.values() if area < 5000)
  return largest_finite_area, safe_count


pois = tuple((int(x), int(y)) for x, y in re.findall(r'(\d+), (\d+)', inp))
largest_finite_area, safe_count = solve(pois)

answer = largest_finite_area
print(answer)

answer = safe_count
print(answer)
