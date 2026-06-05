import math

from PIL import Image

image = Image.open("./input/2025/05/input1.png")

w = math.isqrt(image.size[0])

it = iter(image.get_flattened_data())
dr, dc = -1, 1
r, c = 0, 0
result = [["."] * w for _ in range(w)]
for _ in range(w * w):
    r2 = r + dr
    c2 = c + dc
    if not (0 <= r2 < w and 0 <= c2 < w):
        if not (0 <= r2 < w):
            r2 = r
        if not (0 <= c2 < w):
            c2 = c
            if r2 == r:
                c2 = c - dc
        dr, dc = dc, dr
    r, c = r2, c2
    if next(it)[0] == 0:
        result[r][c] = "#"

# for row in result:
#     print("".join(row))

answer = 958013
print(answer)
