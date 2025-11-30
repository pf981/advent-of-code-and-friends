def get_prominances(nums: list[int]) -> list[int]:
    mono_stack = [[max(nums) + 1, 0]]  # [(peak, right_valley), ...]
    nums = nums + [max(nums) + 1]
    peak = 0
    prominances = []
    for a, b, c in zip(nums[:-2], nums[1:-1], nums[2:]):
        assert a != b and b != c

        if a < b > c:  # Peak
            peak = b
        elif a > b < c:  # Valley
            lowest_prev_valley = peak
            while mono_stack[-1][0] < peak:
                prev_peak, prev_valley = mono_stack.pop()
                lowest_prev_valley = min(lowest_prev_valley, prev_valley)

            lowest_prev_valley = min(lowest_prev_valley, mono_stack[-1][1])
            mono_stack[-1][1] = lowest_prev_valley

            prominances.append(peak - lowest_prev_valley)
            mono_stack.append([peak, b])

    return prominances


with open("./input/40.txt") as f:
    text = f.read()

nums = [int(s) for s in text.split()]

left_to_right = get_prominances(nums)
right_to_left = get_prominances(nums[::-1])[::-1]

answer = sum(min(options) for options in zip(left_to_right, right_to_left))
print(answer)
