import functools


@functools.cache
def collatz_count(n: int) -> int:
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + collatz_count(n // 2)

    return 1 + collatz_count(3 * n + 1)


answer = max(range(1, 1_000_000), key=collatz_count)
print(answer)
