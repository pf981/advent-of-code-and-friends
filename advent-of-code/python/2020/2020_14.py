from aocd import get_data

inp = get_data(day=14, year=2020)

import re

mem = {}
for instruction in inp.splitlines():
  if instruction.startswith('mask'):
    mask = instruction.split(' = ')[1]
    mask_or = int(mask.replace('X', '0'), 2)
    mask_and = int(mask.replace('X', '1'), 2)
    continue

  address, value = re.findall(r'\d+', instruction)
  address = int(address)
  value = int(value)
  value |= mask_or
  value &= mask_and
  mem[address] = value

answer = sum(mem.values())
print(answer)

import functools
import itertools

mem = {}
for instruction in inp.splitlines():
  if instruction.startswith('mask'):
    mask = instruction.split(' = ')[1]
    mask_or = int(mask.replace('X', '0'), 2)
    
    masks = [0]
    for i, c in enumerate(mask):
      if c == 'X':
        masks.append(2 ** (len(mask) - i - 1))
    
    xors = []
    for n in range(1, len(masks) + 1):
      for comb in itertools.combinations(masks, n):
        xors.append(functools.reduce(lambda a, b: a | b, comb))
    continue

  address, value = re.findall(r'\d+', instruction)
  address = int(address)
  value = int(value)
  address |= mask_or
  
  for xor in xors:
    new_address = address ^ xor
    mem[new_address] = value

answer = sum(mem.values())
print(answer)
