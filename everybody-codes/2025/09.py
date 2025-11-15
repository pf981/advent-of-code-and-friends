import collections


def parse(text: str) -> list[int]:
    m = {"A": 0b0001, "T": 0b0010, "C": 0b0100, "G": 0b1000}
    nums = []
    for line in text.splitlines():
        num = 0
        for i, c in enumerate(line.split(":")[1]):
            num |= m[c] << (i * 4)
        nums.append(num)

    return nums


with open("./2025/input/everybody_codes_e2025_q09_p1.txt") as f:
    text = f.read()

p1, p2, child = parse(text)

s1 = (p1 & child).bit_count()
s2 = (p2 & child).bit_count()

answer1 = s1 * s2
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q09_p2.txt") as f:
    text = f.read()

scales = parse(text)
n = len(scales)
n_set_bits = scales[0].bit_count()

answer2 = 0
for i_child in range(n):
    similarities = [
        ((scales[i_child] & scales[i_p]).bit_count(), i_p) for i_p in range(n)
    ]
    similarities.sort(reverse=True)

    for i1 in range(1, n):
        s1, i_p1 = similarities[i1]
        if s1 < n_set_bits // 2:
            break

        for i2 in range(i1 + 1, n):
            s2, i_p2 = similarities[i2]
            if s1 + s2 < n_set_bits:
                break

            child = scales[i_child]
            p1 = scales[i_p1]
            p2 = scales[i_p2]
            if (child & p1) | (child & p2) == child:
                answer2 += s1 * s2

print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q09_p3.txt") as f:
    text = f.read()

scales = parse(text)
n = len(scales)
n_set_bits = scales[0].bit_count()
parents = list(range(n))


def union(i: int, j: int) -> None:
    i = find(i)
    j = find(j)
    parents[i] = j


def find(i: int) -> int:
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


for i_child in range(n):
    similarities = [
        ((scales[i_child] & scales[i_p]).bit_count(), i_p) for i_p in range(n)
    ]
    similarities.sort(reverse=True)

    for i1 in range(1, n):
        s1, i_p1 = similarities[i1]
        if s1 < n_set_bits // 2:
            break

        for i2 in range(i1 + 1, n):
            s2, i_p2 = similarities[i2]
            if s1 + s2 < n_set_bits:
                break

            child = scales[i_child]
            p1 = scales[i_p1]
            p2 = scales[i_p2]
            if (child & p1) | (child & p2) == child:
                union(i_child, i_p1)
                union(i_child, i_p2)


groups: collections.defaultdict[int, list[int]] = collections.defaultdict(
    lambda: [0, 0]
)
for i in range(n):
    p = find(i)
    groups[p][0] += 1
    groups[p][1] += i + 1

answer3 = max(groups.values())[1]
print(answer3)
