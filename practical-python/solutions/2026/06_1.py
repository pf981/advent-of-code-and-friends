def is_cc(p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2) < 0


with open("./input/2026/06/input1.txt") as f:
    lines = f.read().splitlines()


points = [tuple(map(int, line.split(","))) for line in lines]
hull = []
p = leftmost = min(points)
while True:
    hull.append(p)
    p2 = points[0]
    for candidate in points:
        if p2 == p or is_cc(p, candidate, p2):
            p2 = candidate
    p = p2
    if p2 == leftmost:
        break

answer = len(hull) * len(points)
print(answer)
