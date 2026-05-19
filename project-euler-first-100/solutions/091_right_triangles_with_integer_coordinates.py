import math


n = 51
answer = 0

p0 = (0, 0)
for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                p1 = (x1, y1)
                p2 = (x2, y2)

                if p1 >= p2:
                    continue
                if (0, 0) in [p1, p2]:
                    continue

                d1 = math.dist(p0, p1)
                d2 = math.dist(p0, p2)
                d3 = math.dist(p1, p2)

                d1, d2, d3 = sorted([d1, d2, d3])

                if math.isclose(d3 * d3, d1 * d1 + d2 * d2):
                    answer += 1

print(answer)
