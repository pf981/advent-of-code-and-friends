import math

with open("./input/4.txt") as f:
    text = f.read()

n = int(text)
answer = 0
for i in range(1, n):
    if math.gcd(i, n) == 1:
        answer += i

print(answer)
