from aocd import get_data

inp = get_data(day=17, year=2017)

inp = 348

import collections

def solve(skip):
  buffer = collections.deque()
  
  for i in range(2018):
    buffer.rotate(-skip)
    buffer.appendleft(i)
    buffer.rotate(-1)
  
  return buffer[0]

answer = solve(inp)
print(answer)

def solve2(skip):
  buffer_size = 1
  i = 0
  for iteration in range(50000000):
    i = ((i + skip) % buffer_size) + 1
    buffer_size += 1
    if (i == 1):
      result = iteration + 1
  return result

answer = solve2(inp)
print(answer)
