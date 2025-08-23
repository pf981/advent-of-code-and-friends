import math


def get_primes(limit: int) -> frozenset[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return frozenset(i for i in range(limit + 1) if is_prime[i])


primes = get_primes(1_000_000)


def is_truncatable(prime):
    dividend = 10
    while dividend < prime:
        if prime % dividend not in primes or prime // dividend not in primes:
            return False
        dividend *= 10
    return True


truncatable_primes = []
for p in primes:
    if p > 10 and is_truncatable(p):
        truncatable_primes.append(p)
        if len(truncatable_primes) == 11:
            break

answer = sum(truncatable_primes)
print(answer)
