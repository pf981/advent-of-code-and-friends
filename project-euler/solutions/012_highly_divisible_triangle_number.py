import itertools


def count_factors(n: int) -> int:
    total = 1
    d = 2
    while n > 1:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        if exp > 0:
            total *= exp + 1
        d += 1
        if d * d > n:
            if n > 1:
                total *= 2
            break
    return total


triangle_num = 0
for i in itertools.count(1):
    triangle_num += i
    if count_factors(triangle_num) > 500:
        answer = triangle_num
        break

print(answer)
