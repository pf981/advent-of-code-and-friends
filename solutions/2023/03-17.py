import collections
import heapq

import downloader


lines = downloader.get_puzzle(27).splitlines()
start, end = "TYC", "EAR"
stopping_time = 600

m = collections.defaultdict(list)
for line in lines:
    node, tos = line.split(" => ")
    for to in tos.split():
        node2, d_str = to.split(":")
        m[node].append((node2, int(d_str)))

seen = set()
heap = [(0, start)]
while heap:
    d, node = heapq.heappop(heap)

    if node in seen:
        continue
    seen.add(node)

    if node == end:
        break

    d += stopping_time

    for node2, d2 in m[node]:
        heapq.heappush(heap, (d + d2, node2))

answer = d - stopping_time
print(answer)
