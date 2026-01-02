import itertools
import math

for i in itertools.count(144):
    hexagonal = i * (2 * i - 1)
    if ((math.sqrt(24 * hexagonal + 1) + 1) / 6).is_integer():
        break

answer = hexagonal
print(answer)
