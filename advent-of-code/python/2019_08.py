from aocd import get_data

inp = get_data(day=8, year=2019)

import numpy as np

width = 25
height = 6
layers = np.array_split([int(x) for x in inp], len(inp) / (width * height))

answer = min((sum(layer == 0), sum(layer == 1) * sum(layer == 2)) for layer in layers)[1]
print(answer)

pixels = [next(subpixel for subpixel in pixel if subpixel in (0, 1)) for pixel in zip(*layers)]

for i, pixel in enumerate(pixels):
  if i % width == 0:
    print()
  print('#' if pixel else ' ', end='')
