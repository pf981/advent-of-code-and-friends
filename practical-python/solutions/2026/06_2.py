def is_cc(start: tuple[int, int], end: tuple[int, int], p: tuple[int, int]) -> bool:
    x1, y1 = start
    x2, y2 = end
    xp, yp = p
    return (y2 - y1) * (xp - x2) - (x2 - x1) * (yp - y2) < 0


with open("./input/2026/06/input2.txt") as f:
    lines = f.read().splitlines()


points = []
for line in lines:
    x, y, c = line.split(",")
    points.append((int(x), int(y), c))

hull = []
p = leftmost = min(p[:-1] for p in points if p[-1] != "U")
points.sort(key=lambda p: p[-1] == "U")
outside = set()
while True:
    hull.append(p)
    end = points[0][:-1]
    for p2 in points:
        c = p2[-1]
        p2 = p2[:-1]
        if end == p or is_cc(p, p2, end):
            if c == "U":
                outside.add(p2)
            else:
                end = p2
    p = end
    if end == leftmost:
        break

answer = len(hull) * (len(points) - len(outside))
print(answer)
