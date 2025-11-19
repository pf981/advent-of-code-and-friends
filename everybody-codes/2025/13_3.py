import collections


with open("./2025/input/everybody_codes_e2025_q13_p3.txt") as f:
    lines = f.read().splitlines()
turns = 202520252025

q = collections.deque([1])
for i, line in enumerate(lines):
    start, end = line.split("-")
    fn = q.append if i % 2 == 0 else q.appendleft
    for num in range(int(start), int(end) + 1):
        fn(num)

answer = q[(q.index(1) + turns) % len(q)]
print(answer)
