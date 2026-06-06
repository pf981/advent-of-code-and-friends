import collections

from PIL import Image

image = Image.open("./input/2025/07/input2.png")
counts = collections.Counter(image.get_flattened_data())
result = []
m = {
    "0": "O",
    "1": "I",
    "5": "S",
}
for (r, g, b), _ in counts.most_common(3):
    s = f"{r:02X}{g:02X}{b:02X}"
    result.append("".join(m.get(c, c) for c in s))

answer = " ".join(result)
print(answer)
