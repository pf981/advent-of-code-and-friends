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


primes = [prime for prime in get_primes(10**6 - 1) if prime >= 10**5]
primes_set = set(primes)


def compute_family(prime_str, to_replace):
    return sum(
        int(prime_str.replace(to_replace, digit)) in primes_set
        for digit in "0123456789"
    )


for prime in primes:
    candidate = str(prime)
    if any(
        candidate.count(repeated_digit) == 3
        and compute_family(candidate, repeated_digit) == 8
        for repeated_digit in "0123456789"
    ):
        answer = prime
        break

print(answer)
