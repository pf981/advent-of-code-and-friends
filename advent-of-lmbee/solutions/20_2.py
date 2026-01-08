# Too slow
import re

import z3

with open("data/day20.txt") as f:
    text = f.read()
# text = """(4, 6) r=3
# (3, 7) r=1
# (12, 14) r=9
# (10, 6) r=5"""

circles = [[int(x) for x in re.findall(r"\d+", line)] for line in text.splitlines()]

o = z3.Optimize()

x_z3 = z3.Int("x")
y_z3 = z3.Int("y")

overlaps = [
    (x_z3 - x) * (x_z3 - x) + (y_z3 - y) * (y_z3 - y) < r * r for x, y, r in circles
]

overlap_sum = z3.Sum(z3.If(overlap, 1, 0) for overlap in overlaps)
o.maximize(overlap_sum)

check = o.check()
assert check == z3.sat

answer = o.model()[x_z3].py_value() * o.model()[y_z3].py_value()
print(answer)
