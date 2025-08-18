from aocd import get_data, submit
import collections
import copy
import math
import re


def simulate(robots):
    for i, (x, y, dx, dy) in enumerate(robots):
        robots[i][0] = (x + dx) % w
        robots[i][1] = (y + dy) % h


inp = get_data(day=14, year=2024)
w = 101
h = 103

lines = inp.splitlines()
start_robots = []
for line in lines:
    start_robots.append([int(x) for x in re.findall(r'-?\d+', line)])

robots = copy.deepcopy(start_robots)
for _ in range(100):
    simulate(robots)

dw = w // 2
dh = h // 2

m = collections.Counter()
for x, y, dx, dy in robots:
    if x == dw or y == dh:
        continue
    m[(x < dw, y < dh)] += 1

answer1 = math.prod(m.values())
print(answer1)

submit(answer1, part='a', day=14, year=2024)


# Part 2


robots = copy.deepcopy(start_robots)

for seconds in range(1, 10_000):
    simulate(robots)

    positions = {(x, y) for x, y, _, _ in robots}
    for x, y in positions:
        for i in range(1, 20):
            if (x + i, y) not in positions:
                break
        else:
            break
    else:
        continue
    break

for y in range(h):
    for x in range(w):
        c = '#' if (x, y) in positions else '.'
        print(c, end='')
    print()


answer2 = seconds
print(answer2)

submit(answer2, part='b', day=14, year=2024)
