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
    a, *b = line.split()
    if a in m:
        continue
    m[a] = Counter(b)

counts = Counter("AB")
for _ in range(7):
    counts2 = Counter()
    for a, count in counts.items():
        for b, count2 in m[a].items():
            counts2[b] += count * count2
    counts = counts2
    # break
answer = sum(counts.values())
print(answer)
