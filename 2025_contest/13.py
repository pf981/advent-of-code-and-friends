import collections
import math
import heapq


with open("2025_contest/13.txt") as f:
    inp = f.read()

# inp = """STT -> MFP | 5
# AIB -> ZGK | 6
# ZGK -> KVX | 20
# STT -> AFG | 4
# AFG -> ZGK | 16
# MFP -> BDD | 13
# BDD -> AIB | 5
# AXU -> MFP | 4
# CLB -> BLV | 20
# AIB -> BDD | 13
# BLV -> AXU | 17
# AFG -> CLB | 2"""

m = collections.defaultdict(list)
for line in inp.splitlines():
    src, _, dst, _, d = line.split()
    d = int(d)
    m[src].append(dst)

distances = {}
q = collections.deque([(0, "STT")])
while q:
    for _ in range(len(q)):
        d, node = q.popleft()
        if node in distances:
            continue
        distances[node] = d
        for node2 in m[node]:
            q.append((d + 1, node2))

# print(distances)
answer1 = math.prod(sorted(distances.values())[-3:])
print(answer1)


# Part 2

with open("2025_contest/13.txt") as f:
    inp = f.read()

# inp = """STT -> MFP | 5
# AIB -> ZGK | 6
# ZGK -> KVX | 20
# STT -> AFG | 4
# AFG -> ZGK | 16
# MFP -> BDD | 13
# BDD -> AIB | 5
# AXU -> MFP | 4
# CLB -> BLV | 20
# AIB -> BDD | 13
# BLV -> AXU | 17
# AFG -> CLB | 2"""

m = collections.defaultdict(list)
for line in inp.splitlines():
    src, _, dst, _, d = line.split()
    d = int(d)
    m[src].append((dst, d))

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


with open("2025_contest/13.txt") as f:
    inp = f.read()

# inp = """STT -> MFP | 5
# AIB -> ZGK | 6
# ZGK -> KVX | 20
# STT -> AFG | 4
# AFG -> ZGK | 16
# MFP -> BDD | 13
# BDD -> AIB | 5
# AXU -> MFP | 4
# CLB -> BLV | 20
# AIB -> BDD | 13
# BLV -> AXU | 17
# AFG -> CLB | 2"""

m = collections.defaultdict(list)
for line in inp.splitlines():
    src, _, dst, _, d = line.split()
    d = int(d)
    m[src].append((dst, d))


start_node = ...
longest_cycle = 0
seen = set()
d = 0


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
