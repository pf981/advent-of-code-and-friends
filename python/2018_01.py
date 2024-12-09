from aocd import get_data

inp = get_data(day=1, year=2018)

nums = [int(x) for x in inp.splitlines()]

answer = sum(nums)
print(answer)

visited = set()
freq = 0
i = 0
while freq not in visited:
  visited.add(freq)
  freq += nums[i]
  i = (i + 1) % len(nums)

answer = freq
print(answer)
