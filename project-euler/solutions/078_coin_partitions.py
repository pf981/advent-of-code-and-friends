import functools
import itertools


# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
# p(n) = \sum_{k = 1}^\infty (-1)^{k+1} \big(p(n-k(3k-1)/2) + p(n-k(3k+1)/2)\big) .
@functools.cache
def partitions(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0

    result = 0
    sign = -1
    for k in itertools.count(1):
        p1 = partitions(n - k * (3 * k - 1) // 2)
        p2 = partitions(n - k * (3 * k + 1) // 2)
        sign = -sign
        result += sign * (p1 + p2)
        if p1 == p2 == 0:
            break
    return result


for n in itertools.count(1):
    if partitions(n) % 1_000_000 == 0:
        break

answer = n
print(answer)
