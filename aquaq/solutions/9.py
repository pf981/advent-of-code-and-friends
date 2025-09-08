import math

with open("./input/9.txt") as f:
    text = f.read()

answer = math.prod(int(x) for x in text.splitlines())
print(answer)
