from aocd import get_data

inp = get_data(day=6, year=2020)

groups = [group.splitlines() for group in inp.split('\n\n')]
answer = sum(len(set(''.join(group))) for group in groups)
print(answer)

import collections

answer = 0
for group in groups:
  answer += sum(cnt == len(group) for cnt in collections.Counter(''.join(group)).values())
  
print(answer)
