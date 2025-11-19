import collections


with open("./2025/input/everybody_codes_e2025_q13_p1.txt") as f:
    lines = f.read().splitlines()
turns = 2025

q = collections.deque([1])
for i, line in enumerate(lines):
    num = int(line)
    if i % 2 == 0:
        q.append(num)
    else:
        q.appendleft(num)

answer = q[(q.index(1) + turns) % len(q)]
print(answer)
