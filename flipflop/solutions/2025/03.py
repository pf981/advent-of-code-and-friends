import collections

with open("./input/2025/03.txt") as f:
    lines = f.read().splitlines()

answer1 = collections.Counter(lines).most_common(1)[0][0]
print(answer1)

answer2 = 0
for line in lines:
    nums = [int(x) for x in line.split(",")]
    if len(set(nums)) != 3:
        continue
    answer2 += nums[1] == max(nums)
print(answer2)

answer3 = 0
for line in lines:
    nums = [int(x) for x in line.split(",")]
    if len(set(nums)) != 3:
        answer3 += 10
        continue
    answer3 += [5, 2, 4][nums.index(max(nums))]
print(answer3)
