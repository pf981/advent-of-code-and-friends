import math

limit = 1_000_000
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(limit)) + 1):
    if is_prime[i]:
        step = i
        start = i * i
        is_prime[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)
primes = {num for num, num_is_prime in enumerate(is_prime) if num_is_prime}


def rotations(n):
    string = str(n)
    for i in range(len(string)):
        yield int(string[i:] + string[:i])


def is_circular(prime):
    for rotation in rotations(prime):
        if rotation not in primes:
            return False
    return True


circular_primes = [prime for prime in primes if is_circular(prime)]
answer = len(circular_primes)
print(answer)
