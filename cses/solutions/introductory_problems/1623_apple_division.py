_, line = open(0)
nums = [int(x) for x in line.split()]
result = total = sum(nums)
s = 0


def backtrack(i: int) -> None:
    global s
    global result

    if i == len(nums):
        result = min(result, abs(s - (total - s)))
        return

    backtrack(i + 1)

    s += nums[i]
    backtrack(i + 1)
    s -= nums[i]


backtrack(0)
print(result)
