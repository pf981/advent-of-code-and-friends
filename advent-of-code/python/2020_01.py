from aocd import get_data

inp = get_data(day=1, year=2020)

nums = set(int(x) for x in inp.splitlines())

for num in nums:
  if 2020 - num in nums:
    answer = num * (2020 - num)
    break

print(answer)

nums = [int(x) for x in inp.split()]

def solve(nums, target):
  n = len(nums)

  for i in range(n):
    for j in range(i + 1, n):
      for k in range(j + 1, n):
        if nums[i] + nums[j] + nums[k] == target:
          return nums[i] * nums[j] * nums[k]

answer = solve(nums, 2020)
print(answer)
