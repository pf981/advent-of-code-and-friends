import functools

with open("./2024/input/everybody_codes_e2024_q09_p1.txt") as f:
    lines = f.read().splitlines()

# # FIXME: REMOVE
# lines = '''2
# 4
# 7
# 16'''.splitlines()

# 1, 3, 5, 10
stamps = [1, 3, 5, 10]

@functools.cache
def min_stamps(i, target):
    # print(f'{i=} {target=}')
    if i == len(stamps):
        if target == 0:
            return 0
        return float('inf')

    best = float('inf')
    for n in range(target // stamps[i] + 1):
        required = n + min_stamps(i + 1, target - n * stamps[i])
        best = min(best, required)
    return best

nums = [int(line) for line in lines]
answer1 = 0
for num in nums:
    answer1 += min_stamps(0, num)

print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q09_p2.txt") as f:
    lines = f.read().splitlines()

# FIXME: REMOVE
# lines = '''33
# 41
# 55
# 99'''.splitlines()

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

@functools.cache
def min_stamps(i, target):
    # print(f'{i=} {target=}')
    # if i == len(stamps):
    #     if target == 0:
    #         return 0
    #     return float('inf')
    if i == len(stamps) - 1:
        if target % stamps[len(stamps) - 1] == 0:
            return target // stamps[len(stamps) - 1]
        return float('inf')

    best = float('inf')
    for n in range(target // stamps[i] + 1):
        required = n + min_stamps(i + 1, target - n * stamps[i])
        best = min(best, required)
    return best

nums = [int(line) for line in lines]
answer2 = 0
for num in nums:
    answer2 += min_stamps(0, num)

print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q09_p3.txt") as f:
    lines = f.read().splitlines()

# FIXME: REMOVE
lines = '''156488
352486
546212'''.splitlines()

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
stamps.sort(reverse=True)

@functools.cache
def min_stamps(i, target):
    # print(f'{i=} {target=}')
    if i == len(stamps) - 1:
        if target % stamps[len(stamps) - 1] == 0:
            return target // stamps[len(stamps) - 1]
        return float('inf')

    best = float('inf')
    for n in range(target // stamps[i] + 1):
        required = n + min_stamps(i + 1, target - n * stamps[i])
        best = min(best, required)
    return best

nums = [int(line) for line in lines]
answer3 = 0
for num in nums:
    best = float('inf')
    a = num // 2
    b = num - a
    while abs(a - b) <= 100:
        print(f'{a=} {b=} {a+b=} {num=}')
        best = min(
            best,
            min_stamps(0, a) + min_stamps(0, b)
        )
        a -= 1
        b = num - a
    answer3 += best

print(answer3)


# 156488 -> 78275 + 78213
# 78275 = 775*101
# 78213 = 774*101 + 39 = 774*101 + 38 + 1> 776


import z3

def z3abs(x):
    return z3.If(x >= 0, x, -x)

def solve(target: int) -> int:
    o = z3.Optimize()

    # stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    x1 = z3.Int('x1')
    x3 = z3.Int('x3')
    x5 = z3.Int('x5')
    x10 = z3.Int('x10')
    x15 = z3.Int('x15')
    x16 = z3.Int('x16')
    x20 = z3.Int('x20')
    x24 = z3.Int('x24')
    x25 = z3.Int('x25')
    x30 = z3.Int('x30')
    x37 = z3.Int('x37')
    x38 = z3.Int('x38')
    x49 = z3.Int('x49')
    x50 = z3.Int('x50')
    x74 = z3.Int('x74')
    x75 = z3.Int('x75')
    x100 = z3.Int('x100')
    x101 = z3.Int('x101')

    o.add(x1 >= 0)
    o.add(x3 >= 0)
    o.add(x5 >= 0)
    o.add(x10 >= 0)
    o.add(x15 >= 0)
    o.add(x16 >= 0)
    o.add(x20 >= 0)
    o.add(x24 >= 0)
    o.add(x25 >= 0)
    o.add(x30 >= 0)
    o.add(x37 >= 0)
    o.add(x38 >= 0)
    o.add(x49 >= 0)
    o.add(x50 >= 0)
    o.add(x74 >= 0)
    o.add(x75 >= 0)
    o.add(x100 >= 0)
    o.add(x101 >= 0)

    y1 = z3.Int('y1')
    y3 = z3.Int('y3')
    y5 = z3.Int('y5')
    y10 = z3.Int('y10')
    y15 = z3.Int('y15')
    y16 = z3.Int('y16')
    y20 = z3.Int('y20')
    y24 = z3.Int('y24')
    y25 = z3.Int('y25')
    y30 = z3.Int('y30')
    y37 = z3.Int('y37')
    y38 = z3.Int('y38')
    y49 = z3.Int('y49')
    y50 = z3.Int('y50')
    y74 = z3.Int('y74')
    y75 = z3.Int('y75')
    y100 = z3.Int('y100')
    y101 = z3.Int('y101')

    o.add(y1 >= 0)
    o.add(y3 >= 0)
    o.add(y5 >= 0)
    o.add(y10 >= 0)
    o.add(y15 >= 0)
    o.add(y16 >= 0)
    o.add(y20 >= 0)
    o.add(y24 >= 0)
    o.add(y25 >= 0)
    o.add(y30 >= 0)
    o.add(y37 >= 0)
    o.add(y38 >= 0)
    o.add(y49 >= 0)
    o.add(y50 >= 0)
    o.add(y74 >= 0)
    o.add(y75 >= 0)
    o.add(y100 >= 0)
    o.add(y101 >= 0)

    s1 =  z3.Int('s1')
    s2 =  z3.Int('s2')
    part1 =  z3.Int('part1')
    part2 =  z3.Int('part2')
    total =  z3.Int('total')

    o.add(total == s1 + s2)
    o.add(z3abs(part1 - part2) <= 100)
    o.add(part1 + part2 == target)
    o.add(part1 == 1*x1 + 3*x3 + 5*x5 + 10*x10 + 15*x15 + 16*x16 + 20*x20 + 24*x24 + 25*x25 + 30*x30 + 37*x37 + 38*x38 + 49*x49 + 50*x50 + 74*x74 + 75*x75 + 100*x100 + 101*x101)
    o.add(part2 == 1*y1 + 3*y3 + 5*y5 + 10*y10 + 15*y15 + 16*y16 + 20*y20 + 24*y24 + 25*y25 + 30*y30 + 37*y37 + 38*y38 + 49*y49 + 50*y50 + 74*y74 + 75*y75 + 100*y100 + 101*y101)

    o.add(s1 == x1 + x3 + x5 + x10 + x15 + x16 + x20 + x24 + x25 + x30 + x37 + x38 + x49 + x50 + x74 + x75 + x100 + x101)
    o.add(s2 == y1 + y3 + y5 + y10 + y15 + y16 + y20 + y24 + y25 + y30 + y37 + y38 + y49 + y50 + y74 + y75 + y100 + y101)

    o.minimize(total)

    o.check()
    # print(o.model())
    # return o.model()[s1].as_long() + o.model()[s2].as_long() # FIXME. part1 + part2
    return o.model()[total].as_long()

solve(156488) +solve(352486) +solve(546212)
solve(156488)

solve(352486) 


nums = [int(line) for line in lines]
answer3 = sum(solve(num) for num in nums)
print(answer3)
