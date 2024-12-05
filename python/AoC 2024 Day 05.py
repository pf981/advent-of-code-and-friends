from aocd import get_data, submit
import collections


inp = get_data(day=5, year=2024)
rules_lines, numbers_lines = inp.split('\n\n')

m = collections.defaultdict(list)
for line in rules_lines.splitlines():
    a, b = line.split('|')
    m[int(a)].append(int(b))


def is_valid(nums):
    seen = set()
    for num in nums:
        for z in m[num]:
            if z in seen:
                return False
        seen.add(num)
    return True


incorrectly_ordered = []
result = []
for line in numbers_lines.splitlines():
    nums = [int(num) for num in line.split(',')]
    if is_valid(nums):
        result.append(nums[len(nums) // 2])
    else:
        incorrectly_ordered.append(nums)

answer1 = sum(result)
print(answer1)

submit(answer1, part='a', day=5, year=2024)


# Part 2


def reorder_impl(num, nums, seen, res):
    if num in seen:
        return
    seen.add(num)
    for num2 in m[num]:
        if num2 in nums:
            reorder_impl(num2, nums, seen, res)
    res.append(num)
    

def reorder(nums):
    seen = set()
    res = []
    for num in nums:
        reorder_impl(num, nums, seen, res)
    return res

result = []
for nums in incorrectly_ordered:
    l = reorder(nums)
    result.append(l[len(l) // 2])

answer2 = sum(result)
print(answer2)

submit(answer2, part='b', day=5, year=2024)
