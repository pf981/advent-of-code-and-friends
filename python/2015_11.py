from aocd import get_data

inp = get_data(day=11, year=2015)

def is_valid(l):
  doubles = set()
  contains_straight = False
  
  prev_val = -99
  for val in l:
    if val == prev_val:
      doubles.add(val)
    
    if val == prev_val + 1:
      n_sequential += 1
      if n_sequential == 2:
        contains_straight = True
    else:
      n_sequential = 0

    prev_val = val
  return len(doubles) > 1 and contains_straight

def increment(l, i):
  l[i] += 1
  if l[i] == 123:
    l[i] = 97
    increment(l, i - 1)
  if l[i] in (105, 111, 108):
    l[i] += 1

def next_password(s):
  l = [ord(c) for c in s]
  while True:
    increment(l, len(l) - 1)
    if is_valid(l):
      return ''.join(chr(x) for x in l)

answer = next_password(inp)
answer

answer = next_password(answer)
answer
