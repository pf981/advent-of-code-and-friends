# Databricks notebook source
inp = '''inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y'''

# COMMAND ----------

import functools

ops = [line.split(' ') for line in inp.splitlines()]

def run(step, input_z, digit):
  input_i = 0
  r = {
    'w': digit,
    'x': 0,
    'y': 0,
    'z': input_z,
  }
  for i in range(18 * step + 1, 18 * (step + 1)):
    op, *args = ops[i]
    arg_values = [r[arg] if arg in r else int(arg) for arg in args]

    if op == 'add':
      r[args[0]] += arg_values[1]
    elif op == 'mul':
      r[args[0]] *= arg_values[1]
    elif op == 'div':
      r[args[0]] //= arg_values[1]
    elif op == 'mod':
      r[args[0]] %= arg_values[1]
    elif op == 'eql':
      r[args[0]] = int(arg_values[0] == arg_values[1])

  return r['z']

@functools.lru_cache(maxsize=None)
def solve(step, input_z):

  for digit in range(1, 10):
    output_z = run(step, input_z, digit)
    if step == 13: # TODO Check
      if output_z == 0: 
        return str(digit)
    else:
      other_digits = solve(step + 1, output_z)

      if other_digits is not None:
        return str(digit) + other_digits
    
solve.cache_clear()
solve(0, 0)

# COMMAND ----------

# import functools

# ops = [line.split(' ') for line in inp.splitlines()]

# def run(step, input_z, digit):
#   input_i = 0
#   r = {
#     'w': digit,
#     'x': 0,
#     'y': 0,
#     'z': input_z,
#   }
#   for i in range(18 * step + 1, 18 * (step + 1)):
#     op, *args = ops[i]
#     arg_values = [r[arg] if arg in r else int(arg) for arg in args]

#     if op == 'add':
#       r[args[0]] += arg_values[1]
#     elif op == 'mul':
#       r[args[0]] *= arg_values[1]
#     elif op == 'div':
#       r[args[0]] //= arg_values[1]
#     elif op == 'mod':
#       r[args[0]] %= arg_values[1]
#     elif op == 'eql':
#       r[args[0]] = int(arg_values[0] == arg_values[1])

#   return r['z']

# @functools.lru_cache(maxsize=None)
# def solve(step, input_z):
#   if step == 14 and input_z == 0: # TODO Check
#     return ''

#   for digit in range(1, 10):
#     output_z = run(step, input_z, digit)
#     other_digits = solve(step + 1, output_z)

#     if other_digits is not None:
#       return str(digit) + other_digits
    
# solve.cache_clear()
# solve(0, 0)

# COMMAND ----------

len(ops)

# COMMAND ----------

14*18

# COMMAND ----------

[i for i, (v, *_) in enumerate(ops) if v == 'inp']

# COMMAND ----------

ops[18]

# COMMAND ----------

[18*i for i in range(14)]

# COMMAND ----------

def is_valid(input_value):
  input_i = 0
  r = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
  }
  z = {}
  for line in inp.splitlines():
    op, *args = line.split(' ')
    arg_values = [r[arg] if arg in r else int(arg) for arg in args]

    if op == 'inp':
      r[args[0]] = int(input_value[input_i])
      input_i += 1
    elif op == 'add':
      r[args[0]] += arg_values[1]
    elif op == 'mul':
      r[args[0]] *= arg_values[1]
    elif op == 'div':
      r[args[0]] //= arg_values[1]
    elif op == 'mod':
      r[args[0]] %= arg_values[1]
    elif op == 'eql':
      r[args[0]] = int(arg_values[0] == arg_values[1])

  return r['z'] == 0

is_valid('12345678912345') 
is_valid('99999999999999')
is_valid('11111111111111')

# COMMAND ----------

is_valid('49917929934999')

# COMMAND ----------

for i in range(1, 10):
  s = f'{i}'
  if is_valid(s):
    break
print(s)

# COMMAND ----------

is_valid('11999999999999') # 16
is_valid('12999999999999') # 16
is_valid('13999999999999') # 16
is_valid('14999999999999') # 16
is_valid('15999999999999') # 16

# COMMAND ----------

valid_s = set()
#for _ in range(10000):
while True:
  iv = ''.join([random.choice('123456789') for _ in range(14)])
  # print(iv)
  if is_valid(iv):
    valid_s.add(iv)
    break
valid_s

# COMMAND ----------

valid_s = set()
for _ in range(10000):
  iv = ''.join([random.choice('123456789') for _ in range(14)])
  print(iv)
  if is_valid(iv):
    valid_s.add(iv)
valid_s

# COMMAND ----------

is_valid('11999999999999') # 16
is_valid('12999999999999') # 16
is_valid('13999999999999') # 16
is_valid('14999999999999') # 16
is_valid('15999999999999') # 16

# COMMAND ----------

is_valid('21999999999999') # 16
is_valid('22999999999999') # 16
is_valid('23999999999999') # 16
is_valid('24999999999999') # 16
is_valid('25999999999999') # 16

# COMMAND ----------

2+15+1+5

# COMMAND ----------

# inp = '''
# '''

# COMMAND ----------

# # input_value = '12345678901234' # TODO
# # input_i = 0
# import collections
# import random

# def g(v, d):
#   return d[v] if v in d else int(v)

# save = collections.defaultdict(set)

# def is_valid(input_value):
#   global save
#   line_i = 0
#   input_i = 0
#   r = {
#     'w': 0,
#     'x': 0,
#     'y': 0,
#     'z': 0,
#   }
#   for line in inp.splitlines():
#     op, *args = line.split(' ')
#     if op == 'inp':
#       r[args[0]] = int(input_value[input_i])
#       input_i += 1
#     elif op == 'add':
#       #print(line)
#       #print(r[args[0]], g(args[1], r), g(args[1], r)=='1')
#       r[args[0]] += g(args[1], r)
#     elif op == 'mul':
#       r[args[0]] *= g(args[1], r)
#     elif op == 'div':
#       r[args[0]] //= g(args[1], r)
#     elif op == 'mod':
#       r[args[0]] %= g(args[1], r)
#     elif op == 'eql':
#       r[args[0]] = int(r[args[0]] == g(args[1], r))
#     else:
#       print('err', op)
#    #save[line_i].add(frozenset(r.items()))
#     r2 = r.copy()
#     del r2['w']
#     del r2['z']
#     save[line_i].add(frozenset(r2.items()))
#     #print(line_i)
#     line_i += 1
#   return r['z'] == 0
# # is_valid('12345678911234')

# # iv = '99999999999999'
# #while not is_valid(iv):
# for _ in range(1000):
#   iv = ''.join([random.choice('123456789') for _ in range(14)])
#   is_valid(iv)
# #   while True:
# #     iv = str(int(iv) - 1)
# #     if '0' not in iv:
# #       break
# iv

# COMMAND ----------

for i, s in save.items():
  print(i, len(s))
  #print(i, s)

# COMMAND ----------

inp.splitlines()[157]

# COMMAND ----------

save[157]

# COMMAND ----------

save[197]

# COMMAND ----------

list(enumerate(inp.splitlines(197)))

# COMMAND ----------

# # input_value = '12345678901234' # TODO
# # input_i = 0

# def g(v, d):
#   return d[v] if v in d else int(v)



# def is_valid(input_value):
  
#   input_i = 0
#   r = {
#     'w': 0,
#     'x': 0,
#     'y': 0,
#     'z': 0,
#   }
#   for line in inp.splitlines():
#     op, *args = line.split(' ')
#     if op == 'inp':
#       r[args[0]] = int(input_value[input_i])
#       input_i += 1
#     elif op == 'add':
#       #print(line)
#       #print(r[args[0]], g(args[1], r), g(args[1], r)=='1')
#       r[args[0]] += g(args[1], r)
#     elif op == 'mul':
#       r[args[0]] *= g(args[1], r)
#     elif op == 'div':
#       r[args[0]] /= g(args[1], r)
#     elif op == 'mod':
#       r[args[0]] %= g(args[1], r)
#     elif op == 'eql':
#       r[args[0]] = int(r[args[0]] == g(args[1], r))
#     else:
#       print('err', op)

#   return r['z'] == 0
# # is_valid('12345678911234')

# iv = '99999999999999'
# #while not is_valid(iv):
# for _ in range(100):
#   while True:
#     iv = str(int(iv) - 1)
#     if '0' not in iv:
#       break
# iv

# COMMAND ----------

is_valid('12345678911234')

# COMMAND ----------

14 digit number. no 0s

# COMMAND ----------

# input_value = '12345678901234' # TODO
# input_i = 0

# def g(v, d):
#   return d[v] if v in d else int(v)

# r = {
#   'w': 0,
#   'x': 0,
#   'y': 0,
#   'z': 0,
# }
# for line in inp.splitlines():
#   op, *args = line.split(' ')
#   if op == 'inp':
#     r[args[0]] = input_value[i]
#     i += 1
#   elif op == 'add':
#     r[args[0]] += g(args[1], r)
#   elif op == 'mul':
#     r[args[0]] *= g(args[1], r)
#   elif op == 'div':
#     r[args[0]] /= g(args[1], r)
#   elif op == 'mod':
#     r[args[0]] %= g(args[1], r)
#   elif op == 'eql':
#     r[args[0]] = int(r[args[0]] == g(args[1], r))
#   else:
#     print('err', op)
    
# r

# COMMAND ----------

a=1
a/=0

# COMMAND ----------

a = 6
a %= 5
a

# COMMAND ----------

int('a')

# COMMAND ----------

import collections

a = collections.defaultdict(lambda i: i)
a[1]

# COMMAND ----------

# I think the secret lies in the NEGATIVE numbers - that is the only way z can get back to 0
