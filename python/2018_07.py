from aocd import get_data

inp = get_data(day=7, year=2018)

import collections
import re
import string

def solve(remaining, dependencies):
  if len(remaining) == 1:
    return list(remaining)
  
  for s in remaining:
    if any(x in dependencies[s] for x in remaining):
      continue
    
    if (result := solve([x for x in remaining if x != s], dependencies)):
      return [s] + result
  return None

dependencies = collections.defaultdict(set)
for depends_on, step in (re.findall(r' ([A-Z]) ', line) for line in inp.splitlines()):
  dependencies[step].add(depends_on)

steps = solve(list(string.ascii_uppercase), dependencies)
  
answer = ''.join(steps)
print(answer)

import itertools

def solve2(steps, dependencies):
  time_remaining = {step: 60 + i for i, step in enumerate(sorted(steps), 1)}
  for t in itertools.count(1):
    workers = list(itertools.islice((s for s in time_remaining if all(x not in dependencies[s] for x in time_remaining)), 5))
    
    for step in workers:
      time_remaining[step] -= 1
      if time_remaining[step] == 0:
        del time_remaining[step]
    
    if not time_remaining:
      break
  return t
  
solve2(steps, dependencies)
