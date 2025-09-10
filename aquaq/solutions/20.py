with open("./input/20.txt") as f:
    text = f.read()

answer = 0
possibilities = {0}
for card in text.strip().split():
    if card == "A":
        val = 11
    elif card in "JQK":
        val = 10
    else:
        val = int(card)

    possibilities2 = set()
    for p in possibilities:
        possibilities2.add(p + val)
        if card == "A":
            possibilities2.add(p + 1)

    possibilities = {p for p in possibilities2 if p <= 21}

    if 21 in possibilities:
        possibilities = {0}
        answer += 1
    if not possibilities:
        possibilities = {0}

print(answer)
