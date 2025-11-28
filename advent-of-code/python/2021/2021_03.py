from aocd import get_data

inp = get_data(day=3, year=2021)

nums = inp.splitlines()

gamma_b = ''.join(max('01', key = digits.count) for digits in zip(*nums))
epsilon_b = ''.join('1' if x == '0' else '0' for x in gamma_b)

gamma = int(gamma_b, 2)
epsilon = int(epsilon_b, 2)

answer = epsilon * gamma
print(answer)

def get_rate(nums, f, default):
  nums = nums.copy()
  for i in range(len(nums[0])):
    digits = [num[i] for num in nums]
    counts = [digits.count(digit) for digit in '01']
    keep = default if counts[0] == counts[1] else f('01', key = digits.count)
    nums = [num for num in nums if num[i] == keep]

    if len(nums) == 1:
      return int(nums[0], 2)

oxygen_generator_rating = get_rate(nums, max, '1')
co2_scrubber_rating = get_rate(nums, min, '0')

answer = oxygen_generator_rating * co2_scrubber_rating
print(answer)
