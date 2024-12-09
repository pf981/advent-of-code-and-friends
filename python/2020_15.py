from aocd import get_data

inp = get_data(day=15, year=2020)

nums = [int(num) for num in inp.split(',')]

def get_nth(n):
  seen = {num: i for i, num in enumerate(nums[:-1])}
  prev = nums[-1]
  for i in range(len(nums), n):
    value = i - 1 - seen.get(prev, i - 1)
    seen[prev] = i - 1
    prev = value
  return value

answer = get_nth(2020)
print(answer)

answer = get_nth(30000000)
print(answer)
