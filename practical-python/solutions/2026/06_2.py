from functools import reduce


def is_ccw(p1, p2, p3) -> bool:
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1]) < 0


with open("./input/2026/06/input2.txt") as f:
    lines = f.read().splitlines()

points = [tuple(map(int, line[:-2].split(","))) for line in lines]
underground = {p for p, (*_, c) in zip(points, lines) if c == "U"}

hull = []
p1 = start = min(p for p in points if p not in underground)
outside = set()
while True:
    hull.append(p1)

    candidates = (p for p in points if p != p1 and p not in underground)
    p2 = reduce(lambda best, p3: p3 if is_ccw(p1, best, p3) else best, candidates)

    outside |= {p3 for p3 in underground if is_ccw(p1, p2, p3)}

    p1 = p2
    if p1 == start:
        break

answer = len(hull) * (len(points) - len(outside))
print(answer)
