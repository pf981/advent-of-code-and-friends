from collections import Counter

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

    out = "".join([a] + c + [b])
    m[(a + b)] = Counter(out[i] + out[i + 1] for i in range(len(out) - 1))

    a, b = b, a
    out = "".join([a] + c + [b])
    m[(a + b)] = Counter(out[i] + out[i + 1] for i in range(len(out) - 1))

cur = Counter(["AB"])
for _ in range(21):
    nxt = Counter()
    for a, count in cur.items():
        for b, count2 in m[a].items():
            nxt[b] += count * count2
    cur = nxt
    # print("".join(cur), len(cur))
answer = sum(cur.values()) + 1
print(answer)
