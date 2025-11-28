from aocd import get_data

inp = get_data(day=13, year=2022)

import copy

def cmp(a, b):
  a = copy.deepcopy(a)
  b = copy.deepcopy(b)
  
  if isinstance(a, int) and isinstance(b, int):
    if a < b:
      return 1
    if a > b:
      return -1
    return 0
  
  if isinstance(a, list) and isinstance(b, list):
    if not a and not b:
      return 0
    if not a:
      return 1
    if not b:
      return -1
    
    return cmp(a.pop(0), b.pop(0)) or cmp(a, b)
  
  if isinstance(a, int):
    return cmp([a], b)
  return cmp(a, [b])


pairs = [[eval(s) for s in pair.splitlines()] for pair in inp.split('\n\n')]

answer = sum(i for i, (a, b) in enumerate(pairs, 1) if cmp(a, b) == 1)
print(answer)

import functools

packets = [packet for pair in pairs for packet in pair]
packets.append([[2]])
packets.append([[6]])

packets.sort(key=functools.cmp_to_key(cmp), reverse=True)

answer = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
print(answer)
