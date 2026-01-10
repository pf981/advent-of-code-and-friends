with open("data/day24.txt") as f:
    text = f.read()

nums = [int(x) for x in text.split()]

answer = 0
while nums:
    answer += sum(nums)
    nums = [max(nums[i], nums[i + 1]) + 1 for i in range(len(nums) - 1)]

print(answer)
