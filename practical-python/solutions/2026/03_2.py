import re

with open("./input/2026/03/input2.txt") as f:
    text = f.read()

nums = [int(d) for d in re.findall(r"-?\d+", text)]
flips = 0
while nums:
    i = nums.index(max(nums, key=abs))
    if i == len(nums) - 1 and nums[-1] > 0:
        nums.pop()
        continue

    if i != 0:
        nums[: i + 1] = [-x for x in reversed(nums[: i + 1])]
        flips += 1

    nums = [-x for x in reversed(nums)]
    flips += 1
    if nums[-1] < 0:
        flips += 1
    nums.pop()

answer = flips
print(answer)
