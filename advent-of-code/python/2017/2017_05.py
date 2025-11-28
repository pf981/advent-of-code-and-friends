from aocd import get_data

inp = get_data(day=5, year=2017)

def solve(nums, new_jump_rules=False):
  nums = nums.copy()
  n_steps = 0
  i = 0
  
  while i < len(nums):
    offset = nums[i]
    nums[i] += -1 if new_jump_rules and offset >= 3 else 1
    i += offset
    n_steps += 1
    
  return n_steps

nums = [int(x) for x in inp.split('\n')]

answer = solve(nums)
answer

answer = solve(nums, new_jump_rules=True)
answer
