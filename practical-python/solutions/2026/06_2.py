def is_cc(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2) < 0


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
    p2 = points[0][:-1]
    for candidate in points:
        c = candidate[-1]
        candidate = candidate[:-1]
        if p2 == p or is_cc(p, candidate, p2):
            if c == "U":
                outside.add(candidate)
            else:
                p2 = candidate
    p = p2
    if p2 == leftmost:
        break

answer = len(hull) * (len(points) - len(outside))
print(answer)
