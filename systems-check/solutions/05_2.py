import functools

with open("./input/5.txt") as f:
    lines = f.read().splitlines()

borders = set()
for line in lines:
    points = [list(map(int, part.split(","))) for part in line.split()]
    prev = points[-1].copy()
    for cur in points:
        dx = (cur[0] - prev[0]) // max(abs(cur[0] - prev[0]), 1)
        dy = (cur[1] - prev[1]) // max(abs(cur[1] - prev[1]), 1)

        borders.add(tuple(prev))
        while prev != cur:
            prev[0] += dx
            prev[1] += dy
            borders.add(tuple(prev))

filled_borders = set()
min_x = min(x for x, _ in borders) - 2
min_y = min(y for _, y in borders) - 2
max_x = max(x for x, _ in borders) + 2
max_y = max(y for _, y in borders) + 2
filled = {(min_x, min_y)}
stack = [(min_x, min_y)]
while stack:
    x, y = stack.pop()

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            x2 = x + dx
            y2 = y + dy

            if not (min_x <= x2 <= max_x and 0 <= y2 <= max_y):
                continue
            if (x2, y2) in filled:
                continue
            filled.add((x2, y2))

            if (x2, y2) in borders:
                filled_borders.add((x2, y2))
            else:
                stack.append((x2, y2))


def flood(x: int, y: int) -> int:
    if (x, y) not in filled_borders:
        return 0

    filled_borders.remove((x, y))
    return 1 + flood(x - 1, y) + flood(x + 1, y) + flood(x, y - 1) + flood(x, y + 1)


polygons = {}  # (x, y) -> border_size
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) not in filled_borders:
            continue
        polygons[(x, y)] = flood(x, y)

required_travel = sum(polygons.values())
polygons = list(polygons)
target = (1 << len(polygons)) - 1


@functools.cache
def get_min_dist(x: int, y: int, used: int) -> int:
    if used == target:
        return abs(x) + abs(y)

    min_dist = 10**7
    for i, (x2, y2) in enumerate(polygons):
        if used & (1 << i):
            continue

        d = abs(x2 - x) + abs(y2 - y) + get_min_dist(x2, y2, used | (1 << i))
        min_dist = min(min_dist, d)

    return min_dist


answer = get_min_dist(0, 0, 0) + required_travel
print(answer)
