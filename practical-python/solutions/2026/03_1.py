import re

with open("./input/2026/03/input1.txt") as f:
    text = f.read()

nums = [int(d) for d in re.findall(r"\d+", text)]
flips = 0
while nums:
    i = nums.index(max(nums))
    if i == len(nums) - 1:
        nums.pop()
        continue

    if i != 0:
        nums[: i + 1] = reversed(nums[: i + 1])
        flips += 1

    nums.reverse()
    flips += 1
    nums.pop()

answer = flips
print(answer)
