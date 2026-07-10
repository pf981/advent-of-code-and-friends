def is_cc(start: tuple[int, int], end: tuple[int, int], p: tuple[int, int]) -> bool:
    x1, y1 = start
    x2, y2 = end
    xp, yp = p
    return (y2 - y1) * (xp - x2) - (x2 - x1) * (yp - y2) < 0


with open("./input/2026/06/input1.txt") as f:
    lines = f.read().splitlines()


points = [tuple(map(int, line.split(","))) for line in lines]

hull = []
p = leftmost = min(points)
while True:
    hull.append(p)
    end = points[0]
    for p2 in points:
        if end == p or is_cc(p, p2, end):
            end = p2
    p = end
    if end == leftmost:
        break

answer = len(hull) * len(points)
print(answer)
