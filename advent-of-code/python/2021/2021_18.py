from aocd import get_data

inp = get_data(day=18, year=2021)

import functools
import math


def parse_line(s):
  l = []
  num = ''
  for c in s:
    if c in '0123456789':
      num += c
    else:
      if num != '':
        l.append(int(num))
      num = ''
      l.append(c)
  return l


def snailfish_add(a, b):
  return snailfish_reduce(['['] + a + [','] + b + [']'])


def index_next_number_right(l, i):
  for index in range(i + 1, len(l)):
    if isinstance(l[index], int):
      return index


def index_next_number_left(l, i):
  for index in range(i - 1, -1, -1):
    if isinstance(l[index], int):
      return index


def explode(l):
  depth = -1
  for i, c in enumerate(l):
    if c == '[':
      depth += 1
    elif c == ']':
      depth -= 1
    elif c == ',':
      continue
    else:
      if depth == 4:
        index_left = i
        index_next_left = index_next_number_left(l, i)
        
        index_right = index_next_number_right(l, i)
        index_next_right = index_next_number_right(l, index_right)
        
        if index_next_left is not None:
          l[index_next_left] += l[index_left]
        if index_next_right is not None:
          l[index_next_right] += l[index_right]
          
        l[index_left] = 0
        del l[index_left + 1] # ,
        del l[index_left + 1] # right
        del l[index_left + 1] # ]
        del l[index_left - 1] # [
        return True
  return False


def split(l):
  for i, c in enumerate(l):
    if isinstance(c, int) and c >= 10:
      del l[i]
      l.insert(i, '[')
      l.insert(i+1, c // 2)
      l.insert(i+2, ',')
      l.insert(i+3, math.ceil(c / 2))
      l.insert(i+4, ']')
      return True
  return False


def snailfish_reduce(l):
  while True:
    if explode(l):
      continue
    if split(l):
      continue
    break
  return l


def get_magnitude_impl(l):
  if isinstance(l, int):
    return l
  return 3 * get_magnitude_impl(l[0]) + 2 * get_magnitude_impl(l[1])


def get_magnitude(l):
  return get_magnitude_impl(eval(''.join(str(s) for s in l)))
  

addends = [parse_line(line) for line in inp.splitlines()]

answer = get_magnitude(functools.reduce(snailfish_add, addends))
print(answer)

largest_magnitude = max(
  get_magnitude(snailfish_add(left, right))
  for left in addends
  for right in addends
  if left != right
)

answer = largest_magnitude
print(answer)
