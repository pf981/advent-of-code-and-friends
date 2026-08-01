import functools


@functools.cache
def count_ways(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (count_ways(n - 1) + count_ways(n - 2))


with open("./input/2026/09/input1.txt") as f:
    text = f.read()
n = len(text.split(","))

answer = count_ways(n)
print(answer)
