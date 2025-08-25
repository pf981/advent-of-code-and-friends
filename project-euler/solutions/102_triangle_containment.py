type Point = tuple[int, int]


def determinant(p1: Point, p2: Point, p3: Point) -> int:
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def contains_origin(triangle: tuple[Point, Point, Point]):
    origin = (0, 0)

    det1 = determinant(origin, triangle[0], triangle[1]) < 0
    det2 = determinant(origin, triangle[1], triangle[2]) < 0
    det3 = determinant(origin, triangle[2], triangle[0]) < 0

    return det1 == det2 == det3


with open("data/0102_triangles.txt") as f:
    text = f.read()

triangles = []
for line in text.splitlines():
    x1, y1, x2, y2, x3, y3 = (int(s) for s in line.split(","))
    coords = ((x1, y1), (x2, y2), (x3, y3))
    triangles.append((coords))

answer = sum(contains_origin(triangle) for triangle in triangles)
print(answer)
