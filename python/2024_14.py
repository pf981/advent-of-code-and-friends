from aocd import get_data, submit
import re
import collections

inp = get_data(day=14, year=2024)
w = 101
h = 103

inp = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''
w = 11
h = 7

lines = inp.splitlines()
robots = []
for line in lines:
    robots.append([int(x) for x in re.findall(r'-?\d+', line)])

print(robots)

for _ in range(100):
    for i, (x, y, dx, dy) in enumerate(robots):
        robots[i][0] = (x + dx) % w
        robots[i][1] = (y + dy) % h

dw = w // 2
dh = h // 2

answer1 = 0
m = collections.Counter()
for x, y, dx, dy in robots:
    if x == dw or y == dh:
        continue
    m[(x < dw, y < dh)] += 1
    print(x, y)

m
import math
math.prod(m.values())

answer1 = math.prod(m.values())
print(answer1)

submit(answer1, part='a', day=14, year=2024)


rob_pos = collections.Counter()
for x, y, dx, dy in robots:
    rob_pos[(x, y)] += 1
for y in range(h):
    for x in range(w):
        print(rob_pos[(x,y)], end='')
    print()


# Part 2







def pp():
    rob_pos = collections.Counter()
    for x, y, dx, dy in robots:
        rob_pos[(x, y)] += 1
    for y in range(h):
        for x in range(w):
            c = '#' if rob_pos[(x,y)] else '.'
            print(c, end='')
        print()

lines = inp.splitlines()
robots = []
for line in lines:
    robots.append([int(x) for x in re.findall(r'-?\d+', line)])

# for _ in range(100):
#     for i, (x, y, dx, dy) in enumerate(robots):
#         robots[i][0] = (x + dx) % w
#         robots[i][1] = (y + dy) % h

import statistics

best = float('inf')
seconds = 0
best_tree_factor = 0
for seconds in range(1, 500001):
    tree_factor = collections.Counter()
    seen = set()
    cur_tree_factor = 0
    for i, (x, y, dx, dy) in enumerate(robots):
        robots[i][0] = (x + dx) % w
        robots[i][1] = (y + dy) % h

        xx = robots[i][0]
        yy = robots[i][1]
        seen.add((xx, yy))
        cur_tree_factor += (xx-1, yy) in seen
        cur_tree_factor += (xx+1, yy) in seen
        cur_tree_factor += (xx, yy-1) in seen
        cur_tree_factor += (xx, yy+1) in seen

    # avg_tree_factor = statistics.mean(tree_factor.values())
    # avg_tree_factor = max(tree_factor.values())
    avg_tree_factor = cur_tree_factor
    if avg_tree_factor > best_tree_factor:
        best_tree_factor = cur_tree_factor
        # robots2 = robots.copy()
        print(f'{seconds=} {best_tree_factor=}')
        pp()
        print()
        print()

robots = robots2
pp()


# 6432
# That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. [Return to Day 14]


# 6431
# That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. [Return to Day 14]


# 6531 <<---


# best = float('inf')
# seconds = 0
# for seconds in range(1, 50001):
#     tree_factor = collections.Counter()
#     best_tree_factor = 0
#     for i, (x, y, dx, dy) in enumerate(robots):
#         robots[i][0] = (x + dx) % w
#         robots[i][1] = (y + dy) % h

#         xx = robots[i][0]
#         yy = robots[i][1]

#         tree_factor[(xx, yy)] += 1
#         tree_factor[(xx, yy+1)] += 1
#         tree_factor[(xx, yy+2)] += 1
#         tree_factor[(xx, yy+3)] += 1
#         tree_factor[(xx, yy+4)] += 1
#         tree_factor[(xx, yy+5)] += 1
#         tree_factor[(xx, yy+6)] += 1
#         tree_factor[(xx + 1, yy)] += 1
#         tree_factor[(xx - 1, yy)] += 1
#         tree_factor[(xx, yy - 1)] += 1

#     # avg_tree_factor = statistics.mean(tree_factor.values())
#     avg_tree_factor = max(tree_factor.values())
#     if avg_tree_factor > best_tree_factor:
#         best_tree_factor = avg_tree_factor
#         robots2 = robots.copy()
#         # print(seconds)
#         # pp()
#         # print()
#         # print()




# seconds = 0
# for seconds in range(1, 100001):
#     for i, (x, y, dx, dy) in enumerate(robots):
#         robots[i][0] = (x + dx) % w
#         robots[i][1] = (y + dy) % h
    
#     first_row = min(y for _, y, _, _ in robots)
#     n_first_row = len({x for x, y, _, _ in robots if y == first_row})

#     second_row = min(y for _, y, _, _ in robots if y > first_row)
#     n_second_row = len({x for x, y, _, _ in robots if y == second_row})

#     third_row = min(y for _, y, _, _ in robots if y > second_row)
#     n_third_row = len({x for x, y, _, _ in robots if y == third_row})


#     # if n_first_row == 1 and n_second_row == 2 and n_third_row == 2:
#     if n_first_row == 1 and n_second_row == 3 and n_third_row == 5:
#     # if n_first_row == 1 and n_second_row == 2:
#         print(seconds)
#         pp()
#         print()
#         print()




answer2 = 'todo'
print(answer2)

# submit(answer2, part='b', day=14, year=2024)







from aocd import get_data, submit
import re
import collections

inp = get_data(day=14, year=2024)
w = 101
h = 103


lines = inp.splitlines()
robots = []
for line in lines:
    robots.append([int(x) for x in re.findall(r'-?\d+', line)])

robots2 = robots.copy()
# print(robots)

# for _ in range(6432):
# for _ in range(6434):
def gogo(seconds):
    robots = robots2.copy()
    for _ in range(seconds):
        for i, (x, y, dx, dy) in enumerate(robots):
            robots[i][0] = (x + dx) % w
            robots[i][1] = (y + dy) % h

    rob_pos = collections.Counter()
    for x, y, dx, dy in robots:
        rob_pos[(x, y)] += 1
    for y in range(h):
        for x in range(w):
            c = '#' if rob_pos[(x,y)] else '.'
            print(c, end='')
        print()

for seconds in range(6430, 6450):
    print(f'{seconds=}')
    gogo(seconds)
    print()

for seconds in range(6420, 6430):
    print(f'{seconds=}')
    gogo(seconds)
    print()

gogo(6432-100)
gogo(6432-101)


for seconds in range(6432-102, 6432-90):
    print(f'{seconds=}')
    gogo(seconds)
    print()
