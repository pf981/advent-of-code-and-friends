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

import collections
import random

def g(v, d):
  return d[v] if v in d else int(v)

def is_valid(input_value):
#   global save
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
      d = [int(a) for a in input_value]
      z[input_i] = r['z']
      if input_i == 1:
        assert(z[1] == int(input_value[0]) + 15)
      if input_i == 2:
        assert(z[2] == z[1] * 26 + int(input_value[1]) + 5)
      if input_i == 3:
        x = ((d[0] + 15) * 26 + d[1] + 5) % 26  + 13 != d[2]
        assert(z[3] ==  z[2] * (25 * x + 1) + (d[2] + 6) * x)
      if input_i == 4:
        x = ((z[3] % 26) - 14) != d[3]
        assert(r['x'] == x)
        assert(z[4] == z[3] // 26 * (25 * x + 1) + (d[3] + 7) * x)
      if input_i == 5:
        x = (z[4] % 26) + 15 != d[4]
        assert(r['x'] == x)
        assert(z[5] == z[4] * (25 * x + 1) + (d[4] + 9) * x)
      if input_i == 6:
        x = (z[5] % 26) - 7 != d[5]
        assert(r['x'] == x)
        assert(z[6] == z[5] // 26 * (25 * x + 1) + ((d[5] + 6) * x))
      if input_i == 7:
        x = (z[6] % 26) + 14 != d[6]
        assert(r['x'] == x)
        assert(z[7] == z[6] * (25 * x + 1) + (d[6] + 14) * x)
      if input_i == 8:
        x = (z[7] % 26) + 15 != d[7]
        assert(r['x'] == x)
        assert(z[8] == z[7] * (25 * x + 1) + (d[7] + 3) * x)
      if input_i == 9:
        x = (z[8] % 26) + 15 != d[8]
        assert(r['x'] == x)
        assert(z[9] == z[8] * (25 * x + 1) + (d[8] + 1) * x)
      if input_i == 10:
        x = (z[9] % 26) - 7 != d[9]
        assert(r['x'] == x)
        assert(z[10] == z[9] // 26 * (25 * x + 1) + (d[9] + 3) * x)
      if input_i == 11:
        x = (z[10] % 26) - 8 != d[10]
        assert(r['x'] == x)
        assert(z[11] == z[10] // 26 * (25 * x + 1) + (d[10] + 4) * x)
      if input_i == 12:
        x = (z[11] % 26) - 7 != d[11]
        assert(r['x'] == x)
        assert(z[12] == z[11] // 26 * (25 * x + 1) + (d[11] + 6) * x)
      if input_i == 13:
        x = (z[12] % 26) - 5 != d[12]
        assert(r['x'] == x)
        assert(z[13] == z[12] // 26 * (25 * x + 1) + (d[12] + 7) * x)
      if input_i == 14:
        x = (z[13] % 26) - 10 != d[13]
        assert(r['x'] == x)
        assert(z[14] == z[13] // 26 * (25 * x + 1) + (d[13] + 1) * x)
        
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

    line_i += 1
  #return z
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
          11167118139116

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

is_valid('49917929934999')

# COMMAND ----------

is_valid('11911316711816')

# COMMAND ----------

is_valid('21911316711810')

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
