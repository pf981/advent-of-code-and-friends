import collections

with open("./input/2026/02.txt") as f:
    text = f.read()

wall = [0] * 100
i = 0
for inst in text:
    i += (inst == ">") - (inst == "<")
    i %= 100
    wall[i] += 1

answer1 = max(wall) * (wall.index(max(wall)) + 1)
print(answer1)

answer2 = i = j = 0
for inst1, inst2 in zip(text, text[::-1]):
    i += (inst1 == ">") - (inst1 == "<")
    i %= 100
    j += (inst2 == ">") - (inst2 == "<")
    j %= 100
    answer2 += i == j
print(answer2)

wall = collections.deque([0] * 100)
wall_ids = collections.deque(range(100))
i = 0
for inst1, inst2 in zip(text, text[::-1]):
    i += (inst1 == ">") - (inst1 == "<")
    i %= 100

    if inst2 == ">":
        wall.rotate(1)
        wall_ids.rotate(1)
    else:
        wall.rotate(-1)
        wall_ids.rotate(-1)
    wall[i] += 1

answer3 = max(wall) * (wall_ids[wall.index(max(wall))] + 1)
print(answer3)
