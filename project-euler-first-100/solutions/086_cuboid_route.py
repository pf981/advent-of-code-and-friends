import itertools
import math


def has_integer_shortest_path(a: int, b: int, c: int) -> bool:
    a, b, c = sorted([a, b, c], reverse=True)
    squared_d = a * a + (b + c) * (b + c)
    d = math.isqrt(squared_d)
    return d * d == squared_d


count = 0
for m in itertools.count():
    a = m
    for b in range(1, m + 1):
        for c in range(b, m + 1):
            count += has_integer_shortest_path(a, b, c)

    if count > 1_000_000:
        break

answer = m
print(answer)
# Very slow - takes several minutes
