import math


def get_primes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start : limit + 1 : step] = [False] * (
                ((limit - start) // step) + 1
            )

    return [i for i in range(limit + 1) if is_prime[i]]


limit = 50_000_000
primes = get_primes(math.isqrt(limit))
squares = [prime**2 for prime in primes]
cubes = [prime**3 for prime in primes if prime**3 < limit]
fourths = [prime**4 for prime in primes if prime**4 < limit]

sums = set()
for square in squares:
    for cube in cubes:
        for fourth in fourths:
            prime_power_triple = square + cube + fourth

            if prime_power_triple < limit:
                sums.add(prime_power_triple)

answer = len(sums)
print(answer)
