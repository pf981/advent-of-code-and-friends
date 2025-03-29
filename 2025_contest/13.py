import collections
import math
import heapq


with open("2025_contest/13.txt") as f:
    inp = f.read()

m = collections.defaultdict(list)
for line in inp.splitlines():
    src, _, dst, _, d = line.split()
    m[src].append((dst, int(d)))

distances = {"STT": 0}
q = collections.deque(["STT"])
d = 1
while q:
    for _ in range(len(q)):
        node = q.popleft()
        for node2, _ in m[node]:
            if node2 in distances:
                continue
            distances[node2] = d
            q.append(node2)
    d += 1

answer1 = math.prod(sorted(distances.values())[-3:])
print(answer1)


# Part 2

distances = {}
heap = [(0, "STT")]
while heap:
    d, node = heapq.heappop(heap)
    if node in distances:
        continue
    distances[node] = d
    for node2, d2 in m[node]:
        if node2 in distances:
            continue
        heapq.heappush(heap, (d + d2, node2))

answer2 = math.prod(sorted(distances.values())[-3:])
print(answer2)


# Part 3

longest_cycle = 0


def backtrack(node):
    global longest_cycle
    global d
    if node == start_node:
        longest_cycle = max(longest_cycle, d)

    for node2, dd in m[node]:
        if node2 in seen:
            continue

        seen.add(node2)
        d += dd
        backtrack(node2)
        d -= dd
        seen.remove(node2)


for node in m.copy():
    start_node = node
    seen = set()
    d = 0
    backtrack(node)

answer3 = longest_cycle
print(answer3)
