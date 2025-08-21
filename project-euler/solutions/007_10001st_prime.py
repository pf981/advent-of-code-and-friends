import itertools
import math
from typing import Generator


def is_prime(n: int) -> bool:
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


# All primes > 3 are in the form 6k +/- 1
def gen_candidates() -> Generator[int]:
    for k in itertools.count(1):
        yield 6 * k - 1
        yield 6 * k + 1


n = 2
for candidate in gen_candidates():
    n += is_prime(candidate)
    if n == 10001:
        break

answer = candidate
print(answer)
