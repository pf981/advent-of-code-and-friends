import math


def get_primes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]


limit = 1_000_000
primes = get_primes(limit)

answer = 1
for prime in primes:
    if answer * prime > limit:
        break
    answer *= prime

print(answer)
