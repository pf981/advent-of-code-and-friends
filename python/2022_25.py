from aocd import get_data

inp = get_data(day=25, year=2022)

import functools
import math


to_num = {
  '2': 2,
  '1': 1,
  '0': 0,
  '-': -1,
  '=': -2
}
to_string = {
  2: '2',
  1: '1',
  0: '0',
  -1: '-',
  -2: '='
}


def get_value(s):
  return sum((5 ** exponent) * to_num[c] for exponent, c in enumerate(s[::-1]))


@functools.cache
def make_string(target, digits):
  if digits == 1:
    return to_string.get(target)

  if abs(target) > 5 ** digits:
    return None
  
  coef = 5 ** (digits - 1)
  for value, c in to_string.items():
    if (result := make_string(target - value*coef, digits - 1)) is not None:
      return c + result
  return None


target = sum(get_value(line) for line in inp.splitlines())
digits_upper_bound = int(math.log(target, 5) + 2)
answer = make_string(target, digits_upper_bound).lstrip('0')
print(answer)

# No puzzle here - just need 49 stars.
