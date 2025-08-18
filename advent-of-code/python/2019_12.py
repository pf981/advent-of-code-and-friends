from aocd import get_data

inp = get_data(day=12, year=2019)

import copy
import re

def update_dimension(dimension):
  for pos_vel in dimension:
    pos_vel[1] += sum(1 if pos2 > pos_vel[0] else -1 for pos2, _ in dimension if pos2 != pos_vel[0])

  for pos_vel in dimension:
    pos_vel[0] += pos_vel[1]

start_state = list(zip(*[[[int(x), 0] for x in re.findall(r'-?\d+', line)] for line in inp.splitlines()]))

state = copy.deepcopy(start_state)
for _ in range(1000):
  for dimension in state:
    update_dimension(dimension)

answer = sum(sum(abs(pos) for pos, _ in moon) * sum(abs(vel) for _, vel in moon) for moon in zip(*state))
print(answer)

import functools
import itertools

def gcd(a, b):
  while b:      
    a, b = b, a % b
  return a

def lcm(a, b):
  return a * b // gcd(a, b)

def find_cycle(dimension):
  seen = set()
  for i in itertools.count():
    t = tuple(tuple(x) for x in dimension)
    if t in seen:
      return i
    seen.add(t)
    update_dimension(dimension)

cycles = [find_cycle(dimension) for dimension in copy.deepcopy(start_state)]

answer = functools.reduce(lcm, cycles)
print(answer)
