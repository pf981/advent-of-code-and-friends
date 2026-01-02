import itertools


def count_prime_factors(n: int) -> int:
    total = 0
    d = 2
    while n > 1:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        if exp > 0:
            total += 1
        d += 1
        if d * d > n:
            if n > 1:
                total += 1
            break
    return total


streak = 0
for num in itertools.count():
    if count_prime_factors(num) != 4:
        streak = 0
        continue

    streak += 1
    if streak == 4:
        break

answer = num - 3
print(answer)
