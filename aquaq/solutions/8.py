import collections

with open("./input/8.txt") as f:
    text = f.read()

q: collections.deque[list[int]] = collections.deque()
cereal = milk = 0
for t, line in enumerate(text.splitlines()[1:], 1):
    _, milk_str, cereal_str = line.split(",")

    # Buy cereal
    cereal += int(cereal_str)

    # Use 100ml milk, 100g cereal
    d = min(milk, cereal, 100)
    milk -= d
    cereal -= d

    while d:
        if q[0][1] > d:
            q[0][1] -= d
            d = 0
        else:
            d -= q.popleft()[1]

    # Expire milk
    if q and q[0][0] == t:
        milk -= q.popleft()[1]

    # Buy milk
    milk += int(milk_str)
    q.append([t + 5, int(milk_str)])

answer = milk + cereal
print(answer)
