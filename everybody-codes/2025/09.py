import collections


with open("./2025/input/everybody_codes_e2025_q09_p1.txt") as f:
    lines = f.read().splitlines()

p1, p2, child = [line.split(":")[1] for line in lines]

s1 = sum(a == b for a, b in zip(child, p1))
s2 = sum(a == b for a, b in zip(child, p2))

answer1 = s1 * s2
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q09_p2.txt") as f:
    lines = f.read().splitlines()

scales = [line.split(":")[1] for line in lines]
n = len(scales)

answer2 = 0
for i_child in range(n):
    for i_p1 in range(n):
        if i_p1 == i_child:
            continue
        for i_p2 in range(i_p1 + 1, n):
            if i_p2 in (i_p1, i_child):
                continue

            d1 = d2 = 0
            for child, p1, p2 in zip(scales[i_child], scales[i_p1], scales[i_p2]):
                if child not in (p1, p2):
                    break
                d1 += child == p1
                d2 += child == p2
            else:
                answer2 += d1 * d2

print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q09_p3.txt") as f:
    lines = f.read().splitlines()


scales = [line.split(":")[1] for line in lines]
n = len(scales)
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


for i_child in range(n):
    for i_p1 in range(n):
        if i_p1 == i_child:
            continue
        for i_p2 in range(i_p1 + 1, n):
            if i_p2 in (i_p1, i_child):
                continue

            if all(
                child in (p1, p2)
                for child, p1, p2 in zip(scales[i_child], scales[i_p1], scales[i_p2])
            ):
                union(i_child, i_p1)
                union(i_child, i_p2)


groups: collections.Counter[int] = collections.Counter()
for i in range(n):
    groups[find(i)] += i + 1

answer3 = max(groups.values())
print(answer3)
