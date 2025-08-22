import math


def find_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                return (a, b, c)


answer = math.prod(find_triplet())
print(answer)
