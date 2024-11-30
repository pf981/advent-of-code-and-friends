
with open("./2024/input/everybody_codes_e2024_q04_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''3
# 4
# 7
# 8'''.splitlines()

nums = [int(x) for x in lines]
answer1 = sum(x - min(nums) for x in nums)

print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q04_p2.txt") as f:
    lines = f.read().splitlines()

nums = [int(x) for x in lines]
answer2 = sum(x - min(nums) for x in nums)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q04_p3.txt") as f:
    lines = f.read().splitlines()

# lines = '''2
# 4
# 5
# 6
# 8'''.splitlines()

nums = [int(x) for x in lines]
# z = sum(nums) // len(nums)
# answer3 = sum(abs(x - z) for x in nums)

answer3 = float('inf')
for z in range(min(nums), max(nums) + 1):
    s = sum(abs(x - z) for x in nums)
    answer3 = min(answer3, s)


# [abs(x - z) for x in nums]

print(answer3)
