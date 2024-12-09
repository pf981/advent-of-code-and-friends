from aocd import get_data

inp = get_data(day=14, year=2021)

import collections
import functools

starting_polymer, inserts = inp.split('\n\n')
inserts = dict(line.split(' -> ') for line in inserts.splitlines())


@functools.lru_cache(maxsize=None)
def get_counts(polymer, n_steps):
  if n_steps == 0:
    return collections.Counter(polymer)
  
  if len(polymer) == 2:
    middle = inserts[polymer]
    left, right = polymer
    n_steps -= 1
  else:
    left, middle, *right = polymer
    right = ''.join(right)
    
  return get_counts(left + middle, n_steps) + get_counts(middle + right, n_steps) - collections.Counter(middle)


def solve(polymer, n_steps):
  counts = get_counts(polymer, n_steps)
  most_common, *_, least_common = (count for _, count in counts.most_common())
  return most_common - least_common


get_counts.cache_clear()

answer = solve(starting_polymer, 10)
print(answer)

answer = solve(starting_polymer, 40)
print(answer)
