import re


with open("2025_contest/05.txt") as f:
    lines = f.read().splitlines()

coords = [(int(line.split(', ')[0][1:]), int(line.split(', ')[1][:-1])) for line in lines]

closest = min(abs(x) + abs(y) for x, y in coords)
furthest = max(abs(x) + abs(y) for x, y in coords)
answer1 = furthest - closest
print(answer1)


# Part 2
_, x1, y1 = min((abs(x) + abs(y), x, y) for x, y in coords)
answer2 = min((abs(x - x1) + abs(y - y1), x, y) for x, y in coords if (x, y) != (x1, y1))
print(answer2)


# Part 3

answer3 = 0
x1, y1 = 0, 0
remaining = set(coords)
while remaining:
    d, x1, y1 = min((abs(x - x1) + abs(y - y1), x, y) for x, y in remaining)
    remaining.remove((x1, y1))
    answer3 += d

print(answer3)
