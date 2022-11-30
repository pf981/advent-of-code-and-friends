# Databricks notebook source
# MAGIC %pip install z3-solver

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

import z3


# w = z3.Int('w')
# x = z3.Int('x')
# y = z3.Int('y')
# z = z3.Int('z')

d14 = z3.Int('d14')
d13 = z3.Int('d13')
d12 = z3.Int('d12')
d11 = z3.Int('d11')
d10 = z3.Int('d10')
d9 = z3.Int('d9')
d8 = z3.Int('d8')
d7 = z3.Int('d7')
d6 = z3.Int('d6')
d5 = z3.Int('d5')
d4 = z3.Int('d4')
d3 = z3.Int('d3')
d2 = z3.Int('d2')
d1 = z3.Int('d1')

o = z3.Optimize()

o.add(z3.And(d14 > 0, d14 < 10))
o.add(z3.And(d13 > 0, d13 < 10))
o.add(z3.And(d12 > 0, d12 < 10))
o.add(z3.And(d11 > 0, d11 < 10))
o.add(z3.And(d10 > 0, d10 < 10))
o.add(z3.And(d9 > 0, d9 < 10))
o.add(z3.And(d8 > 0, d8 < 10))
o.add(z3.And(d7 > 0, d7 < 10))
o.add(z3.And(d6 > 0, d6 < 10))
o.add(z3.And(d5 > 0, d5 < 10))
o.add(z3.And(d4 > 0, d4 < 10))
o.add(z3.And(d3 > 0, d3 < 10))
o.add(z3.And(d2 > 0, d2 < 10))
o.add(z3.And(d1 > 0, d1 < 10))

# o.add(z == 0)

o.maximize(int(1e13)*d14+int(1e12)*d13+int(1e11)*d12+int(1e10)*d11+int(1e9)*d10+int(1e8)*d9+int(1e7)*d8+int(1e6)*d7+int(1e5)*d6+int(1e4)*d5+int(1e3)*d4+int(1e2)*d3+int(1e1)*d2+int(1e0)*d1)


# COMMAND ----------

input_i = 1

cur_vars =  {
  'w': 0,
  'x': 0,
  'y': 0,
  'z': 0,
  'd14': 0,
  'd13': 0,
  'd12': 0,
  'd11': 0,
  'd10': 0,
  'd9': 0,
  'd8': 0,
  'd7': 0,
  'd6': 0,
  'd5': 0,
  'd4': 0,
  'd3': 0,
  'd2': 0,
  'd1': 0
}

def get_var(x, is_new=False):
  global cur_vars
  try:
    return int(x)
  except ValueError:
    pass

  if 'd' in x:
    return z3.Int(x)
  
  if is_new:
    cur_vars[x] += 1
  return z3.Int(f'{x}{cur_vars[x]}')

for line in inp.splitlines():
  op, *args = line.split(' ')
  if op == 'inp':
    o.add(get_var(args[0], True) == get_var(f'd{input_i}'))
    input_i += 1
  elif op == 'add':
    old = get_var(args[0])
    o.add(get_var(args[0], True) == old + get_var(args[1]))
  elif op == 'mul':
    old = get_var(args[0])
    o.add(get_var(args[0], True) == old * get_var(args[1]))
  elif op == 'div':
    old = get_var(args[0])
    o.add(get_var(args[0], True) == old / get_var(args[1])) # FIXME Is this integer division?
  elif op == 'mod':
    old = get_var(args[0])
    o.add(get_var(args[0], True) == old % get_var(args[1]))
  elif op == 'eql':
    old = get_var(args[0])
    o.add(get_var(args[0], True) == (old == get_var(args[1])))
  else:
    print('err', op)
    
o.add(get_var('z') == 0)

# COMMAND ----------

o.check()

# COMMAND ----------

o.model()

# COMMAND ----------

l = list(o.model())

# COMMAND ----------

''.join(o.model()[get_var(f'D{i}')] for i in range(1, 15))

# COMMAND ----------

# o = z3.Optimize()
# a = z3.Int('a')
# b = z3.Int('b')
# #o.add(b == z3.If(a == 1, 1, 0))
# o.add(a == 1)
# # o.add(b == (a == 1))
# o.check()

# COMMAND ----------

# o.model()
