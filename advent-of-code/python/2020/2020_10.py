from aocd import get_data

inp = get_data(day=10, year=2020)

joltages = [int(x) for x in inp.splitlines()]
joltages.sort()
joltages.append(3 + joltages[-1])
joltages.insert(0, 0)

z = list(zip(joltages[:-1], joltages[1:]))
one_jolt = sum(b == a + 1 for a, b in z)
three_jolt = sum(b == a + 3 for a, b in z)

answer = one_jolt * three_jolt
print(answer)

import functools

@functools.cache
def count_ways(i):
  if i == len(joltages) - 1:
    return 1
  
  ways = 0
  j = i + 1
  while j < len(joltages) and joltages[j] <= joltages[i] + 3:
    ways += count_ways(j)
    j += 1
  return ways

answer = count_ways(0)
print(answer)
