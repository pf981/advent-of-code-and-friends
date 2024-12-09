from aocd import get_data

inp = get_data(day=11, year=2022)

import collections
import copy
import math
import re

monkeys_start = []
for lines in inp.split('\n\n'):
  lines = lines.splitlines()
  
  monkey_id = int(re.findall(r'\d+', lines[0])[0])
  starting_items = [int(item) for item in re.findall(r'\d+', lines[1])]
  op = eval('lambda old: ' + lines[2].split(' = ')[1])
  div = int(re.findall(r'\d+', lines[3])[0])
  monkey_true = int(re.findall(r'\d+', lines[4])[0])
  monkey_false = int(re.findall(r'\d+', lines[5])[0])
  
  monkeys_start.append((starting_items, op, div, monkey_true, monkey_false))

monkeys = copy.deepcopy(monkeys_start)
activity = collections.Counter()
for _ in range(20):
  for monkey, (items, op, div, monkey_true, monkey_false) in enumerate(monkeys):
    while items:
      activity[monkey] += 1
      item = items.pop(0)
      item = op(item)
      item //= 3
      if item % div == 0:
        monkeys[monkey_true][0].append(item)
      else:
        monkeys[monkey_false][0].append(item)

most_active = [monkey for _, monkey in activity.most_common(2)]
monkey_business = math.prod(most_active)
answer = monkey_business
print(answer)

lcm = math.lcm(*(div for _, _, div, _, _ in monkeys))

monkeys = copy.deepcopy(monkeys_start)
activity = collections.Counter()
for _ in range(10000):
  for monkey, (items, op, div, monkey_true, monkey_false) in enumerate(monkeys):
    while items:
      activity[monkey] += 1
      item = items.pop(0)
      item = op(item)
      if item % div == 0:
        monkeys[monkey_true][0].append(item % lcm)
      else:
        monkeys[monkey_false][0].append(item % lcm)

most_active = [monkey for _, monkey in activity.most_common(2)]
monkey_business = math.prod(most_active)
answer = monkey_business
print(answer)
