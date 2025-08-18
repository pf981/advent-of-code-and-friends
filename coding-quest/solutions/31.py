import math

import downloader

lines = downloader.get_puzzle(31).splitlines()

positions = []
for line in lines[1:]:
    name = line.split("  ")[0]
    pos = [float(x) for x in line.split()[-3:]]
    positions.append(pos)

n = len(positions)
answer = float("inf")
for i in range(n):
    for j in range(i + 1, n):
        d = math.sqrt(sum((b - a) ** 2 for a, b in zip(positions[i], positions[j])))
        answer = min(answer, d)

answer = round(answer, 3)
print(answer)
