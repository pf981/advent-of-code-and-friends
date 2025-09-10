with open("./input/20.txt") as f:
    text = f.read()

answer = 0
possibilities = {0}

values = {
    "A": [1, 11],
    "J": [10],
    "Q": [10],
    "K": [10],
    **{str(i): [i] for i in range(2, 11)},
}

for card in text.split():
    next_poss = set()
    for p in possibilities:
        for val in values[card]:
            total = p + val
            if total <= 21:
                next_poss.add(total)

    if 21 in next_poss:
        answer += 1
        possibilities = {0}
    else:
        possibilities = next_poss or {0}

print(answer)
