from aocd import get_data

inp = get_data(day=1, year=2017)

def solve(nums, offset = 1):
  return sum(int(x) for x, y in zip(nums, nums[offset:] + nums[:offset]) if x == y)

answer = solve(inp)
answer

answer = solve(inp, len(inp) // 2)
answer
