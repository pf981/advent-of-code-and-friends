import re

with open("./story_1/input/q03_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """x=1 y=2
# x=2 y=3
# x=3 y=4
# x=4 y=4""".splitlines()

answer1 = 0
for line in lines:
    x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))
    # print(f"{x=} {y=}")
    # x -= 1
    # y -= 1
    # diag = y-x

    # x = m y

    # print(f"{x=} {y=} {y-x=}")
    for _ in range(100):
        x += 1
        y -= 1
        if y == 0:
            y = x - y - 1
            x = 1
    answer1 += x + 100 * y

print(answer1)
# x, y = 1, 3
# for day in range(1, 8):
#     print(f"{day=} {x=} {y=}")
#     x += 1
#     y -= 1
#     if y == 0:
#         y = x - y - 1
#         x = 1

import itertools

with open("./story_1/input/q03_p2.txt") as f:
    lines = f.read().splitlines()

lines = """x=12 y=2
x=8 y=4
x=7 y=1
x=1 y=5
x=1 y=3""".splitlines()

max_val = 10_000_000
candidates = set(range(max_val))
for line in lines:
    x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))

    seen = None
    for day in itertools.count():
        if y == 1:
            if seen is None:
                seen = day
            else:
                break
        x += 1
        y -= 1
        if y == 0:
            y = x - y - 1
            x = 1

    print(f"{seen=} {day=} {day-seen=}")
    cycle_length = day - seen
    d = seen
    candidates2 = set()
    while d < max_val:
        candidates2.add(d)
        d += cycle_length
    candidates.intersection_update(candidates2)


answer2 = min(candidates)
print(answer2)


# import heapq
# import collections

with open("./story_1/input/q03_p3.txt") as f:
    lines = f.read().splitlines()

# lines = """x=12 y=2
# x=8 y=4
# x=7 y=1
# x=1 y=5
# x=1 y=3""".splitlines()

# heap = []  #
# counts = collections.Counter()
# for line in lines:
#     x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))

#     seen = None
#     for day in itertools.count():
#         if y == 1:
#             if seen is None:
#                 seen = day
#             else:
#                 break
#         x += 1
#         y -= 1
#         if y == 0:
#             y = x - y - 1
#             x = 1

#     print(f"{seen=} {day=} {day-seen=}")
#     cycle_length = day - seen
#     heapq.heappush(heap, (seen, cycle_length))
#     counts[seen] += 1

# # xx = 0
# target = len(heap)
# while heap:
#     day, cycle_length = heapq.heappop(heap)
#     # print(f"{day=} {cycle_length=} {target=} {heap=} {counts=}")
#     if counts[day] == target:
#         answer3 = day
#         break

#     del counts[day]
#     day2 = day + cycle_length
#     counts[day2] += 1
#     heapq.heappush(heap, (day2, cycle_length))

#     # xx += 1
#     # if xx > 100:
#     #     break

# print(answer3)


# import z3

# o = z3.Optimize()

# z3_day = z3.Int("z3_day")
# o.add(z3_day >= 1)
import itertools

for i, line in enumerate(lines):
    x, y = (int(x) for x in re.findall(r"-?[0-9]+", line))

    seen = None
    for day in itertools.count():
        if y == 1:
            if seen is None:
                seen = day
            else:
                break
        x += 1
        y -= 1
        if y == 0:
            y = x - y - 1
            x = 1

    print(f"{seen=} {day=} {day-seen=}")
    cycle_length = day - seen

    # ki = z3.Int(f"k{i}")
    # o.add(z3_day == seen + ki * cycle_length)
    # o.add(z3_day % cycle_length == seen)

# o.minimize(z3_day)
# o.check()
# o.model()[z3_day].as_long()
