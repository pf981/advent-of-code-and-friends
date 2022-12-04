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


o = z3.Optimize()

for i in range(14):
  d = z3.Int(f'd{i}')
  o.add(z3.And(d > 0, d < 10))

d0 = z3.Int('d0')
d1 = z3.Int('d1')
d2 = z3.Int('d2')
d3 = z3.Int('d3')
d4 = z3.Int('d4')
d5 = z3.Int('d5')
d6 = z3.Int('d6')
d7 = z3.Int('d7')
d8 = z3.Int('d8')
d9 = z3.Int('d9')
d10 = z3.Int('d10')
d11 = z3.Int('d11')
d12 = z3.Int('d12')
d13 = z3.Int('d13')

  
z1 = z3.Int('z1')
z2 = z3.Int('z2')
zz3 = z3.Int('z3')
z4 = z3.Int('z4')
z5 = z3.Int('z5')
z6 = z3.Int('z6')
z7 = z3.Int('z7')
z8 = z3.Int('z8')
z9 = z3.Int('z9')
z10 = z3.Int('z10')
z11 = z3.Int('z11')
z12 = z3.Int('z12')
z13 = z3.Int('z13')
z14 = z3.Int('z14')
  
o.add(z1 == d0 + 15)
o.add(z2 == z1 * 26 + d1 + 5)
o.add(zz3 == z2 * (25 + 1) + (d2 + 6))
o.add(z4 == zz3 / 26 * (25 + 1) + (d3 + 7))
o.add(z5 == z4 * (25 + 1) + (d4 + 9))
o.add(z6 == z5 / 26 * (25 + 1) + ((d5 + 6)))
o.add(z7 == z6 * (25 + 1) + (d6 + 14))
o.add(z8 == z7 * (25 + 1) + (d7 + 3))
o.add(z9 == z8 * (25 + 1) + (d8 + 1))
o.add(z10 == z9 / 26 * (25 + 1) + (d9 + 3))
o.add(z11 == z10 / 26 * (25 + 1) + (d10 + 4))
o.add(z12 == z11 / 26 * (25 + 1) + (d11 + 6))
o.add(z13 == z12 / 26 * (25 + 1) + (d12 + 7))
o.add(z14 == z13 / 26 * (25 + 1) + (d13 + 1))

o.add(z14 == 0)
o.maximize(sum(10**i * z3.Int(f'd{i}') for i in range(14)))

# COMMAND ----------

o.check()

# COMMAND ----------

answer = ''.join(o.model()[z3.Int(f'd{i}')].as_string() for i in range(14))
print(answer)
