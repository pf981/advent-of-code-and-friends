with open("data/day13.txt") as f:
    text = f.read()

evens = odds = answer = 0
for line in reversed(text.splitlines()):
    op, what = line.split()
    if op == "plant":
        num = int(what)
        answer += num
        answer += odds if num % 2 else evens
        continue

    if what == "even":
        evens = odds + 1
    elif what == "odd":
        odds = evens + 1
    else:
        evens, odds = odds + 1, evens + 1

print(answer)
