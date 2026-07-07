import functools
import sys

sys.setrecursionlimit(2**31 - 1)

with open("input/07.txt") as f:
    text = f.read()

n, *nums = map(int, text.split())
MOD = 998_244_353


@functools.cache
def count_ways(i: int, prev: tuple[int, ...]) -> int:
    if len(prev) == 3 and prev not in [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]:
        return 0

    if i == n:
        if len(prev) < 3:
            return 0
        return 1

    discard = count_ways(i + 1, prev)
    keep = count_ways(i + 1, (prev + (nums[i] % 2,))[-3:])

    return (discard + keep) % MOD


answer = count_ways(0, tuple())
print(answer)
