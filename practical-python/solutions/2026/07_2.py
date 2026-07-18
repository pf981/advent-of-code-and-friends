import functools

with open("./input/2026/07/input2.txt") as f:
    text = f.read()

nums = [int(s) if s.isdigit() else None for s in text.split()]


@functools.cache
def get_max_score(i: int, used_prev: bool) -> int:
    if i >= len(nums):
        return 0

    discard = get_max_score(2 * i + 1, False) + get_max_score(2 * i + 2, False)

    keep = 0
    if nums[i] is not None and not used_prev:
        keep = nums[i] + get_max_score(2 * i + 1, True) + get_max_score(2 * i + 2, True)

    return max(discard, keep)


answer = get_max_score(0, False)
print(answer)
