import collections
import itertools


with open("./2025/input/everybody_codes_e2025_q08_p1.txt") as f:
    lines = f.read().splitlines()

nails = 32
nums = [int(x) - 1 for x in lines[0].split(",")]

answer1 = sum(abs(b - a) == nails // 2 for a, b in itertools.pairwise(nums))
print(answer1)


# Part 2


def does_cross(a1: int, b1: int, a2: int, b2: int) -> bool:
    if a1 in (a2, b2) or b1 in (a2, b2):
        return False

    b2_is_left = b2 < a1 or b2 > b1
    a2_is_left = a2 < a1 or a2 > b1

    return b2_is_left != a2_is_left


with open("./2025/input/everybody_codes_e2025_q08_p2.txt") as f:
    lines = f.read().splitlines()

nails = 256
nums = [int(x) - 1 for x in lines[0].split(",")]

answer2 = 0
seen: list[tuple[int, int]] = []
for a1, b1 in itertools.pairwise(nums):
    if a1 > b1:
        a1, b1 = b1, a1

    for a2, b2 in seen:
        answer2 += does_cross(a1, b1, a2, b2)

    seen.append((a1, b1))

print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q08_p3.txt") as f:
    lines = f.read().splitlines()

nails = 256
nums = [int(x) - 1 for x in lines[0].split(",")]

pair_counts = collections.Counter(itertools.pairwise(nums))
answer3 = 0
for a1 in range(nails):
    for b1 in range(a1 + 1, nails):
        cuts = 0
        for (a2, b2), count in pair_counts.items():
            if does_cross(a1, b1, a2, b2):
                cuts += count

        cuts += pair_counts[(a1, b1)]
        cuts += pair_counts[(b1, a1)]
        answer3 = max(answer3, cuts)

print(answer3)
