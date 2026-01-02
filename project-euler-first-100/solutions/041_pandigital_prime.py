import itertools
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for max_range in reversed(range(1, 10)):
    for permutation in itertools.permutations(reversed(range(1, max_range + 1))):
        num = int("".join(str(digit) for digit in permutation))
        if is_prime(num):
            answer = num
            break
    else:
        continue
    break

print(answer)
