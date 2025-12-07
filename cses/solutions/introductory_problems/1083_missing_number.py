n, nums = open(0)

n = int(n)
nums = [int(x) for x in nums.split()]
print(n * (n + 1) // 2 - sum(nums))
