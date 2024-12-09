from aocd import get_data, submit


def is_safe(nums):
    f = lambda a, b: a - b if nums[0] > nums[1] else b - a
    for a, b in zip(nums[:-1], nums[1:]):
        if not (1 <= f(a, b) <= 3):
            return False
    return True


inp = get_data(day=2, year=2024)
lines = inp.splitlines()
reports = [[int(num) for num in line.split()] for line in lines]

answer1 = sum(is_safe(nums) for nums in reports)
print(answer1)

submit(answer1, part='a', day=2, year=2024)


# Part 2


answer2 = 0
for nums in reports:
    for i in range(len(nums)):
        nums2 = nums[:i] + nums[i+1:]
        if is_safe(nums2):
            answer2 +=1
            break
print(answer2)

submit(answer2, part='b', day=2, year=2024)
