import math


with open("./2025/input/everybody_codes_e2025_q04_p1.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]

spins = 2025.0
nxt = nums[-1]
nums.pop()
for num in nums[::-1]:
    spins *= num / nxt
    nxt = num

answer1 = int(spins)
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q04_p2.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]

spins = 1
nxt = nums[-1]
nums.pop()
for num in nums[::-1]:
    spins *= num / nxt
    nxt = num

answer2 = math.ceil(10000000000000 / spins)
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q04_p3.txt") as f:
    lines = f.read().splitlines()

pairs = []
for line in lines:
    first, *rest = line.split("|")
    a = int(first)
    b = a if not rest else int(rest[0])
    pairs.append((a, b))

spins = 100
size = pairs[0][0]
for a, b in pairs:
    spins *= size / a
    size = b

answer3 = int(spins)
print(answer3)
