with open("./2024/input/everybody_codes_e2024_q14_p1.txt") as f:
    lines = f.read().splitlines()

# lines = 'U5,R3,D2,L5,U4,R5,D2'.splitlines()

h = 0
answer1 = 0
for direction, *d in lines[0].split(','):
    d = int(''.join(d))
    if direction == 'U':
        h += d
    elif direction == 'D':
        h -= d
    answer1 = max(answer1, h)

print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q14_p2.txt") as f:
    lines = f.read().splitlines()

# lines = '''U5,R3,D2,L5,U4,R5,D2
# U6,L1,D2,R3,U2,L1'''.splitlines()

# seen = {(0, 0, 0)}
seen = set()
for line in lines:
    x = y = z = 0
    for direction, *d in line.split(','):
        d = int(''.join(d))
        # print(f'{direction=} {d=}')
        dx = dy = dz = 0
        if direction == 'U':
            dy = 1
        elif direction == 'D':
            dy = -1
        elif direction == 'L':
            dx = -1
        elif direction == 'R':
            dx = 1
        elif direction == 'F':
            dz = 1
        elif direction == 'B':
            dz = -1
        else:
            print(f'Unknown: {direction=} {d=}')
        
        for _ in range(d):
            x += dx
            y += dy
            z += dz
            seen.add((x, y, z))

answer2 = len(seen)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q14_p3.txt") as f:
    lines = f.read().splitlines()


# lines = '''U5,R3,D2,L5,U4,R5,D2
# U6,L1,D2,R3,U2,L1'''.splitlines()

seen = set()
saps = set()
for line in lines:
    x = y = z = 0
    for direction, *d in line.split(','):
        d = int(''.join(d))
        # print(f'{direction=} {d=}')
        dx = dy = dz = 0
        if direction == 'U':
            dy = 1
        elif direction == 'D':
            dy = -1
        elif direction == 'L':
            dx = -1
        elif direction == 'R':
            dx = 1
        elif direction == 'F':
            dz = 1
        elif direction == 'B':
            dz = -1
        else:
            print(f'Unknown: {direction=} {d=}')
        
        for _ in range(d):
            x += dx
            y += dy
            z += dz
            seen.add((x, y, z))
    saps.add((x, y, z))

import collections

def get_distance(start_pos, end_pos, valid):
    q = collections.deque([start_pos])
    d = 0
    visited = {start_pos}
    while q:
        for _ in range(len(q)):
            pos = q.popleft()
            # print(f'{pos=} {d=}')
            if pos == end_pos:
                return d
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dz in [-1, 0, 1]:
                        # if dx == dy == dz == 0:
                        #     continue
                        if abs(dx) + abs(dy) + abs(dz) != 1:
                            continue
                        pos2 = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
                        if pos2 not in valid or pos2 in visited:
                            continue
                        visited.add(pos2)
                        q.append(pos2)
        d += 1

    return None

answer3 = float('inf')
y = 1
while (0, y, 0) in seen:
    d = sum(get_distance((0, y, 0), sap, seen) for sap in saps)
    answer3 = min(answer3, d)
    y += 1

print(answer3)

# get_distance((0, 1, 0), list(saps)[0], seen)

# list(saps)[0]
# seen
