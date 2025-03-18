import itertools


with open("2025_contest/01.txt") as f:
    lines = f.read().splitlines()

offset, *corrections, signs = lines
offset = int(offset)

nums = [int(correction) * (-1 if sign == '-' else 1) for correction, sign in zip(corrections, signs)]

answer1 = offset + sum(nums)
print(answer1)


# Part 2

nums = [int(correction) * (-1 if sign == '-' else 1) for correction, sign in zip(corrections, reversed(signs))]

answer2 = offset + sum(nums)
print(answer2)


# Part 3

o1, o2, *corrections, signs = lines

nums = [int(a + b) * (-1 if sign == '-' else 1) for (a, b), sign in zip(itertools.batched(corrections, 2), reversed(signs))]

answer3 = int(o1 + o2) + sum(nums)
print(answer3)
