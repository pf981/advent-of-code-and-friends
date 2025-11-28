from aocd import get_data

inp = get_data(day=16, year=2019)

def create_pattern(step, length_out):
  base_pattern = (0, 1, 0, -1)
  for i in range(1, length_out + 1):
    yield base_pattern[(i // step) % len(base_pattern)]

def process_phase(nums):
  base_pattern = (0, 1, 0, -1)
  for step, _ in enumerate(nums, 1):
    pattern = create_pattern(step, len(nums))
    yield (
      abs(sum(x * y for x, y in zip(nums, pattern))) % 10
    )

def solve(nums, n_phases=100):
  for _ in range(n_phases):
    nums = list(process_phase(nums))
  return nums

nums = [int(x) for x in inp]

result = solve(nums)

answer = ''.join(str(x) for x in result[:8])
print(answer)

def solve2(nums):
  offset = int(''.join(str(x) for x in nums[:7]))

  nums = (nums * 10000)[offset:]
  for _ in range(100):
    cumsum = 0
    nums = [cumsum := (cumsum + num) % 10 for num in nums[::-1]][::-1]
    
  return nums

result = solve2(nums)

answer = ''.join(str(x) for x in result[:8])
print(answer)
