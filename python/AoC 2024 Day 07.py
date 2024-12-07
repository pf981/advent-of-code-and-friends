from aocd import get_data, submit
import re


def can_make(i, target, nums):
    if i == len(nums):
        if target == 0:
            return True
        # if target == 1:
        #     return True
        return False
    
    if can_make(i + 1, target / nums[i], nums):
        return True
    if can_make(i + 1, target - nums[i], nums):
        return True
    return False


inp = get_data(day=7, year=2024)

# inp = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''

lines = inp.splitlines()

m = [[int(x) for x in re.findall(r'\d+', line)]for line in lines]

answer1 = 0
for target, *nums in m:
    if can_make(0, target, nums[::-1]):
        answer1 += target
print(answer1)

# 3267 = 81 * 40 + 27
# 3267 / 81
# # 190+3267+292

# submit(answer1, part='a', day=7, year=2024)


# Part 2

def can_make(i, target, nums):
    # print(f'{target=} {i=} {nums[i:]=}')
    if i == len(nums):
        # if -1 < target < 1:
        #     print(f'----> {target=} {nums[i:]=}')
        if target == 0:
            return True
        # if target == 1:
        #     return True
        return False
    
    if can_make(i + 1, target / nums[i], nums):
        return True
    if can_make(i + 1, target - nums[i], nums):
        return True
    
    if int(target) == target and str(int(target)).endswith(str(nums[i])):
        if can_make(i + 1, target // (10**(len(str(nums[i])))), nums):
            return True
    return False


inp = get_data(day=7, year=2024)

# inp = '''190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20'''

# inp = '''7290: 6 8 6 15'''

lines = inp.splitlines()

m = [[int(x) for x in re.findall(r'\d+', line)]for line in lines]

answer2 = 0
for target, *nums in m:
    if can_make(0, target, nums[::-1]):
        answer2 += target
print(answer2)

# answer2 = 0
# for target, *nums in m:
#     for i in range(len(nums)-1):
#         nums2 = nums.copy()
#         nums2[i] = int(str(nums2[i]) + str(nums2[i+1]))
#         del nums2[i+1]
#         if can_make(0, target, nums2[::-1]):
#             answer2 += target
# print(answer2)


submit(answer2, part='b', day=7, year=2024)
