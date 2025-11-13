with open("./2025/input/everybody_codes_e2025_q09_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """1:CAAGCGCTAAGTTCGCTGGATGTGTGCCCGCG
# 2:CTTGAATTGGGCCGTTTACCTGGTTTAACCAT
# 3:CTAGCGCTGAGCTGGCTGCCTGGTTGACCGCG""".splitlines()

child = lines[2][2:]
p1 = lines[1][2:]
p2 = lines[0][2:]

x = y = 0
for a, b in zip(child, p1):
    x += a == b
for a, b in zip(child, p2):
    y += a == b

answer1 = x * y
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q09_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
# 2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
# 3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
# 4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
# 5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
# 6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
# 7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG""".splitlines()

scales = []
for line in lines:
    scales.append(line.split(":")[1])

n = len(scales)

assert len(scales) == len(set(scales))

similarities = []
for i in range(n):
    child = scales[i]
    for p1i in range(n):
        p1 = scales[p1i]
        if p1 == child:
            continue
        for p2i in range(p1i + 1, n):
            p2 = scales[p2i]
            if p2 in (p1, child):
                continue

            # print(f"{child=} {p1=} {p2=}")
            d1 = d2 = 0
            for cc, a, b in zip(child, p1, p2):
                if cc not in (a, b):
                    break
                d1 += cc == a
                d2 += cc == b
            else:
                similarities.append(d1 * d2)

answer2 = sum(similarities)
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q09_p3.txt") as f:
    lines = f.read().splitlines()


# lines = """1:GCAGGCGAGTATGATACCCGGCTAGCCACCCC
# 2:TCTCGCGAGGATATTACTGGGCCAGACCCCCC
# 3:GGTGGAACATTCGAAAGTTGCATAGGGTGGTG
# 4:GCTCGCGAGTATATTACCGAACCAGCCCCTCA
# 5:GCAGCTTAGTATGACCGCCAAATCGCGACTCA
# 6:AGTGGAACCTTGGATAGTCTCATATAGCGGCA
# 7:GGCGTAATAATCGGATGCTGCAGAGGCTGCTG
# 8:GGCGTAAAGTATGGATGCTGGCTAGGCACCCG""".splitlines()

scales = []
for line in lines:
    scales.append(line.split(":")[1])

n = len(scales)

assert len(scales) == len(set(scales))

parents = list(range(n))


def union(i, j):
    i = find(i)
    j = find(j)
    parents[i] = j


def find(i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


similarities = []
for i in range(n):
    child = scales[i]
    for p1i in range(n):
        p1 = scales[p1i]
        if p1 == child:
            continue
        for p2i in range(p1i + 1, n):
            p2 = scales[p2i]
            if p2 in (p1, child):
                continue

            # print(f"{child=} {p1=} {p2=}")
            d1 = d2 = 0
            for cc, a, b in zip(child, p1, p2):
                if cc not in (a, b):
                    break
                d1 += cc == a
                d2 += cc == b
            else:
                similarities.append(d1 * d2)
                union(i, p1i)
                union(i, p2i)

import collections

groups = collections.Counter()
for i in range(n):
    groups[find(i)] += i + 1

answer3 = max(groups.values())
print(answer3)
