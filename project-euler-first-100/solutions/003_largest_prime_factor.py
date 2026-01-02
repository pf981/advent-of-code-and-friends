def prime_factors(n: int) -> list[int]:
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(int(n))
            break
    return factors


answer = max(prime_factors(600851475143))
print(answer)
