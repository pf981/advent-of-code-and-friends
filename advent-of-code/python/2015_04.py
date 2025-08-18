from aocd import get_data

inp = get_data(day=4, year=2015)

import hashlib
import itertools

def solve(prefix, n_zeroes):
  for i in itertools.count(1):
    if (hashlib.md5(f'{inp}{i}'.encode('utf-8')).hexdigest().startswith('0' * n_zeroes)):
      return i

answer = solve(inp, 5)
answer

answer = solve(inp, 6)
answer
