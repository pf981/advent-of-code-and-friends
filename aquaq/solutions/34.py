import heapq

with open("./input/33.txt") as f:
    text = f.read()

text = """station,r1,r2,r3
a,00:01,,00:02
b,00:16,,00:17
c,,00:21,
d,00:46,00:51,00:47
"""

n_routes = len(text.splitlines()[0].split(",")) - 1
routes: list[list[int | None]] = [[] for _ in range(n_routes)]
starts = [None] * n_routes
heap: list[tuple[int, int, int]] = []

prevs: list[int | None] = [None] * n_routes
for line in text.splitlines()[1:]:
    _, *time_strs = line.split(",")

    for route, time_str in enumerate(time_strs):
        if not time_str:
            routes[route].append(None)
            continue

        h_str, m_str = time_str.split(":")
        t = 60 * int(h_str) + int(m_str)

        if starts[route] is None:
            starts[route] = t
            routes[route].append(0)

            station = len(routes[route]) - 1
            heapq.heappush(heap, (station, t, route))
        else:
            assert prevs[route] is not None
            delta = t - prevs[route]
            routes[route].append(delta)

        prevs[route] = t

# for route, stops in enumerate(routes):
#     for station, t in enumerate(stops):
#         if t is None:
#             continue
#         heapq.heappush(heap, (station, t, route))
#         starts[route] = t
#         break
ends = starts.copy()

while heap:
    station, t, route = heapq.heappop(heap)


answer = max(end - start for start, end in zip(starts, ends))
print(answer)
