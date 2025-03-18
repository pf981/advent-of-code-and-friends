with open("2024_sample/01.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]

answer1 = sum(nums)
print(answer1)


answer2 = sum(sorted(nums, reverse=True)[20:])
print(answer2)


answer3 = sum(-num if i % 2 else num for i, num in enumerate(nums))
print(answer3)
