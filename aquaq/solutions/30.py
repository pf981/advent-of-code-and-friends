with open("./input/30.txt") as f:
    text = f.read()

answer = 0
for line in text.splitlines():
    ones = line.count("1")
    if ones % 2 == 1:
        answer += ones // 2 + 1

print(answer)
