def parse(lines: list[str]) -> tuple[list[list[str]], list[int]]:
    jumps, _, *wheels_lines = lines
    jumps = [int(jump) for jump in jumps.split(',')]

    wheels = [[] for _ in range(len(jumps))]
    for line in wheels_lines:
        for i in range(len(jumps)):
            face = line[i*4:i*4+3].replace(' ', '')
            if face:
                wheels[i].append(face)

    return wheels, jumps


with open("./2024/input/everybody_codes_e2024_q16_p1.txt") as f:
    lines = f.read().splitlines()

wheels, jumps = parse(lines)

answer1 = []
for jump, wheel in zip(jumps, wheels):
    answer1.append(wheel[(jump * 100) % len(wheel)])
answer1 = ' '.join(answer1)
print(answer1)


# Part 2


import collections
import math


def count_coins(n_pulls: int, wheels: list[list[str]], jumps: list[int]) -> int:
    coins = 0
    indexes = [0 for _ in range(len(wheels))]

    for _ in range(n_pulls):
        s = ''
        for i in range(len(wheels)):
            indexes[i] = (indexes[i] + jumps[i]) % len(wheels[i])
            face = wheels[i][indexes[i]]
            s += face[0] + face[2]
        
        for count in collections.Counter(s).values():
            coins += max(0, count - 2)

    return coins


with open("./2024/input/everybody_codes_e2024_q16_p2.txt") as f:
    lines = f.read().splitlines()

wheels, jumps = parse(lines)

cycle_lengths = []
for jump, wheel in zip(jumps, wheels):
    i = 0
    cycle_length = 0
    while True:
        cycle_length += 1
        i = (i + jump) % len(wheel)
        if i == 0:
            break
    cycle_lengths.append(cycle_length)

full_cycle_length = math.lcm(*cycle_lengths)
n_full_cycles = 202420242024 // full_cycle_length
remaining = 202420242024 % full_cycle_length

coins_per_full_cycle = count_coins(full_cycle_length, wheels, jumps)
remaining_coins = count_coins(remaining, wheels, jumps)

answer2 = coins_per_full_cycle * n_full_cycles + remaining_coins
print(answer2)


# Part 3


def shift_one(indexes, wheels, shift):
    indexes = list(indexes)
    for i in range(len(wheels)):
        indexes[i] = (indexes[i] + shift) % len(wheels[i])
    return tuple(indexes)


def min_max_coins(n_pulls, wheels, jumps):
    min_coins = solve(n_pulls, wheels, jumps, False)
    max_coins = solve(n_pulls, wheels, jumps, True)
    return min_coins, max_coins


def solve(n_pulls, wheels, jumps, is_max):
    indexes = tuple(0 for _ in range(len(wheels)))
    f = max if is_max else min
    best = 0 if is_max else float('inf')
    dp = {} # (n_pulls, indexes, can_shift) -> coins
    stack = [(0, n_pulls, indexes, True, tuple())] # [(coins, n_pulls, indexes, can_shift, path), ...]
    # path is ((coins, n_pulls, indexes, can_shift), ...)
    while stack:
        coins, n_pulls, indexes, can_shift, path = stack.pop()

        if (n_pulls, indexes, can_shift) in dp:
            coins += dp[(n_pulls, indexes, can_shift)]
            n_pulls = 0

        if n_pulls == 0:
            best = f(best, coins)
            for p in path:
                if p[1:] in dp:
                    dp[p[1:]] = f(coins - p[0], dp[p[1:]])
                else:
                    dp[p[1:]] = coins - p[0] # TODO: Check this
            continue

        path = path + ((coins, n_pulls, indexes, can_shift),)

        if can_shift:
            stack.append((coins, n_pulls, shift_one(indexes, wheels, +1), False, path))
            stack.append((coins, n_pulls, shift_one(indexes, wheels, -1), False, path))

        indexes2 = list(indexes)
        s = ''
        for i in range(len(wheels)):
            indexes2[i] = (indexes2[i] + jumps[i]) % len(wheels[i])
            face = wheels[i][indexes2[i]]
            s += face[0] + face[2]
        for count in collections.Counter(s).values():
            coins += max(0, count - 2)
        
        stack.append((coins, n_pulls - 1, tuple(indexes2), True, path))
    
    return best


with open("./2024/input/everybody_codes_e2024_q16_p3.txt") as f:
    lines = f.read().splitlines()

wheels, jumps = parse(lines)

min_coins, max_coins = min_max_coins(256, wheels, jumps)
answer3 = f'{max_coins} {min_coins}'
print(answer3)
