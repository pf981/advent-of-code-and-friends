from collections import Counter

with open("./input/2026/08.txt") as f:
    lines = f.read().splitlines()

m = {}
for line in lines:
    start, end, *mid = line.split()

    for a, b in [(start, end), (end, start)]:
        out = "".join([a] + mid + [b])
        m[a + b] = Counter(out[i] + out[i + 1] for i in range(len(out) - 1))

cur = Counter(["AB"])
for _ in range(21):
    nxt = Counter()
    for a, count in cur.items():
        for b, count2 in m[a].items():
            nxt[b] += count * count2
    cur = nxt

answer = sum(cur.values()) + 1
print(answer)
