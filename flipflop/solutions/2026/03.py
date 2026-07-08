import itertools


with open("./input/2026/03.txt") as f:
    text = f.read()
lines = text.splitlines()

score_password = (0, "")
for line in lines:
    score = any(c in line for c in "abcdefghijklmnopqrstuvwxyz")
    score += any(c in line for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    score += any(c in line for c in "1234567890")
    score_password = max(score_password, (score * len(line), line))

answer1 = score_password[1]
print(answer1)


score_password = (0, "")
for line in lines:
    score = any(c in line for c in "abcdefghijklmnopqrstuvwxyz")
    score += any(c in line for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    score += any(c in line for c in "1234567890")

    if all(c not in line for c in "123456890") and "7" in line:
        score += 7

    longest = max(len(list(group)) for _, group in itertools.groupby(line))
    if longest >= 3:
        score += longest**2

    if any(c in line for c in ["red", "green", "blue"]):
        score *= 3
    score *= len(line)
    score_password = max(score_password, (score, line))

answer2 = score_password[1]
print(answer2)


answer3 = 0
for suffix in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
    total = 0
    for line in lines:
        line += suffix

        score = any(c in line for c in "abcdefghijklmnopqrstuvwxyz")
        score += any(c in line for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        score += any(c in line for c in "1234567890")

        if all(c not in line for c in "123456890") and "7" in line:
            score += 7

        longest = max(len(list(group)) for _, group in itertools.groupby(line))
        if longest >= 3:
            score += longest**2

        if any(c in line for c in ["red", "green", "blue"]):
            score *= 3
        score *= len(line)
        total += score
    answer3 = max(answer3, total)

print(answer3)
