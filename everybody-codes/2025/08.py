with open("./2025/input/everybody_codes_e2025_q08_p1.txt") as f:
    lines = f.read().splitlines()
nails = 32
# lines = "1,5,2,6,8,4,1,7,3".splitlines()
# nails = 8

nums = [int(x) - 1 for x in lines[0].split(",")]
n = len(nums)

answer1 = 0
prev = -100000
for num in nums:
    d = abs(prev - num)
    print(d)
    if d == nails // 2:
        answer1 += 1
    prev = num
# answer1 = "todo"
print(answer1)


# # Part 2

# import math

with open("./2025/input/everybody_codes_e2025_q08_p2.txt") as f:
    lines = f.read().splitlines()
nails = 256

# lines = "1,5,2,6,8,4,1,7,3,5,7,8,2".splitlines()
# nails = 8

nums = [int(x) - 1 for x in lines[0].split(",")]
n = len(nums)


def is_left(num, big, small):
    return num > big or num < small


def is_right(num, big, small):
    return not is_left(num, big, small)


# is_left(8, 7, 1)
# is_right(4, 7, 1)

answer2 = 0
pairs = []
prev = nums[0]
for num in nums[1:]:
    # print(f"{num=} {pairs=}")
    a1, b1 = prev, num
    if a1 < b1:
        a1, b1 = b1, a1

    # a1 bigger

    for a, b in pairs:
        if a in (a1, b1) or b in (a1, b1):
            continue

        if (is_left(a, a1, b1) and is_right(b, a1, b1)) or (
            is_right(a, a1, b1) and is_left(b, a1, b1)
        ):
            answer2 += 1

    pairs.append((prev, num))
    prev = num

print(answer2)


# # Part 3


import collections

with open("./2025/input/everybody_codes_e2025_q08_p3.txt") as f:
    lines = f.read().splitlines()
nails = 256

# lines = "1,5,2,6,8,4,1,7,3,6".splitlines()
# nails = 8

nums = [int(x) - 1 for x in lines[0].split(",")]
n = len(nums)


def is_left(num, big, small):
    return num > big or num < small


def is_right(num, big, small):
    return not is_left(num, big, small)


# is_left(8, 7, 1)
# is_right(4, 7, 1)

answer3 = 0
pairs = collections.Counter()
# pairs = []
prev = nums[0]
for num in nums[1:]:
    # print(f"{num=} {pairs=}")
    a1, b1 = prev, num
    if a1 < b1:
        a1, b1 = b1, a1

    # a1 bigger

    # for (a, b), count in pairs.items():
    #     if a in (a1, b1) or b in (a1, b1):
    #         continue

    #     if (is_left(a, a1, b1) and is_right(b, a1, b1)) or (
    #         is_right(a, a1, b1) and is_left(b, a1, b1)
    #     ):
    #         answer3 += 1

    pairs[(prev, num)] += 1
    prev = num

answer3 = 0
for a1 in range(nails):
    for b1 in range(nails):
        if a1 < b1:
            a1, b1 = b1, a1
        if a1 == b1:
            continue

        cuts = 0
        for (a, b), count in pairs.items():
            if a in (a1, b1) or b in (a1, b1):
                continue

            if (is_left(a, a1, b1) and is_right(b, a1, b1)) or (
                is_right(a, a1, b1) and is_left(b, a1, b1)
            ):
                cuts += count
        # cuts += a1 in nums
        # cuts += b1 in nums
        # cuts += ((a1, b1) in pairs) or ((b1, a1) in pairs)
        cuts += pairs[(a1, b1)]
        cuts += pairs[(b1, a1)]
        answer3 = max(answer3, cuts)

print(answer3)
