with open("./2025/input/everybody_codes_e2025_q16_p1.txt") as f:
    text = f.read().strip()
target = 90

spell = [int(x) for x in text.split(",")]
n = target
cols = [0] * target
for num in spell:
    for j in range(num - 1, target, num):
        cols[j] += 1

answer = sum(cols)
print(answer)
