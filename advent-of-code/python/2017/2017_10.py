from aocd import get_data

inp = get_data(day=10, year=2017)

import collections
import math

def reverse(nums, n):
  rev = collections.deque()

  for _ in range(n):
    rev.append(nums.popleft())
  
  while rev:
    nums.appendleft(rev.popleft())

def hash_lengths(lengths, n_rounds=1):
  nums = collections.deque(range(256))
  skip_size = 0
  total_rotation = 0
  
  for _ in range(n_rounds):
    for length in lengths:
      reverse(nums, length)

      rotation = length + skip_size
      total_rotation += rotation
      nums.rotate(-rotation)

      skip_size += 1
  
  nums.rotate(total_rotation)
  return list(nums)

lengths = [int(x) for x in inp.split(',')]

answer = math.prod(hash_lengths(lengths)[:2])
print(answer)

import functools
import operator

def get_knot_hash(s):
  lengths = [ord(c) for c in inp] + [17, 31, 73, 47, 23]
  sparse_hash = hash_lengths(lengths, n_rounds=64)
  dense_hash = [functools.reduce(operator.xor, l) for l in zip(*[iter(sparse_hash)] * 16)]
  return ''.join(f'{i:0>2x}' for i in dense_hash)

answer = get_knot_hash(inp)
print(answer)
