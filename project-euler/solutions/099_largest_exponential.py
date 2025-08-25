import math


with open("data/0099_base_exp.txt") as f:
    text = f.read()

best = (0.0, 0)
for i, line in enumerate(text.splitlines(), 1):
    base, exponent = line.split(",")
    d = int(exponent) * math.log(int(base))
    best = max(best, (d, i))

answer = best[1]
print(answer)
