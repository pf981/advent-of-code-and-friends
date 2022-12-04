# Databricks notebook source
# %pip install z3-solver

# COMMAND ----------

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

# z#!!!! 

# COMMAND ----------

# input_value = '12345678901234' # TODO
# input_i = 0
import collections
import random

def g(v, d):
  return d[v] if v in d else int(v)

save = collections.defaultdict(set)

def is_valid(input_value):
  global save
  line_i = 0
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
    if op == 'inp':
      z[input_i] = r['z']
      if input_i == 3:
        print(f'{z[1]=} {z[2]=} {z[3]=}')
        return # DEBUGGING
      r[args[0]] = int(input_value[input_i])
      input_i += 1
    elif op == 'add':
      r[args[0]] += g(args[1], r)
    elif op == 'mul':
      r[args[0]] *= g(args[1], r)
    elif op == 'div':
      r[args[0]] //= g(args[1], r)
    elif op == 'mod':
      r[args[0]] %= g(args[1], r)
    elif op == 'eql':
      r[args[0]] = int(r[args[0]] == g(args[1], r))
    else:
      print('err', op)
   #save[line_i].add(frozenset(r.items()))
#     r2 = r.copy()
#     del r2['w']
#     del r2['z']
#     save[line_i].add(frozenset(r2.items()))
    #print(line_i)
    line_i += 1
  return r['z'] == 0
# is_valid('12345678911234')

# iv = '99999999999999'
#while not is_valid(iv):
# for _ in range(1000):
#   iv = ''.join([random.choice('123456789') for _ in range(14)])
#   is_valid(iv)
#   while True:
#     iv = str(int(iv) - 1)
#     if '0' not in iv:
#       break
#iv

# COMMAND ----------

is_valid('11999999999999') # 16
is_valid('12999999999999') # 16
is_valid('13999999999999') # 16
is_valid('14999999999999') # 16
is_valid('15999999999999') # 16

# COMMAND ----------

# I think minimize z
# First digit is 1 makes z 16
# 2: 

# COMMAND ----------

a = 1
((a+15)%26)+12

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

z = z 

# COMMAND ----------

(16) * 26 + 1 + 5

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
