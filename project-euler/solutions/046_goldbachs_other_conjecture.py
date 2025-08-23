import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_square(num):
    root = math.sqrt(num)
    return math.isclose(root, int(root))


primes = []

for candidate in range(3, 10_000, 2):
    if is_prime(candidate):
        primes.append(candidate)
    elif not any(is_square((candidate - prime) / 2) for prime in primes):
        answer = candidate
        break

print(answer)
