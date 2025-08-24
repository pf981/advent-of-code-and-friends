import math

count = 0
for n in range(101):
    for r in range(n + 1):
        count += math.comb(n, r) > 1_000_000

answer = count
print(answer)
