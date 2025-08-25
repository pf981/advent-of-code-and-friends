import math


def get_period(n: int) -> int:
    a0 = math.isqrt(n)
    if a0 * a0 == n:
        return 0

    m = 0
    d = 1
    a = a0
    period = 0

    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period += 1

    return period


MAX_ROOT = 10_000
total_odd_periods = 0

for n in range(10_000):
    if get_period(n) % 2 == 1:
        total_odd_periods += 1

answer = total_odd_periods
print(answer)
