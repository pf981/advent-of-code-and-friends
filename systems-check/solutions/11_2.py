import functools

with open("./input/11.txt") as f:
    text = f.read()

nums = [int(s, 16) for s in text.split()]


@functools.cache
def get_length(l: int, r: int) -> int:
    length = 0
    i = l
    while i <= r:
        if nums[i] == 0xFE:
            start = i - nums[i + 1]
            end = start + nums[i + 2] - 1
            length += get_length(start, end)
            i += 3
        elif nums[i] == 0xFF:
            length += nums[i + 2]
            i += 3
        else:
            length += 1
            i += 1

    return length


answer = get_length(0, len(nums) - 1)
print(answer)
