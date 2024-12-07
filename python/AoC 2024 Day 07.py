from aocd import get_data, submit
import re


def can_make(i, target, nums, is_p2):
    if i == len(nums):
        if target == 0:
            return True
        return False
    
    if can_make(i + 1, target / nums[i], nums, is_p2):
        return True
    if can_make(i + 1, target - nums[i], nums, is_p2):
        return True
    
    if (is_p2
        and int(target) == target
        and str(int(target)).endswith(str(nums[i]))
        and can_make(i + 1, target // (10**(len(str(nums[i])))), nums, is_p2)
    ):
            return True

    return False


inp = get_data(day=7, year=2024)
lines = inp.splitlines()
m = [[int(x) for x in re.findall(r'\d+', line)]for line in lines]

answer1 = 0
for target, *nums in m:
    if can_make(0, target, nums[::-1], False):
        answer1 += target
print(answer1)

submit(answer1, part='a', day=7, year=2024)


# Part 2


answer2 = 0
for target, *nums in m:
    if can_make(0, target, nums[::-1], True):
        answer2 += target
print(answer2)

submit(answer2, part='b', day=7, year=2024)
