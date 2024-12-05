from aocd import get_data, submit


inp = get_data(day=5, year=2024)

# inp = '''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13\n\n75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# '''

len(inp.split('\n\n'))

a, b = inp.split('\n\n')
a = a.splitlines()
b = b.splitlines()
# lines = inp.splitlines()
import collections
bad = collections.defaultdict(list)

for line in a:
    x, y = line.split('|')
    # int(x)
    bad[int(x)].append(int(y)) # If you see x before y, it is bad


def is_bad(nums):
    seen = set()
    for num in nums:
        for z in bad[num]:
            if z in seen:
                return True
        seen.add(num)
    return False

incorrectly_ordered = []
result = []
for line in b:
    nums = [int(x) for x in line.split(',')]
    if is_bad(nums):
        incorrectly_ordered.append(nums)
        continue
    result.append(nums[len(nums) // 2])
    
# result


answer1 = sum(result)
print(answer1)

# submit(answer1, part='a', day=5, year=2024)


# Part 2
def reorder_impl(num, nums, seen, res):
    if num in seen:
        return
    seen.add(num)
    for num2 in bad[num]:
        if num2 in nums:
            reorder_impl(num2, nums, seen, res)
    res.append(num)
    

def reorder(nums):
    seen = set()
    res = []
    for i in nums:
        reorder_impl(i, nums, seen, res)
    return res

result2 = []
for nums in incorrectly_ordered:
    l = reorder(nums.copy())
    print(l)
    result2.append(l[len(l) // 2])

# reorder([75, 97, 47, 61, 53])

answer2 = sum(result2)
print(answer2)

# submit(answer2, part='b', day=5, year=2024)
