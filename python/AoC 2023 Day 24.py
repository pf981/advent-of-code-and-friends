from aocd import get_data

inp = get_data(day=24, year=2023)

from aocd import get_data, submit
import re
import z3


def does_intersect(px1, py1, pz1, vx1, vy1, vz1, px2, py2, pz2, vx2, vy2, vz2, test_min=200000000000000, test_max=400000000000000):
    X1 = z3.Real('X1')
    Y1 = z3.Real('Y1')
    T1 = z3.Real('T1')

    X2 = z3.Real('X2')
    Y2 = z3.Real('Y2')
    T2 = z3.Real('T2')

    # Optimize runs significantly faster than Solver for part 1
    # o = z3.Solver()
    o = z3.Optimize()

    o.add(X1 >= test_min)
    o.add(X1 <= test_max)
    o.add(Y1 >= test_min)
    o.add(Y1 <= test_max)
    o.add(T1 >= 0)

    o.add(X2 >= test_min)
    o.add(X2 <= test_max)
    o.add(Y2 >= test_min)
    o.add(Y2 <= test_max)
    o.add(T2 >= 0)

    o.add(X1 == px1 + vx1 * T1)
    o.add(Y1 == py1 + vy1 * T1)

    o.add(X2 == px2 + vx2 * T2)
    o.add(Y2 == py2 + vy2 * T2)

    o.add(X1 == X2)
    o.add(Y1 == Y2)

    return str(o.check()) == 'sat'


inp = get_data(day=24, year=2023)
stones = [[int(x) for x in re.findall(r'-?[0-9]+', line)] for line in inp.splitlines()]

answer1 = 0
for i, a in enumerate(stones):
    for j in range(i + 1, len(stones)):
        if does_intersect(*a, *stones[j]):
            answer1 += 1

print(answer1)

submit(answer1, part='a', day=24, year=2023)


# Part 2


import z3


# Solver runs significantly faster than Optimize for part 2
# o = z3.Optimize()
o = z3.Solver()

X0 = z3.Int('X0')
Y0 = z3.Int('Y0')
Z0 = z3.Int('Z0')
VX0 = z3.Int('VX0')
VY0 = z3.Int('VY0')
VZ0 = z3.Int('VZ0')


def add_rock(i, px1, py1, pz1, vx1, vy1, vz1):
    T1 = z3.Int('T' + str(i))
    o.add(T1 >= 0)
    o.add(px1 + vx1 * T1 == X0 + VX0 * T1)
    o.add(py1 + vy1 * T1 == Y0 + VY0 * T1)
    o.add(pz1 + vz1 * T1 == Z0 + VZ0 * T1)

answer = 0
for i, a in enumerate(stones):
    add_rock(i, *a)

o.check()
answer2 = o.model().eval(X0 + Y0 + Z0)
print(answer2)

submit(answer2, part='b', day=24, year=2023)
