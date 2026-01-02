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


limit = 1_000_000
primes = get_primes(limit)
primes_set = frozenset(primes)


def make_prime(consecutive_length: int) -> int | None:
    start = 0
    s = 0
    for end in range(len(primes)):
        s += primes[end]

        if end - start + 1 > consecutive_length:
            s -= primes[start]
            start += 1

        if end - start + 1 == consecutive_length and s in primes_set:
            return s
    return None


max_length = s = 0
for prime in primes:
    s += prime
    if s >= limit:
        break
    max_length += 1

for consecutive_length in reversed(range(max_length)):
    if answer := make_prime(consecutive_length):
        break
print(answer)
