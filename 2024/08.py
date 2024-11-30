with open("./2024/input/everybody_codes_e2024_q08_p1.txt") as f:
    lines = f.read().splitlines()

target = int(lines[0])

blocks = 1
width = 1
while blocks < target:
    width += 2
    blocks += width

remaining = blocks - target
answer1 = remaining * width
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q08_p2.txt") as f:
    lines = f.read().splitlines()

mod = 1111
target = 20240000
priests = int(lines[0])

blocks = 1
width = 1
extra_height = 1
while blocks < target:
    extra_height = (extra_height * priests) % mod
    width += 2
    blocks += width * extra_height

remaining = blocks - target
answer2 = remaining * width
print(answer2)


# Part 3


import collections


with open("./2024/input/everybody_codes_e2024_q08_p3.txt") as f:
    lines = f.read().splitlines()

extra = mod = 10
target = 202400000
priests = int(lines[0])

heights = collections.deque([1])

blocks = 1
width = 1
extra_height = 1
while blocks < target:
    extra_height = (extra_height * priests) % mod + extra # AKA thickness
    width += 2
    blocks += width * extra_height
    
    heights.appendleft(0)
    heights.append(0)
    for i in range(len(heights)):
        heights[i] += extra_height
    
to_remove = 0
for i in range(1, len(heights) - 1):
    to_remove += (priests * width * heights[i]) % mod

required_to_complete_shell = blocks - to_remove
answer3 = required_to_complete_shell - target
print(answer3)
