with open("./input/2026/08.txt") as f:
    lines = f.read().splitlines()
# lines = """A A C
# A B C
# A C B
# B B A B A
# B C B A
# C C B B""".splitlines()
m = {}
for line in lines:
    a, b, *c = line.split()
    if (a, b) in m:
        continue
    m[(a, b)] = [a] + c + [b]
    a, b = b, a
    m[(a, b)] = [a] + c + [b]

cur = list("AB")
for _ in range(7):
    # for _ in range(5):
    nxt = []
    for i in range(0, len(cur) - 1):
        pair = (cur[i], cur[i + 1])
        # print(pair)
        nxt.extend(m[pair])
        if i < len(cur) - 2:
            nxt.pop()
    cur = nxt
    # print("".join(cur), len(cur))
answer = len(cur)
print(answer)
