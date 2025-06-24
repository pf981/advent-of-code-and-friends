import functools

import downloader

lines = downloader.get_puzzle(25).splitlines()
n = len(lines)
m = [[int(s) for s in line.split()] for line in lines]


@functools.cache
def tsp(pos, visited_mask):
    if visited_mask == (1 << n) - 1:
        return m[pos][0]

    min_cost = float("inf")
    for next_city in range(n):
        if visited_mask & (1 << next_city):
            continue

        new_mask = visited_mask | (1 << next_city)
        cost = m[pos][next_city] + tsp(next_city, new_mask)
        min_cost = min(min_cost, cost)

    return min_cost


answer = tsp(0, 1)
print(answer)
