from aocd import get_data, submit


inp = get_data(day=2, year=2024)

# inp = '''7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# '''

lines = inp.splitlines()

def is_good(nums):
    if nums[1] > nums[0]: # inc
        for a, b in zip(nums[:-1], nums[1:]):
            if not (1 <= b - a <= 3):
                return False
        return True
    #dec
    for a, b in zip(nums[:-1], nums[1:]):
        if not (1 <= a - b <= 3):
            return False
    return True


answer1 = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    print(nums)
    if is_good(nums):
        answer1 +=1

# is_good([7,6,4,2,1])

print(answer1)

submit(answer1, part='a', day=2, year=2024)


# Part 2

answer2 = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    print(nums)
    for i in range(len(nums)):
        nums2 = nums[:i] + nums[i+1:]
        if is_good(nums2):
            answer2 +=1
            break


print(answer2)

submit(answer2, part='b', day=2, year=2024)
