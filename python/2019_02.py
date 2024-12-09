from aocd import get_data

inp = get_data(day=2, year=2019)

import itertools
import operator

def run_instructions(nums, a, b):
  nums = nums.copy()
  nums[1] = a
  nums[2] = b
  for i in itertools.count(step=4):
    if nums[i] == 99:
      return nums[0]
    fn = operator.add if (nums[i] == 1) else operator.mul
    nums[nums[i + 3]] = fn(nums[nums[i + 1]], nums[nums[i + 2]])

nums = [int(x) for x in inp.split(',')]

answer = run_instructions(nums, 12, 2)
print(answer)

def solve(nums):
  for a in range(100):
    for b in range(100):
      if run_instructions(nums, a, b) == 19690720:
        return 100 * a + b

answer = solve(nums)
print(answer)
