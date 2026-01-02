import collections
import math

limit = 1_500_000
sqrt_limit = math.isqrt(limit)

# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
counts: collections.Counter[int] = collections.Counter()
for n in range(1, sqrt_limit + 1):
    for m in range(n + 1, sqrt_limit + 1, 2):
        if math.gcd(m, n) != 1:
            continue

        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        length = a + b + c

        if length > limit:
            break

        k = 1
        while k * length <= limit:
            counts[k * length] += 1
            k += 1

answer = sum(count == 1 for count in counts.values())
print(answer)
