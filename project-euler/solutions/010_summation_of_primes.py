import math

limit = 2_000_000
sieve = [1] * limit
sieve[0] = 0
sieve[1] = 0

for i in range(4, limit, 2):
    sieve[i] = 0

last_prime = 1
for i in range(3, int(math.sqrt(limit)) + 1, 2):
    if not sieve[i]:
        continue

    for j in range(i * (last_prime + 2), limit, 2 * i):
        sieve[j] = 0
    last_prime = i

answer = sum(i for i, is_prime in enumerate(sieve) if is_prime)
print(answer)
