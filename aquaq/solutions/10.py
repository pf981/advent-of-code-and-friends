import collections
import heapq

with open("./input/10.txt") as f:
    text = f.read()

m = collections.defaultdict(list)
for line in text.splitlines()[1:]:
    source, dest, cost = line.split(",")
    m[source].append((dest, int(cost)))

heap = [(0, "DIDDY")]
seen = set()
while True:
    d, name = heapq.heappop(heap)

    if name in seen:
        continue
    seen.add(name)

    if name == "TUPAC":
        break

    for name2, dd in m[name]:
        heapq.heappush(heap, (d + dd, name2))

answer = d
print(answer)
