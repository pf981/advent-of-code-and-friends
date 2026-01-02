import math


def get_primes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def is_permutation(a: int, b: int) -> bool:
    return sorted(str(a)) == sorted(str(b))


limit = 10_000_000
primes = get_primes(2 * math.isqrt(limit))

best_n = 0
best_ratio = float("inf")

for i, p in enumerate(primes):
    for q in primes[i:]:
        n = p * q
        if n > limit:
            break

        phi_n = (p - 1) * (q - 1)
        if not is_permutation(n, phi_n):
            continue

        ratio = n / phi_n
        if ratio < best_ratio:
            best_ratio = ratio
            best_n = n

answer = best_n
print(answer)
