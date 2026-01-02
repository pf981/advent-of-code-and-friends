import functools
import itertools
from collections.abc import Iterator

primes: list[int] = [2, 3]


def generate_primes() -> Iterator[int]:
    for p in primes:
        yield p
    candidate = primes[-1] + 2
    while True:
        is_p = True
        for q in primes:
            if q * q > candidate:
                break
            if candidate % q == 0:
                is_p = False
                break
        if is_p:
            primes.append(candidate)
            yield candidate
        candidate += 2


@functools.cache
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in generate_primes():
        if p * p > n:
            return True
        if n % p == 0:
            return False
    assert False


cur_value = 1
num_primes = 0

for spiral_radius in itertools.count(1):
    gap_between_diagonals = 2 * spiral_radius

    for _ in range(3):
        cur_value += gap_between_diagonals
        num_primes += is_prime(cur_value)

    cur_value += gap_between_diagonals

    prime_ratio_of_diagonal = num_primes / (4 * spiral_radius + 1)
    if prime_ratio_of_diagonal < 0.1:
        answer = spiral_radius * 2 + 1
        break

print(answer)
