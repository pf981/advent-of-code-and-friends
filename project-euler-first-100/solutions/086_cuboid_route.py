import itertools
import math

count = 0
for a in itertools.count(1):
    for s in range(2, 2 * a + 1):
        d_squared = a * a + s * s
        d = math.isqrt(d_squared)

        if d * d == d_squared:
            if s <= a:
                count += s // 2
            else:
                count += a - (s - 1) // 2

    if count > 1_000_000:
        break

answer = a
print(answer)
