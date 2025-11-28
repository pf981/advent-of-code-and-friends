from aocd import get_data

inp = get_data(day=16, year=2015)

inp2 = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

import re

sues = {}
for line in inp.split('\n'):
  sue_id = re.search(r'\d+', line).group()
  sues[sue_id] = {key: int(value) for _, key, value in re.findall(r'((\w+): (\d))', line)}

target = {line.split(': ')[0]: int(line.split(': ')[1]) for line in inp2.split('\n')}

def matches(sue, target):
  for key, value in sue.items():
    if target[key] != value:
      return False
  return True

answer = next(sue_id for sue_id, sue in sues.items() if matches(sue, target))
answer

def matches2(sue, target):
  for key, value in sue.items():
    if key in ('cats', 'trees'):
      f = lambda a, b: a < b
    elif key in ('pomeranians', 'goldfish'):
      f = lambda a, b: a > b
    else:
      f = lambda a, b: a == b
    
    if not f(target[key], value):
      return False
  return True

answer = next(sue_id for sue_id, sue in sues.items() if matches2(sue, target))
answer
