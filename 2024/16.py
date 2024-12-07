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

def min_max_coins(n_pulls, wheels, jumps):
    indexes = [0 for _ in range(len(wheels))]
    min_coins, max_coins = min_max_coins_impl(n_pulls, wheels, jumps, indexes, True)
    return min_coins, max_coins

def shift_one(indexes, wheels, shift):
    indexes = indexes.copy()
    for i in range(len(wheels)):
        indexes[i] = (indexes[i] + shift) % len(wheels[i])
    return indexes


def min_max_coins_impl(n_pulls, wheels, jumps, indexes, can_shift) -> int:
    if n_pulls == 0:
        return 0, 0
    
    # print(f'{indexes=}')

    indexes = indexes.copy()
    min_coins = float('inf')
    max_coins = 0
    if can_shift:
        a, b = min_max_coins_impl(n_pulls, wheels, jumps, shift_one(indexes, wheels, +1), False)
        min_coins = min(min_coins, a)
        max_coins = max(max_coins, b)

        a, b = min_max_coins_impl(n_pulls, wheels, jumps, shift_one(indexes, wheels, -1), False)
        min_coins = min(min_coins, a)
        max_coins = max(max_coins, b)

    coins = 0
    for _ in range(1):
        s = ''
        for i in range(len(wheels)):
            indexes[i] = (indexes[i] + jumps[i]) % len(wheels[i])
            face = wheels[i][indexes[i]]
            s += face[0] + face[2]
        
        for count in collections.Counter(s).values():
            coins += max(0, count - 2)
    # a, b = min_max_coins_impl(n_pulls - 1, wheels, jumps, indexes, can_shift)
    a, b = min_max_coins_impl(n_pulls - 1, wheels, jumps, indexes, True) # Test
    min_coins = min(min_coins, a + coins)
    max_coins = max(max_coins, b + coins)

    return min_coins, max_coins



# min_max_coins(1, wheels, jumps)
# min_max_coins(2, wheels, jumps)
# min_max_coins(3, wheels, jumps)


min_coins, max_coins = min_max_coins(256, wheels, jumps)
answer3 = f'{max_coins} {min_coins}'
print(answer3)

# TODO: May be just prune?
