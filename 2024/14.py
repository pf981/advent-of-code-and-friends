with open("./2024/input/everybody_codes_e2024_q14_p1.txt") as f:
    lines = f.read().splitlines()

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

seen = set()
for line in lines:
    x = y = z = 0
    for direction, *d in line.split(','):
        d = int(''.join(d))
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
        
        for _ in range(d):
            x += dx
            y += dy
            z += dz
            seen.add((x, y, z))

answer2 = len(seen)
print(answer2)


# Part 3


import collections


def get_distance(start_pos: tuple[int, int, int], end_pos: tuple[int, int, int], valid: set[tuple[int, int, int]]):
    q = collections.deque([start_pos])
    d = 0
    visited = {start_pos}
    while q:
        for _ in range(len(q)):
            pos = q.popleft()
            if pos == end_pos:
                return d
            
            for delta in [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0)]:
                pos2 = (pos[0] + delta[0], pos[1] + delta[1], pos[2] + delta[2])
                if pos2 not in valid or pos2 in visited:
                    continue
                visited.add(pos2)
                q.append(pos2)
        d += 1
    return None


with open("./2024/input/everybody_codes_e2024_q14_p3.txt") as f:
    lines = f.read().splitlines()

seen = set()
saps = set()
for line in lines:
    x = y = z = 0
    for direction, *d in line.split(','):
        d = int(''.join(d))
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
        
        for _ in range(d):
            x += dx
            y += dy
            z += dz
            seen.add((x, y, z))
    saps.add((x, y, z))

answer3 = float('inf')
y = 1
while (0, y, 0) in seen:
    d = sum(get_distance((0, y, 0), sap, seen) for sap in saps)
    answer3 = min(answer3, d)
    y += 1

print(answer3)
