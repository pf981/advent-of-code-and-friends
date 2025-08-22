import functools


@functools.cache
def sum_factors(n: int) -> int:
    total = 1
    d = 2
    start_n = n
    while n > 1:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        if exp > 0:
            total *= (d ** (exp + 1) - 1) // (d - 1)
        d += 1
        if d * d > n:
            if n > 1:
                total *= (n**2 - 1) // (n - 1)
            break
    return total - start_n


d = sum_factors
answer = sum(n for n in range(2, 10_000) if d(d(n)) == n and d(n) != n)
print(answer)
