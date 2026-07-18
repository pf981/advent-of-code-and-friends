import functools

with open("./input/2026/07/input1.txt") as f:
    text = f.read()

nums = [int(s) for s in text.split() if s.isdigit()]


@functools.cache
def get_max_score(i: int) -> int:
    if i >= len(nums):
        return 0

    discard = get_max_score(i + 1)
    keep = nums[i] + get_max_score(i + 2)
    return max(discard, keep)


answer = get_max_score(0)
print(answer)
