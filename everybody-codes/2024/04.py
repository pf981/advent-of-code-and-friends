
with open("./2024/input/everybody_codes_e2024_q04_p1.txt") as f:
    lines = f.read().splitlines()

nums = [int(s) for s in lines]
answer1 = sum(num - min(nums) for num in nums)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q04_p2.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]
answer2 = sum(num - min(nums) for num in nums)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q04_p3.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]
answer3 = min(sum(abs(num - target) for num in nums) for target in set(nums))
print(answer3)
