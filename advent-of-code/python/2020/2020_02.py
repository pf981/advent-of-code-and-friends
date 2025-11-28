from aocd import get_data

inp = get_data(day=2, year=2020)

import re

n_valid = 0
for least, most, c, s in re.findall(r'(\d+)-(\d+) (.): (.+)', inp):
  least = int(least)
  most = int(most)
  if least <= s.count(c) <= most:
    n_valid += 1

answer = n_valid
print(answer)

n_valid = 0
for i, j, c, s in re.findall(r'(\d+)-(\d+) (.): (.+)', inp):
  i = int(i)
  j = int(j)
  if (s[i - 1] == c) + (s[j - 1] == c) == 1:
    n_valid += 1

answer = n_valid
print(answer)
