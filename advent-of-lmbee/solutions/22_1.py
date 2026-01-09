import itertools
import re

with open("data/day22.txt") as f:
    text = f.read()

users = list(itertools.batched(map(int, re.findall(r"\d+", text)), 3))

answer = 0
for _, fav_digit, fav_num in users:
    for i in itertools.count(1):
        num = fav_num * i

        s = str(num)
        if s.count(str(fav_digit)) >= len(s) / 2:
            break

    answer += num

print(answer)
