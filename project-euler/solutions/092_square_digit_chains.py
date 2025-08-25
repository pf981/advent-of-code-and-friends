import functools


@functools.cache
def arrives_at_89(n: int) -> bool:
    if n == 89:
        return True
    if n == 1:
        return False

    n2 = 0
    while n:
        digit = n % 10
        n2 += digit * digit
        n //= 10
    return arrives_at_89(n2)


answer = sum(arrives_at_89(n) for n in range(1, 10_000_000))
print(answer)
