from aocd import get_data

inp = get_data(day=4, year=2019)

import re

def satisfies_criteria(candidate):
  contains_double = re.search(r'(.)\1', candidate)
  is_non_decreasing = all(a <= b for a, b in zip(candidate, candidate[1:]))
  return bool(contains_double and is_non_decreasing)

range_min, range_max = (int(x) for x in inp.split('-'))

answer = sum(satisfies_criteria(str(candidate)) for candidate in range(range_min, range_max+1))
print(answer)

answer = sum(satisfies_criteria(re.sub(r'(.)\1\1+', r'\1', str(candidate))) for candidate in range(range_min, range_max+1))
print(answer)
