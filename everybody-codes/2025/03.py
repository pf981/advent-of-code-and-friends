import collections


with open("./2025/input/everybody_codes_e2025_q03_p1.txt") as f:
    lines = f.read().splitlines()

nums = [int(x) for x in lines[0].split(",")]

answer1 = sum(set(nums))
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q03_p2.txt") as f:
    lines = f.read().splitlines()

nums = [int(x) for x in lines[0].split(",")]

answer2 = sum(sorted((set(nums)))[:20])
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q03_p3.txt") as f:
    lines = f.read().splitlines()

nums = [int(x) for x in lines[0].split(",")]

answer3 = max(collections.Counter(nums).values())
print(answer3)
