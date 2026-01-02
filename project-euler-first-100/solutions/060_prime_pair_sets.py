import collections
import math
import random

random.seed(0)


def is_prime_mr(n: int, k: int = 1) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def get_primes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]


def find_sets(
    current: list[int], remaining: list[int], target_size: int
) -> list[list[int]]:
    if len(current) == target_size:
        return [current]

    results = []
    for i, p in enumerate(remaining):
        if all(p in pairs.get(q, set()) for q in current):
            new_remaining = [x for x in remaining[i + 1 :] if x in pairs.get(p, set())]
            results.extend(find_sets(current + [p], new_remaining, target_size))
    return results


limit = 10_000
primes = get_primes(limit)
primes_set = set(primes)

pairs = collections.defaultdict(set)

for i, p1 in enumerate(primes):
    for p2 in primes[i + 1 :]:
        c1 = int(str(p1) + str(p2))
        c2 = int(str(p2) + str(p1))

        if (c1 <= limit and c1 in primes_set or c1 > limit and is_prime_mr(c1)) and (
            c2 <= limit and c2 in primes_set or c2 > limit and is_prime_mr(c2)
        ):
            pairs[p1].add(p2)
            pairs[p2].add(p1)


answer = min(sum(s) for s in find_sets([], sorted(pairs.keys()), 5))
print(answer)
