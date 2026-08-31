import collections

with open("./input/4.txt") as f:
    lines = f.read().splitlines()

counts = collections.Counter()
for line in lines:
    s, expected = line.rsplit("|", 1)
    s += "|"
    expected = int(expected)
    actual = 0
    for c in s:
        actual ^= ord(c)

    if actual == expected:
        continue

    ops = s.rsplit("|", 2)[1]
    for i in range(0, len(ops), 2):
        counts[ops[i : i + 2]] += 1

counts_values = sorted(counts.values())
answer = counts_values[-1] * counts_values[-2]
print(answer)
