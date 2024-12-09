from aocd import get_data

inp = get_data(day=3, year=2022)

import string

items = inp.splitlines()
alphabet = '0' + string.ascii_letters

total = 0
for line in items:
  half = len(line) // 2
  a = set(line[:half])
  b = set(line[half:])
  intersection = a.intersection(b)
  total += alphabet.index(next(iter(intersection)))

answer = total
print(answer)

total = 0
for i in range(0, len(items), 3):
  a, b, c = (set(s) for s in items[i:i+3])
  intersection = a.intersection(b).intersection(c)
  total += alphabet.index(next(iter(intersection)))

answer = total
print(answer)
