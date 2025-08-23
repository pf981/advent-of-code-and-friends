import collections
import math


def generate_triples(max_side):
    for a in range(1, max_side):
        for b in range(a, max_side):
            c_double = math.sqrt(a * a + b * b)
            c = int(c_double)
            if math.isclose(c, c_double):
                yield [a, b, c]


all_p: collections.Counter[int] = collections.Counter()
for a, b, c in generate_triples(1000):
    p = a + b + c
    if p <= 1000:
        all_p[p] += 1

answer = max(all_p.keys(), key=lambda key: all_p[key])
print(answer)
