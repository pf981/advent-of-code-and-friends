from shapely.geometry.polygon import Polygon

from aocd import get_data, submit


inp = get_data(day=9, year=2025)
lines = inp.splitlines()
nums = [[int(x) for x in line.split(",")] for line in lines]

polygon = Polygon(nums)

answer2 = 0
for a in nums:
    for b in nums:
        w = abs(b[0] - a[0]) + 1
        h = abs(b[1] - a[1]) + 1

        if w * h <= answer2:
            continue

        x1 = min(a[0], b[0])
        x2 = max(a[0], b[0])
        y1 = min(a[1], b[1])
        y2 = max(a[1], b[1])

        rect = Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])
        if not polygon.covers(rect):
            continue

        answer2 = w * h

submit(answer2, part="b", day=9, year=2025)
