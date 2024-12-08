with open("./2024/input/everybody_codes_e2024_q16_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''1,2,3

# ^_^ -.- ^,-
# >.- ^_^ >.<
# -_- -.- >.<
#     -.^ ^_^
#     >.>'''.splitlines()

jumps, _, *wheels_lines = lines
jumps = [int(jump) for jump in jumps.split(',')]

wheels = [[] for _ in range(len(jumps))]
for line in wheels_lines:
    for i in range(len(jumps)):
        face = line[i*4:i*4+3].replace(' ', '')
        # print(f'{i=} {face=}')
        if face:
            wheels[i].append(face)

answer1 = []
for jump, wheel in zip(jumps, wheels):
    answer1.append(wheel[(jump * 100) % len(wheel)])
answer1 = ' '.join(answer1)
print(answer1)


# Part 2


import collections
import math


with open("./2024/input/everybody_codes_e2024_q16_p2.txt") as f:
    lines = f.read().splitlines()

# lines = '''1,2,3

# ^_^ -.- ^,-
# >.- ^_^ >.<
# -_- -.- >.<
#     -.^ ^_^
#     >.>'''.splitlines()

jumps, _, *wheels_lines = lines
jumps = [int(jump) for jump in jumps.split(',')]

wheels = [[] for _ in range(len(jumps))]
for line in wheels_lines:
    for i in range(len(jumps)):
        face = line[i*4:i*4+3].replace(' ', '')
        if face:
            wheels[i].append(face)

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
print(cycle_lengths)

full_cycle_length = math.lcm(*cycle_lengths)
n_full_cycles = 202420242024 // full_cycle_length
remaining = 202420242024 % full_cycle_length

def count_coins(n_pulls: int, wheels, jumps) -> int:
    coins = 0
    indexes = [0 for _ in range(len(wheels))]

    for _ in range(n_pulls):
        s = ''
        for i in range(len(wheels)):
            indexes[i] = (indexes[i] + jumps[i]) % len(wheels[i])
            face = wheels[i][indexes[i]]
            s += face[0] + face[2]
        
        # print(f'{s} {[max(0, count - 2) for count in collections.Counter(s).values()]}')
        for count in collections.Counter(s).values():
            coins += max(0, count - 2)


    return coins

a = count_coins(full_cycle_length, wheels, jumps)
b = count_coins(remaining, wheels, jumps)

answer2 = a * n_full_cycles + b
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q16_p3.txt") as f:
    lines = f.read().splitlines()


lines = '''1,2,3

^_^ -.- ^,-
>.- ^_^ >.<
-_- -.- ^.^
    -.^ >.<
    >.>'''.splitlines()

jumps, _, *wheels_lines = lines
jumps = [int(jump) for jump in jumps.split(',')]

wheels = [[] for _ in range(len(jumps))]
for line in wheels_lines:
    for i in range(len(jumps)):
        face = line[i*4:i*4+3].replace(' ', '')
        if face:
            wheels[i].append(face)

# def min_max_coins(n_pulls, wheels, jumps):
#     indexes = [0 for _ in range(len(wheels))]
#     min_coins, max_coins = min_max_coins_impl(n_pulls, wheels, jumps, indexes, True)
#     return min_coins, max_coins

def shift_one(indexes, wheels, shift):
    indexes = indexes.copy()
    for i in range(len(wheels)):
        indexes[i] = (indexes[i] + shift) % len(wheels[i])
    return indexes


# def min_max_coins_impl(n_pulls, wheels, jumps, indexes, can_shift) -> int:
#     if n_pulls == 0:
#         return 0, 0
    
#     # print(f'{indexes=}')

#     indexes = indexes.copy()
#     min_coins = float('inf')
#     max_coins = 0
#     if can_shift:
#         a, b = min_max_coins_impl(n_pulls, wheels, jumps, shift_one(indexes, wheels, +1), False)
#         min_coins = min(min_coins, a)
#         max_coins = max(max_coins, b)

#         a, b = min_max_coins_impl(n_pulls, wheels, jumps, shift_one(indexes, wheels, -1), False)
#         min_coins = min(min_coins, a)
#         max_coins = max(max_coins, b)

#     coins = 0
#     for _ in range(1):
#         s = ''
#         for i in range(len(wheels)):
#             indexes[i] = (indexes[i] + jumps[i]) % len(wheels[i])
#             face = wheels[i][indexes[i]]
#             s += face[0] + face[2]
        
#         for count in collections.Counter(s).values():
#             coins += max(0, count - 2)
#     # a, b = min_max_coins_impl(n_pulls - 1, wheels, jumps, indexes, can_shift)
#     a, b = min_max_coins_impl(n_pulls - 1, wheels, jumps, indexes, True) # Test
#     min_coins = min(min_coins, a + coins)
#     max_coins = max(max_coins, b + coins)

#     return min_coins, max_coins


def min_max_coins(n_pulls, wheels, jumps):
    min_coins = min_max_coins_impl(n_pulls, wheels, jumps, False)
    max_coins = min_max_coins_impl(n_pulls, wheels, jumps, True)
    return min_coins, max_coins

def min_max_coins_impl(n_pulls, wheels, jumps, is_max):
    q = collections.deque([(0, n_pulls, [0 for _ in range(len(wheels))], True)]) # coins, n_pulls, indexes, can_shift
    best = 0 if is_max else float('inf')
    f = max if is_max else min
    n_pulls_start = n_pulls
    while q:
        # Prune
        if len(q) >= 3_000_000:
            q = sorted(list(q), key=lambda l: l[0] / (n_pulls_start - l[1]), reverse=is_max)
            q = q[:50_000]
            q = collections.deque(q)
        
        for _ in range(len(q)):
            coins, n_pulls, indexes, can_shift = q.popleft()
            indexes = indexes.copy()

            if n_pulls == 0:
                best = f(best, coins)
                continue



            if can_shift:
                q.append((coins, n_pulls, shift_one(indexes, wheels, +1), False))
                q.append((coins, n_pulls, shift_one(indexes, wheels, -1), False))

            for _ in range(1):
                s = ''
                for i in range(len(wheels)):
                    indexes[i] = (indexes[i] + jumps[i]) % len(wheels[i])
                    face = wheels[i][indexes[i]]
                    s += face[0] + face[2]
                
                for count in collections.Counter(s).values():
                    coins += max(0, count - 2)

            q.append((coins, n_pulls - 1, indexes, True))
    
    return best


# min_max_coins(1, wheels, jumps)
# min_max_coins(2, wheels, jumps)
# min_max_coins(3, wheels, jumps)
# min_max_coins(10, wheels, jumps)

# min_max_coins(100, wheels, jumps)

min_coins, max_coins = min_max_coins(256, wheels, jumps)
answer3 = f'{max_coins} {min_coins}'
print(answer3)

# 580 89
# Your answer length is: correct
# The first character of your answer is: incorrect
# This  was with 100_000, 3_000
# So probably starts with 6?

# Trying 150_000, 5_000 -> 569 94 (not correct start)
# Trying 300_000, 10_000 -> 562 95 (not correct start)
# Trying 800_000, 20_000 -> 578 93 (not correct start)
# Trying 3_000_000, 50_000 -> 580 83 (not correct start)


# TODO: May be just prune?
# Maybe prune randomly, too?

# 5_000, 500 -> 488 128
# 10_000, 1_000 -> 492 128
# 20_000, 2_000 -> 490 129 ??? Huh?
# 30_000, 3_000 -> 490 129
# 100_000, 3_000 -> 627 128

# Updating sort lambda made it much better. Originally was just number of coins, but now is coin rate.


# 15_000, 2_000 -> 


################

import collections
import functools
import sys

# sys.setrecursionlimit(2*(10**9))
# sys.setrecursionlimit(2_147_483_647)
sys.setrecursionlimit(10**10)



with open("C:/Users/Paul/dev/everybody-codes-solutions/2024/input/everybody_codes_e2024_q16_p3.txt") as f:
    lines = f.read().splitlines()


# lines = '''1,2,3

# ^_^ -.- ^,-
# >.- ^_^ >.<
# -_- -.- ^.^
#     -.^ >.<
#     >.>'''.splitlines()

jumps, _, *wheels_lines = lines
jumps = [int(jump) for jump in jumps.split(',')]

wheels = [[] for _ in range(len(jumps))]
for line in wheels_lines:
    for i in range(len(jumps)):
        face = line[i*4:i*4+3].replace(' ', '')
        if face:
            wheels[i].append(face)

def shift_one(indexes, wheels, shift):
    indexes = list(indexes)
    for i in range(len(wheels)):
        indexes[i] = (indexes[i] + shift) % len(wheels[i])
    return tuple(indexes)

def min_max_coins(n_pulls, wheels, jumps):
    indexes = tuple(0 for _ in range(len(wheels)))
    min_coins = dfs(n_pulls, indexes, False, True)
    max_coins = dfs(n_pulls, indexes, True, True)
    return min_coins, max_coins

@functools.cache
def dfs(n_pulls, indexes, is_max, can_shift):
    if n_pulls == 0:
        return 0
    
    best = 0 if is_max else float('inf')
    f = max if is_max else min
    if can_shift:
        best = f(
            best,
            dfs(n_pulls, shift_one(indexes, wheels, +1), is_max, False),
            dfs(n_pulls, shift_one(indexes, wheels, -1), is_max, False)
        )

    indexes = list(indexes)
    s = ''
    coins = 0
    for i in range(len(wheels)):
        indexes[i] = (indexes[i] + jumps[i]) % len(wheels[i])
        face = wheels[i][indexes[i]]
        s += face[0] + face[2]
    for count in collections.Counter(s).values():
        coins += max(0, count - 2)
    best = f(
        best,
        coins + dfs(n_pulls - 1, tuple(indexes), is_max, True)
    )
    return best

# min_max_coins(1, wheels, jumps)
# min_max_coins(2, wheels, jumps)
# min_max_coins(3, wheels, jumps)
# min_max_coins(10, wheels, jumps)

# min_max_coins(100, wheels, jumps)
# min_max_coins(250, wheels, jumps)

min_coins, max_coins = min_max_coins(256, wheels, jumps)
answer3 = f'{max_coins} {min_coins}'
print(answer3)
