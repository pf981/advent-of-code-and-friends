from aocd import get_data

inp = get_data(day=11, year=2018)

inp = 4172

import numpy as np

def get_power_level(x, y, grid_serial_number):
  rack_id = x + 10
  power_level = rack_id * y
  power_level += grid_serial_number
  power_level *= rack_id
  power_level = power_level // 100 % 10
  power_level -= 5
  
  return power_level

def solve(m, min_size=3, max_size=3):
  summed_area_table = m.cumsum(axis=0).cumsum(axis=1)
  result = (float("-inf"), 0, 0, 0)
  
  for size in range(min_size, max_size + 1):
    for x in range(np.shape(m)[0] - size):
      for y in range(np.shape(m)[1] - size):
        area = (
          summed_area_table[x, y] + 
          summed_area_table[x + size, y + size] - 
          summed_area_table[x + size, y] -
          summed_area_table[x, y + size]
        )

        result = max(
          result,
          (area, x + 1, y + 1, size)
        )
        
  return result


m = np.fromfunction(get_power_level, (300, 300), grid_serial_number=inp)
_, x, y, _ = solve(m)

answer = f'{x},{y}'
print(answer)

_, x, y, size = solve(m, 1, 300)

answer = f'{x},{y},{size}'
print(answer)
