from aocd import get_data

inp = get_data(day=13, year=2020)

import math

start, buses = inp.splitlines()
start = int(start)
buses = {i: int(x) for i, x in enumerate(buses.split(',')) if x != 'x'}

t, bus = min((bus * math.ceil(start / bus), bus) for bus in buses.values())

answer = (t - start) * bus
print(answer)

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
import functools

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
      return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    s = 0
    prod = functools.reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod

mod = buses.values()
a = [(bus - i) % bus for i, bus in buses.items()]

answer = chinese_remainder(mod, a)
print(answer)
