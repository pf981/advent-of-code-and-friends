import math

import downloader


lines = downloader.get_puzzle(3).splitlines()

pos = [0, 0, 0]
answer = 0
for line in lines:
    pos2 = [int(s) for s in line.split()]
    d = math.sqrt(sum((x2 - x1) ** 2 for x1, x2 in zip(pos, pos2)))
    answer += int(d)
    pos = pos2

print(answer)
