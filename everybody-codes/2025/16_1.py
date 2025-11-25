with open("./2025/input/everybody_codes_e2025_q16_p1.txt") as f:
    text = f.read().strip()
target = 90

spell = [int(x) for x in text.split(",")]
answer = 0
for num in spell:
    answer += len(range(num - 1, target, num))

print(answer)
