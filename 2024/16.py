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



# count_coins(21, wheels, jumps)
# count_coins(33, wheels, jumps)
# count_coins(100, wheels, jumps)

# count_coins(6, wheels, jumps)
# count_coins(7, wheels, jumps)
# count_coins(8, wheels, jumps)
# count_coins(9, wheels, jumps)

# count_coins(90, wheels, jumps)

# count_coins(1, wheels, jumps)
# count_coins(33, wheels, jumps)
# count_coins(10, wheels, jumps) # This isn't correct
# count_coins(100, wheels, jumps)

a = count_coins(full_cycle_length, wheels, jumps)
b = count_coins(remaining, wheels, jumps)

answer2 = a * n_full_cycles + b
print(answer2)

# for jump, wheel in zip(jumps, wheels):
#     n_wheel_cycles_per_full_cycle = full_cycle_length // len(wheel)
#     n_wheel_cycles = n_wheel_cycles_per_full_cycle * n_full_cycles
#     n_coins_per_cycle = sum(face == )

# 54600

# Calculate the number of coins per cycle
# Calculate the number of full cycles
# Also get remainnig coins not part of a full cycle

# You can do this PER WHEEL - you don't have to combine first
# Actually, if you don't want to do individual letters, you need to simulate a full cycle

# answer2 = []
# for jump, wheel in zip(jumps, wheels):
#     cycle_length = 0
#     coins_per_cycle = 0

#     while True:
#         if wheels[i] == ''
#         cycle_length += 1
#         i = jump % len(wheel)
#         if i == 0:
#             break

#     n_cycles = ...
#     answer2.append(wheel[(jump * 202420242024) % len(wheel)])
# answer2 = ' '.join(answer2)

answer2 = 'todo'
print(answer2)


# So, I think that I need to do a cycle simulation PER CHARACTER
# Note that jumps are prime and distinct, so the LCM is enourmous. Actually, you need to look at it MOD wheel size
# Actually, when looking at remainders, LCM is like 1MM so that is workable.
# When looking at cycles, it's around 55k which is very workable.



# Part 3


with open("./2024/input/everybody_codes_e2024_q16_p3.txt") as f:
    lines = f.read().splitlines()

answer3 = 'todo'
print(answer3)
