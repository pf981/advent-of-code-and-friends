import collections
import functools
import re

# import z3

with open("2025_contest/18.txt") as f:
    inp = f.read()

# inp = """RULE 1: 8x+10y+3z+5a DIVIDE 9 HAS REMAINDER 4 | DEBRIS VELOCITY (0, -1, 0, 1)
# RULE 2: 3x+7y+10z+9a DIVIDE 9 HAS REMAINDER 4 | DEBRIS VELOCITY (0, 1, 0, 1)
# RULE 3: 10x+3y+7z+3a DIVIDE 11 HAS REMAINDER 9 | DEBRIS VELOCITY (-1, 0, 1, -1)
# RULE 4: 5x+4y+9z+3a DIVIDE 7 HAS REMAINDER 2 | DEBRIS VELOCITY (0, -1, -1, -1)
# RULE 5: 3x+11y+11z+3a DIVIDE 3 HAS REMAINDER 1 | DEBRIS VELOCITY (-1, 1, 0, -1)
# RULE 6: 4x+6y+7z+3a DIVIDE 8 HAS REMAINDER 6 | DEBRIS VELOCITY (0, -1, 0, -1)
# RULE 7: 7x+4y+3z+7a DIVIDE 11 HAS REMAINDER 5 | DEBRIS VELOCITY (0, 1, 0, -1)
# RULE 8: 3x+6y+9z+9a DIVIDE 5 HAS REMAINDER 3 | DEBRIS VELOCITY (1, 1, -1, -1)"""

# inp = """RULE 1: 8x+10y+3z+5a DIVIDE 9 HAS REMAINDER 4 | DEBRIS VELOCITY (0, -1, 0, 1)
# RULE 2: 3x+7y+10z+9a DIVIDE 9 HAS REMAINDER 4 | DEBRIS VELOCITY (0, 1, 0, 1)
# RULE 3: 10x+3y+7z+3a DIVIDE 11 HAS REMAINDER 9 | DEBRIS VELOCITY (-1, 0, 1, -1)
# RULE 4: 5x+4y+9z+3a DIVIDE 7 HAS REMAINDER 2 | DEBRIS VELOCITY (0, -1, -1, -1)
# RULE 5: 3x+11y+11z+3a DIVIDE 3 HAS REMAINDER 1 | DEBRIS VELOCITY (-1, 1, 0, -1)
# RULE 6: 4x+6y+7z+3a DIVIDE 8 HAS REMAINDER 6 | DEBRIS VELOCITY (0, -1, 0, -1)
# RULE 7: 7x+4y+3z+7a DIVIDE 11 HAS REMAINDER 5 | DEBRIS VELOCITY (0, 1, 0, -1)
# RULE 8: 3x+6y+9z+9a DIVIDE 5 HAS REMAINDER 3 | DEBRIS VELOCITY (1, 1, -1, -1)"""

rules = []
for line in inp.splitlines():
    rule = [int(num) for num in re.findall(r"-?[0-9]+", line)]
    rules.append(rule)

answer1 = 0
for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
    for x in range(10):
        for y in range(15):
            for z in range(60):
                for a in [-1, 0, 1]:
                    answer1 += (cx * x + cy * y + cz * z + ca * a) % denom == mod

# 10 by 15 by 60 by 3

print(answer1)


# Part 2


def increment(debris_state):
    for i, (x, y, z, a, vx, vy, vz, va) in enumerate(debris_state):
        xx = (x + vx) % 10
        yy = (y + vy) % 15
        zz = (z + vz) % 60
        aa = a + va
        while aa > 1:
            aa -= 3
        while aa < -1:
            aa += 3
        debris_state[i] = (xx, yy, zz, aa, vx, vy, vz, va)


def get_debris(debris_state):
    return {(x, y, z) for x, y, z, a, *_ in debris_state if a == 0}


target = (9, 14, 59)
positions = {(0, 0, 0)}
t = 0

debris_state = []
for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
    for x in range(10):
        for y in range(15):
            for z in range(60):
                for a in [-1, 0, 1]:
                    if (cx * x + cy * y + cz * z + ca * a) % denom == mod:
                        debris_state.append((x, y, z, a, vx, vy, vz, va))


# (0, 0, 0) in get_debris(debris_state)  # False
# increment(debris_state)
# (1, 0, 0) in get_debris(debris_state)  # True
# (0, 1, 0) in get_debris(debris_state)  # False
# (0, 0, 1) in get_debris(debris_state)  # True
# increment(debris_state)
# (0, 1, 0) in get_debris(debris_state)  # True
# (0, 0, 0) in get_debris(debris_state)  # True
# (1, 1, 0) in get_debris(debris_state)  # True
# (0, 2, 0) in get_debris(debris_state)  # True
# (0, 1, 1) in get_debris(debris_state)  # True
# ??? So even when I simulate normally, it results in no moves!!??


# has_debris(0, 1, 0, 0, 1)  # This is FALSE!!!??

import collections


def has_debris(x, y, z, a, t):
    if (x, y, z, a) == (0, 0, 0, 0):
        return False
    for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
        start_x = (x - t * vx) % 10
        start_y = (y - t * vy) % 15
        start_z = (z - t * vz) % 60
        start_a = (a - t * va + 1) % 3 - 1
        # print(f"{start_x, start_y, start_z, start_a}")
        if (cx * start_x + cy * start_y + cz * start_z + ca * start_a) % denom == mod:
            # print(f"{_, cx, cy, cz, ca, denom, mod, vx, vy, vz, va=}")
            # print(f"{start_x, start_y, start_z, start_a=}")
            return True
    return False


## TEST
# has_debris(0, 0, 0, 0, 0)
# has_debris(
#     0, 0, 0, 0, 1
# )  # RULE 4: 5x+4y+9z+3a DIVIDE 7 HAS REMAINDER 2 | DEBRIS VELOCITY (0, -1, -1, -1)
# has_debris(1, 0, 0, 0, 1)
# has_debris(1, 0, 0, 0, 0)
# has_debris(0, 1, 0, 0, 1)
# has_debris(0, 1, 0, 0, 2)
# has_debris(0, 0, 0, 0, 2)
# has_debris(0, 1, 1, 0, 2)
# has_debris(0, 2, 0, 0, 2)# RULE 8: 3x+6y+9z+9a DIVIDE 5 HAS REMAINDER 3 | DEBRIS VELOCITY (1, 1, -1, -1)


# has_debris(9, 14, 59, 0, 0)


# debris_state = []
# for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
#     for x in range(10):
#         for y in range(15):
#             for z in range(60):
#                 for a in [-1, 0, 1]:
#                     if (cx * x + cy * y + cz * z + ca * a) % denom == mod:
#                         print(f"{x, y, z} {denom, mod, vx, vy, vz=}")
#                         break
#                         debris_state.append((x, y, z, a, vx, vy, vz, va))
# (9, 14, 59) denom, mod, vx, vy, vz=(5, 3, 1, 1, -1)
# RULE 8: 3x+6y+9z+9a DIVIDE 5 HAS REMAINDER 3 | DEBRIS VELOCITY (1, 1, -1, -1)


target = (9, 14, 59)
positions = {(0, 0, 0)}
t = 0
counterzz = 0
while positions:
    counterzz += 1
    if counterzz > 1000:
        break
    next_positions = set()
    for pos in positions:
        if pos == target:
            print(f"FOUND! {t=}")
            break
        for dx, dy, dz in [
            (0, 0, 0),
            (-1, 0, 0),
            (1, 0, 0),
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
        ]:
            pos2 = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
            # print(f"Considering {pos2=} {t+1=}")
            if has_debris(*pos2, 0, t + 1):
                continue
            if not (0 <= pos2[0] < 10 and 0 <= pos2[1] < 15 and 0 <= pos2[2] < 60):
                continue
            next_positions.add(pos2)
            # print(f"Added {pos2=}")
    else:
        t += 1
        positions = sorted(next_positions)[-1000:]
        # positions = next_positions
        continue
    break

print(t)


print(answer2)


# Part 3


def count_debris(x, y, z, a, t):
    if (x, y, z, a) == (0, 0, 0, 0):
        return 0
    cnt = 0
    for _, cx, cy, cz, ca, denom, mod, vx, vy, vz, va in rules:
        start_x = (x - t * vx) % 10
        start_y = (y - t * vy) % 15
        start_z = (z - t * vz) % 60
        start_a = (a - t * va + 1) % 3 - 1
        # print(f"{start_x, start_y, start_z, start_a}")
        if (cx * start_x + cy * start_y + cz * start_z + ca * start_a) % denom == mod:
            # print(f"{_, cx, cy, cz, ca, denom, mod, vx, vy, vz, va=}")
            # print(f"{start_x, start_y, start_z, start_a=}")
            cnt += 1
    return cnt


target = (9, 14, 59)
positions = {(3, (0, 0, 0))}
t = 0
counterzz = 0
while positions:
    counterzz += 1
    if counterzz > 1000:
        break
    next_positions = set()
    for life, pos in positions:
        if pos == target:
            print(f"FOUND! {t=}")
            break
        for dx, dy, dz in [
            (0, 0, 0),
            (-1, 0, 0),
            (1, 0, 0),
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
        ]:
            pos2 = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
            life2 = life - count_debris(*pos2, 0, t + 1)
            # print(f"Considering {pos2=} {t+1=}")

            if life2 < 0:
                continue
            if not (0 <= pos2[0] < 10 and 0 <= pos2[1] < 15 and 0 <= pos2[2] < 60):
                continue
            next_positions.add((life2, pos2))
            # print(f"Added {pos2=}")
    else:
        t += 1
        positions = sorted(next_positions, key=lambda x: (x[1:], x[0]))[-10000:]
        # positions = next_positions
        continue
    break

print(t)

# 82 not correct
# 165 not correct

print(answer3)
