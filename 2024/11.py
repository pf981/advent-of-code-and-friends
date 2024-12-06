import collections


with open("./2024/input/everybody_codes_e2024_q11_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''A:B,C
# B:C,A
# C:A'''.splitlines()

m = {}
for line in lines:
    # print(line)
    a, b = line.split(':')
    m[a] = collections.Counter(b.split(','))

counts = collections.Counter('A')

for _ in range(4):
    counts2 = collections.Counter()
    for c, cnt in counts.items():
        for c2, cnt2 in m[c].items():
            counts2[c2] += cnt * cnt2
    counts = counts2

answer1 = sum(counts.values())
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q11_p2.txt") as f:
    lines = f.read().splitlines()

m = {}
for line in lines:
    # print(line)
    a, b = line.split(':')
    m[a] = collections.Counter(b.split(','))

counts = collections.Counter('Z')

for _ in range(10):
    counts2 = collections.Counter()
    for c, cnt in counts.items():
        for c2, cnt2 in m[c].items():
            counts2[c2] += cnt * cnt2
    counts = counts2

answer2 = sum(counts.values())
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q11_p3.txt") as f:
    lines = f.read().splitlines()

# lines = '''A:B,C
# B:C,A,A
# C:A'''.splitlines()

m = collections.defaultdict()
for line in lines:
    # print(line)
    a, b = line.split(':')
    m[a] = collections.Counter(b.split(','))


def sim(start):
    counts = collections.Counter([start])

    for _ in range(20):
        counts2 = collections.Counter()
        for c, cnt in counts.items():
            for c2, cnt2 in m[c].items():
                counts2[c2] += cnt * cnt2
        counts = counts2

    return sum(counts.values())

l = []
for start in m:
    l.append(sim(start))


answer3 = max(l) - min(l)
print(answer3)
