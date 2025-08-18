from aocd import get_data

inp = get_data(day=23, year=2018)

import re

bots = [[int(x) for x in re.findall(r'-?\d+', line)] for line in inp.splitlines()]
target_x, target_y, target_z, target_r = max(bots, key=lambda x: x[3])

answer = sum(abs(x - target_x) + abs(y - target_y) + abs(z - target_z) <= target_r for x, y, z, _ in bots)
print(answer)

import z3

def Abs(X):
  return z3.If(X >= 0, X, -X)

X = z3.Int('X')
Y = z3.Int('Y')
Z = z3.Int('Z')
D = z3.Int('D')

o = z3.Optimize()
o.add(D == Abs(X) + Abs(Y) + Abs(Z))
o.maximize(sum(z3.If(Abs(X - x) + Abs(Y - y) + Abs(Z - z) <= r, 1, 0) for x, y, z, r in bots))
o.minimize(D)
o.check()

answer = o.model()[D]
print(answer)
