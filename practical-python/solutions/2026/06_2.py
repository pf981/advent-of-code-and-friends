with open("./input/2026/06/input2.txt") as f:
    lines = f.read().splitlines()

points = [tuple(map(int, line[:-2].split(","))) for line in lines]
underground = {p for p, (*_, c) in zip(points, lines) if c == "U"}

hull = []
p1 = leftmost = min(p for p in points if p not in underground)
points.sort(key=lambda p: p in underground)
outside = set()
while True:
    hull.append(p1)
    p2 = points[0]
    for p3 in points:
        if (
            p2 == p1
            or (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1]) < 0
        ):
            if p3 in underground:
                outside.add(p3)
            else:
                p2 = p3
    p1 = p2
    if p2 == leftmost:
        break

answer = len(hull) * (len(points) - len(outside))
print(answer)
