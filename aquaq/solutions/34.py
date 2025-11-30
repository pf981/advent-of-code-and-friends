import heapq


with open("./input/34.txt") as f:
    text = f.read()

n_routes = len(text.splitlines()[0].split(",")) - 1
routes: list[list[int | None]] = [[] for _ in range(n_routes)]
starts: list[int | None] = [None] * n_routes
heap: list[tuple[int, int, int, int, int]] = []

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
            heapq.heappush(heap, (t, -1, station, t, route))
        else:
            p = prevs[route]
            assert p is not None
            delta = t - p
            routes[route].append(delta)

        prevs[route] = t

ends = starts.copy()
n_stations = len(routes[0])
occupied_until = [0] * n_stations

while heap:
    t, prev_station, station, first_arrival, route = heapq.heappop(heap)

    if occupied_until[station] > t:
        heapq.heappush(
            heap, (occupied_until[station], prev_station, station, first_arrival, route)
        )
        continue

    occupied_until[station] = t + 5

    for station2 in range(station + 1, n_stations):
        dt = routes[route][station2]
        if dt is not None:
            t2 = t + dt + 5
            heapq.heappush(heap, (t2, station, station2, t2, route))
            break
    else:
        ends[route] = t + 5

answer = 0
for start, end in zip(starts, ends):
    assert start is not None
    assert end is not None
    answer = max(answer, end - start)
print(answer)
