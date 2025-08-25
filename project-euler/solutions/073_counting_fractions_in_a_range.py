import math

LEFT = 1 / 3
RIGHT = 1 / 2
LIMIT = 12_000

answer = 0
for d in range(2, LIMIT + 1):
    n_min = d // 3 + 1
    n_max = (d - 1) // 2

    for n in range(n_min, n_max + 1):
        if math.gcd(n, d) == 1:
            answer += 1

print(answer)
