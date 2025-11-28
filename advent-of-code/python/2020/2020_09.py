from aocd import get_data

inp = get_data(day=9, year=2020)

nums = [int(x) for x in inp.splitlines()]
w = 25

for i, num in enumerate(nums[w:], w):
  s = set(nums[i-w:i])
  for a in s:
    if num - a in s:
      break
  else:
    target = num
    break

answer = target
print(answer)

def solve():
  for l in range(0, len(nums) - 1):
    for r in range(l + 1, len(nums)):
      vals = nums[l:r]
      if sum(vals) == target:
        return min(vals) + max(vals)
        
answer = solve()
print(answer)
