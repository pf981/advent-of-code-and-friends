import collections
import math

factors: collections.Counter[int] = collections.Counter()
for n in range(2, 21):
    cur_factors: collections.Counter[int] = collections.Counter()
    d = 2
    while n > 1:
        while n % d == 0:
            cur_factors[d] += 1
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                cur_factors[n] += 1
            break

    for factor in cur_factors:
        factors[factor] = max(factors[factor], cur_factors[factor])

answer = math.prod(factor**count for factor, count in factors.items())
print(answer)
