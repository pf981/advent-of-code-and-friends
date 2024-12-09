from aocd import get_data

inp = get_data(day=24, year=2015)

# This is a nifty solution using z3 but it is too slow

# import z3

# o = z3.Optimize()

# group0_count = group1_count = group2_count = 0
# group0_weight = group1_weight = group2_weight = 0
# group0_quantum_entanglement = 1
# for i, weight in enumerate(int(x) for x in inp.split('\n')):
#   present_group = z3.Int(f'x{i}') 
#   o.add(present_group >= 0)
#   o.add(present_group < 3)
  
#   group0_count += z3.If(present_group == 0, 1, 0)
#   group0_quantum_entanglement = group0_quantum_entanglement * z3.If(present_group == 0, weight, 1)
  
#   group0_weight += z3.If(present_group == 0, weight, 0)
#   group1_weight += z3.If(present_group == 1, weight, 0)
#   group2_weight += z3.If(present_group == 2, weight, 0)

# o.add(group0_weight == group1_weight)
# o.add(group0_weight == group2_weight)

# qe = z3.Int('qe')
# o.add(qe = group0_quantum_entanglement)

# o.minimize(group0_count)
# o.minimize(qe)

# o.check()
# o.model()[qe]

from itertools import combinations
from math import prod

weights = set(int(x) for x in inp.split('\n'))

def solve(weights, n_groups = 3):
  min_quantum_entanglement = float('inf')
  for group0_size in range(len(weights) + 1):
    for group0 in combinations(weights, group0_size):
      if sum(group0) == sum(weights) / n_groups:
        min_quantum_entanglement = min(prod(group0), min_quantum_entanglement)
    if min_quantum_entanglement != float('inf'):
      return min_quantum_entanglement

answer = solve(weights)
answer

answer = solve(weights, 4)
answer
