import math
import re


def circle_circle_intersections(
    x1: int, y1: int, r1: int, x2: int, y2: int, r2: int
) -> list[tuple[int, int]]:
    dx = x2 - x1
    dy = y2 - y1
    d = math.hypot(dx, dy)

    # No intersection if:
    # - too far apart
    # - one circle inside the other
    # - same centre
    if d > r1 + r2 or d < abs(r1 - r2) or d == 0:
        return []

    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h_sq = r1 * r1 - a * a
    if h_sq < 0:
        return []
    h = math.sqrt(h_sq)

    x3 = x1 + a * dx / d
    y3 = y1 + a * dy / d

    rx = -dy * (h / d)
    ry = dx * (h / d)

    points = [
        (math.floor(x3 + rx), math.floor(y3 + ry)),
        (math.floor(x3 - rx), math.floor(y3 - ry)),
    ]
    for x, y in points.copy():
        points.append((x + 1, y))
        points.append((x, y + 1))
        points.append((x + 1, y + 1))

    return points


def count_overlaps(x: int, y: int, circles: list[list[int]]) -> int:
    overlaps = 0
    for x1, y1, r in circles:
        overlaps += math.dist((x, y), (x1, y1)) <= r
    return overlaps


with open("data/day20.txt") as f:
    text = f.read()

circles = [[int(x) for x in re.findall(r"\d+", line)] for line in text.splitlines()]
n = len(circles)

# I believe there are two possibilities for where the point could be.
#     1. If a circle is fully contained within the region of most overlap,
#        then every point in that circle will be the solution
#     2. Otherwise, the point must lie on the edge intersection of two circles
#
# It can't be (1) because we know there is exactly 1 solution. That would only
# work if there was a tiny circle with only one integer coordinate.
#
# There not being a third option is a hand-waving assumption. So it "must" be (2).
#
# So just iterate through all of the intesections and count the overlaps at
# those points. Try integer coordinates around the intersections.


best = 0, 0, 0  # overlap, x, y
for i in range(n):
    for j in range(i + 1, n):
        for x, y in circle_circle_intersections(*circles[i], *circles[j]):
            best = max(best, (count_overlaps(x, y, circles), x, y))

answer = best[1] * best[2]
print(answer)
