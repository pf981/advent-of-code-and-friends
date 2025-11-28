from aocd import get_data

inp = get_data(day=14, year=2019)

import collections
import math
import re

def calculate_required_ore(reactions, n_fuel=1):
  leftovers = collections.defaultdict(int)
  total_ore = 0
  targets = collections.defaultdict(int, {'FUEL': n_fuel})
  
  while targets:
    target_chemical, target_n = targets.popitem()
    
    n_from_leftovers = min(leftovers[target_chemical], target_n)
    target_n -= n_from_leftovers
    leftovers[target_chemical] -= n_from_leftovers
    
    if target_n == 0:
      continue
    
    n_out, reagents = reactions[target_chemical]

    n_batches = math.ceil(target_n / n_out)
    n_out_created = n_batches * n_out
    n_out_leftover = n_out_created - target_n
    
    leftovers[target_chemical] += n_out_leftover
    
    for chemical_in, n_in in reagents:
      n_in *= n_batches

      n_in_from_leftovers = min(leftovers[chemical_in], n_in)
      n_in -= n_in_from_leftovers
      leftovers[chemical_in] -= n_in_from_leftovers

      if n_in == 0:
        continue
      
      if chemical_in == 'ORE':
        total_ore += n_in
      else:
        targets[chemical_in] += n_in
  
  return total_ore


reactions = {
  reagents[-1][0]: (reagents[-1][1], reagents[:-1])
  for reagents in [
    list(
        zip(re.findall(r'[A-Z]+', line), [int(x) for x in re.findall(r'\d+', line)])
    )
    for line in inp.splitlines()
  ]
}

answer = calculate_required_ore(reactions)
print(answer)

target = 1000000000000
low = 1
high = float('inf')
while low < high - 1:
  if math.isinf(high):
    mid = low * 10
  else:
    mid = (low + high) // 2
  
  result = calculate_required_ore(reactions, mid)
  
  if result < target:
    low = mid
  elif result > target:
    high = mid
  else:
    low = mid
    break

answer = low
print(answer)
