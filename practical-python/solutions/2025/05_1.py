import math

from PIL import Image

image = Image.open("./input/2025/05/input1.png")

w = math.isqrt(image.size[0])

# it = iter(image.get_flattened_data())
# for r in range(w):
#     for c in range(w):
#         print("X" if next(it)[0] == 0 else ".", end="")
#     print()

answer = 7462
print(answer)
