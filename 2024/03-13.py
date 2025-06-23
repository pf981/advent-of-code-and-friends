import functools

cables = [40, 12, 2, 1]


@functools.cache
def count_ways(d: int) -> int:
    if d == 0:
        return 1

    if d < 0:
        return 0

    ways = 0
    for cable in cables:
        ways += count_ways(d - cable)

    return ways


answer = count_ways(856)
print(answer)
