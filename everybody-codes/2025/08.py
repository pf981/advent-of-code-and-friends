import collections


with open("./2025/input/everybody_codes_e2025_q08_p1.txt") as f:
    lines = f.read().splitlines()

nails = 32
nums = [int(x) - 1 for x in lines[0].split(",")]

answer1 = 0
prev = nums[0]
for num in nums[1:]:
    d = abs(prev - num)
    answer1 += d == nails // 2
    prev = num

print(answer1)


# Part 2


def is_left(num, big, small):
    return num > big or num < small


def is_right(num, big, small):
    return not is_left(num, big, small)


with open("./2025/input/everybody_codes_e2025_q08_p2.txt") as f:
    lines = f.read().splitlines()

nails = 256
nums = [int(x) - 1 for x in lines[0].split(",")]

answer2 = 0
pairs: list[tuple[int, int]] = []
prev = nums[0]
for num in nums[1:]:
    a1, b1 = prev, num
    if a1 < b1:
        a1, b1 = b1, a1

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


# Part 3


with open("./2025/input/everybody_codes_e2025_q08_p3.txt") as f:
    lines = f.read().splitlines()

nails = 256
nums = [int(x) - 1 for x in lines[0].split(",")]

pair_counts = collections.Counter(zip(nums[:-1], nums[1:]))

answer3 = 0
for a1 in range(1, nails):
    for b1 in range(a1):
        cuts = 0
        for (a, b), count in pair_counts.items():
            if a in (a1, b1) or b in (a1, b1):
                continue

            if (is_left(a, a1, b1) and is_right(b, a1, b1)) or (
                is_right(a, a1, b1) and is_left(b, a1, b1)
            ):
                cuts += count

        cuts += pair_counts[(a1, b1)]
        cuts += pair_counts[(b1, a1)]
        answer3 = max(answer3, cuts)

print(answer3)
