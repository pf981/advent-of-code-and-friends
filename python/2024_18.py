from aocd import get_data, submit
import re
import collections

inp = get_data(day=18, year=2024)
max_x = max_y = 70
first_n = 1024
target = (70, 70)

# inp = '''5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0
# '''
# max_x = max_y = 6
# first_n = 12


target = (max_x, max_y)

lines = inp.splitlines()


corrupted = set()
for i, line in enumerate(lines):
    if i == first_n:
        break
    xx, yy = map(int, re.findall(r'-?[0-9]+', line))
    corrupted.add((xx, yy))

seen = {(0, 0)}
q = collections.deque([(0, 0, ((0, 0),))])
d = 0
while q:
    for _ in range(len(q)):
        x, y, path = q.popleft()
        if (x, y) == target:
            answer1 = d
            final_path = path
            break
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x2 = x + dx
            y2 = y + dy
            if not (0 <= x2 <= max_x) or not (0 <= y2 <= max_y) or (x2, y2) in seen or (x2, y2) in corrupted:
                continue
            seen.add((x2, y2))
            q.append((x2, y2, path + ((x2, y2),)))
    d += 1

# answer1 = 'todo'
print(answer1)

# submit(answer1, part='a', day=18, year=2024)


# Part 2


def can_solve():

    seen = {(0, 0)}
    q = collections.deque([(0, 0, (0, 0))])
    d = 0
    while q:
        for _ in range(len(q)):
            x, y, path = q.popleft()
            if (x, y) == target:
                return True
                break
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                x2 = x + dx
                y2 = y + dy
                if not (0 <= x2 <= max_x) or not (0 <= y2 <= max_y) or (x2, y2) in seen or (x2, y2) in corrupted:
                    continue
                seen.add((x2, y2))
                q.append((x2, y2, path + ((x2, y2),)))
        d += 1
    return False



corrupted = set()
for i, line in enumerate(lines):
    xx, yy = map(int, re.findall(r'-?[0-9]+', line))
    corrupted.add((xx, yy))
    if not can_solve():
        answer2 = f'{xx},{yy}'
        break


# for x, y in final_path:
#     if (x, y) in corrupted:
#         print('???')
#     print(f'{x=} {y=}')
#     corrupted.add((x, y))
#     if not can_solve():
#         answer2 = f'{x},{y}'
#     corrupted.remove((x, y))

print(answer2)

submit(answer2, part='b', day=18, year=2024)
