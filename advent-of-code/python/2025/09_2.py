import heapq

from shapely.geometry.polygon import Polygon
from aocd import get_data, submit


inp = get_data(day=9, year=2025)
lines = inp.splitlines()
nums = [[int(x) for x in line.split(",")] for line in lines]

polygon = Polygon(nums)
heap = []

for x1, y1 in nums:
    for x2, y2 in nums:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        w = x2 - x1 + 1
        h = y2 - y1 + 1

        heapq.heappush(heap, (-w * h, x1, x2, y1, y2))

answer2 = None
while heap:
    neg_area, x1, x2, y1, y2 = heapq.heappop(heap)
    rect = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
    if polygon.covers(rect):
        answer2 = -neg_area
        break

assert answer2
submit(answer2, part="b", day=9, year=2025)
