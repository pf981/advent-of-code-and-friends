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

answer = len(filled_borders)
print(answer)
