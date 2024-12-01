import functools


with open("./2024/input/everybody_codes_e2024_q09_p1.txt") as f:
    lines = f.read().splitlines()

stamps = [1, 3, 5, 10]

@functools.cache
def min_stamps(i, target):
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

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

@functools.cache
def min_stamps(i, target):
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


import z3


def z3abs(x):
    return z3.If(x >= 0, x, -x)


def solve(target: int) -> int:
    o = z3.Optimize()

    stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]

    part1_formula = 0
    part2_formula = 0
    s1_formula = 0
    s2_formula = 0

    for i, stamp in enumerate(stamps):
        x = z3.Int(f'x{i}')
        y = z3.Int(f'y{i}')

        o.add(x >= 0)
        o.add(y >= 0)

        part1_formula += stamp * x
        part2_formula += stamp * y
        s1_formula += x
        s2_formula += y
    
    s1 = z3.Int('s1')
    s2 = z3.Int('s2')
    part1 = z3.Int('part1')
    part2 = z3.Int('part2')
    total = z3.Int('total')

    o.add(total == s1 + s2)
    o.add(z3abs(part1 - part2) <= 100)
    o.add(part1 + part2 == target)
    o.add(part1 == part1_formula)
    o.add(part2 == part2_formula)

    o.add(s1 == s1_formula)
    o.add(s2 == s2_formula)

    o.minimize(total)

    o.check()
    return o.model()[total].as_long()


with open("./2024/input/everybody_codes_e2024_q09_p3.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]
answer3 = sum(solve(num) for num in nums)
print(answer3)
