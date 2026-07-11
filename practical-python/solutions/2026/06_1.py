from functools import reduce


def is_ccw(p1, p2, p3) -> bool:
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1]) < 0


with open("./input/2026/06/input1.txt") as f:
    lines = f.read().splitlines()


points = [tuple(map(int, line.split(","))) for line in lines]
hull = []
p1 = start = min(points)
while True:
    hull.append(p1)

    candidates = (p for p in points if p != p1)
    p2 = reduce(lambda best, p3: p3 if is_ccw(p1, best, p3) else best, candidates)

    p1 = p2
    if p1 == start:
        break

answer = len(hull) * len(points)
print(answer)
