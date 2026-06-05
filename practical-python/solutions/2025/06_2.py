import collections
import heapq
import math

with open("./input/2025/06/input2.txt") as f:
    lines = f.read().splitlines()

known = []
for line in lines[1:]:
    *p, name = line.split(",")
    known.append((tuple(map(float, p)), name))

result = []
for unknown in lines[0].split():
    p1 = tuple(map(float, unknown.split(",")))
    closest = heapq.nsmallest(7, ((math.dist(p1, p2), name) for p2, name in known))
    counts = collections.Counter(name for _, name in closest)
    result.append(counts.most_common(1)[0][0])

answer = "".join(result)
print(answer)
