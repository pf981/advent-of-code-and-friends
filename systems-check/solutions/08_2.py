import heapq

with open("./input/8.txt") as f:
    text = f.read()

part1, part2 = text.split("\n\n")

m = {}  # node -> (node2, d)
non_roots = set()
for line in part1.splitlines():
    node1 = line[:3]
    node2 = line[-3:]
    d = int(line.split("[")[1].split("]")[0])

    m[node1] = (node2, d)
    non_roots.add(node2)

delays = {}  # node -> delay
for line in part2.splitlines():
    node, delay = line.split()
    delay = int(delay)
    if delay:
        delays[node] = delay

heap = []  # [(t, node), ...]
for node in m:
    if node in non_roots:
        continue
    heapq.heappush(heap, (0, node))

answer = None
while heap:
    t, node = heapq.heappop(heap)

    if node in delays:
        heapq.heappush(heap, (t + delays[node], node))
        del delays[node]
        continue

    if node not in m:
        answer = t
        break

    node2, d = m[node]
    heapq.heappush(heap, (t + d, node2))

assert answer is not None
print(answer)
