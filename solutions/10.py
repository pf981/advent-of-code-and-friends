import numpy as np
from PIL import Image
import urllib

import downloader

url = "https://codingquest.io/may2022/010-inputdata-327485957345.png"
image_path = downloader.CQ_DATA_DIR / "10.png"

try:
    image = Image.open(image_path)
except FileNotFoundError:
    with urllib.request.urlopen(url) as f:
        data = f.read()

    with open(image_path, "wb") as f:
        f.write(data)

    image = Image.open(image_path)

r, g, b = image.split()
red_channel = np.array(r)

result = []
for chunk in red_channel.reshape(red_channel.size // 8, 8):
    num = 0
    for pixel in chunk:
        num = (num << 1) | (pixel & 1)
    result.append(chr(num))
    if not num:
        break

text = "".join(result)
# print(text)

answer = "".join(c for c in text.split()[-1] if c.isalpha())
print(answer)
