with open("./input/01.txt", encoding="utf-8") as f:
    text = f.read()

answer = 0
for line in text.splitlines():
    sms = len(line.encode("utf-8")) <= 160
    twitter = len(line) <= 140

    if sms and twitter:
        answer += 13
    elif sms:
        answer += 11
    elif twitter:
        answer += 7

print(answer)
