with open("data/day13.txt") as f:
    text = f.read()

evens = {}
odds = {}

for line in text.splitlines():
    op, what = line.split()

    if op == "plant":
        val = int(what)
        if val == 0:
            continue
        if val % 2 == 0:
            evens[val] = evens.get(val, 0) + 1
        else:
            odds[val] = odds.get(val, 0) + 1
        continue

    # spray
    if what == "even" or what == "all":
        target_items = evens.items()
        evens = {}
        for h, count in target_items:
            new_h = h // 2
            if new_h == 0:
                continue
            if new_h % 2 == 0:
                evens[new_h] = evens.get(new_h, 0) + count
            else:
                odds[new_h] = odds.get(new_h, 0) + count

    if what == "odd" or what == "all":
        target_items = odds.items()
        odds = {}
        for h, count in target_items:
            new_h = h // 2
            if new_h == 0:
                continue
            if new_h % 2 == 0:
                evens[new_h] = evens.get(new_h, 0) + count
            else:
                odds[new_h] = odds.get(new_h, 0) + count

answer = sum(h * count for h, count in evens.items()) + sum(
    h * count for h, count in odds.items()
)
print(answer)
