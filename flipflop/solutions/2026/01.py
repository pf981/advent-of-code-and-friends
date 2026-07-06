with open("./input/2026/01.txt") as f:
    lines = f.read().splitlines()

nums = list(map(int, lines))

answer1 = sum(d for num in nums if (d := 60 - num) > 0)
print(answer1)

answer2 = 0
for num in nums:
    if num <= 60:
        answer2 += 60 - num
    else:
        answer2 += 5 * (num - 60)
print(answer2)

mid = len(nums) // 2
answer3 = 0
for num, target in zip(nums[:mid], nums[mid:]):
    if num <= target:
        answer3 += target - num
    else:
        answer3 += 5 * (num - target)
print(answer3)
