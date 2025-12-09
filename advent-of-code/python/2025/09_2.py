from aocd import get_data, submit


inp = get_data(day=9, year=2025)
# inp = """7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3
# """

lines = inp.splitlines()
nums = [tuple(int(x) for x in line.split(",")) for line in lines]
# nums = {tuple(int(x) for x in line.split(",")) for line in lines}

# important_xs = sorted({x for x, _ in nums})
# important_ys = sorted({y for _, y in nums})

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

polygon = Polygon(nums)
# print(polygon.contains(point))

answer2 = 0
for a in nums:
    for b in nums:
        w = abs(b[0] - a[0]) + 1
        h = abs(b[1] - a[1]) + 1
        for c in nums:
            x1 = min(a[0], b[0])
            x2 = max(a[0], b[0])
            y1 = min(a[1], b[1])
            y2 = max(a[1], b[1])
            if c == a or c == b:
                continue
            if c[0] in (x1, x2) and c[1] in (y1, y2):
                continue
            if x1 <= c[0] <= x2 and y1 <= c[1] <= y2:
                break
            # TODO: Check if middle point is inside
            mx = (x1 + x2) // 2
            my = (y1 + y2) // 2
            if not polygon.contains(Point(mx, my)):
                continue
        else:
            # if w * h > answer2:
            # print(f"{a=} {b=} {w=} {h=}")
            answer2 = max(answer2, (w * h))

print(answer2)
# for x, y in nums:

# print(answer2)
# answer1 = None
answer2 = answer2 or None
submit(answer2, part="b", day=9, year=2025)

# 4548962670 wrong
