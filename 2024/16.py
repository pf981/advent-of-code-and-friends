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
        # print(f'{i=} {face=}')
        if face:
            wheels[i].append(face)

remainders = []
for jump, wheel in zip(jumps, wheels):
    print(f'{jump=} {len(wheel)=} {jump % len(wheel)=}')
    remainders.append(jump % len(wheel))
print(remainders)

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

import math
math.lcm(*cycle_lengths)
# 54600

# Calculate the number of coins per cycle
# Calculate the number of full cycles
# Also get remainnig coins not part of a full cycle

# You can do this PER WHEEL - you don't have to combine first

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
