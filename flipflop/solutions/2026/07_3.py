import collections

with open("./input/2026/07.txt") as f:
    lines = f.read().splitlines()

ops, _, *sushi = lines
sushi = [tuple(map(int, line.split(","))) for line in sushi]
sushi.reverse()

self_eats = x = y = 0
q = collections.deque([(0, 0)])
for op in ops:
    x += (op == ">") - (op == "<")
    y += (op == "^") - (op == "v")
    if sushi and (x, y) == sushi[-1]:
        sushi.pop()
    else:
        q.popleft()

    if (x, y) in q:
        self_eats += 1
        while (x, y) in q:
            q.popleft()
        q.popleft()

    q.append((x, y))

answer = len(q) * self_eats
print(answer)
