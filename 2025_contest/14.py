import functools
import math
import re


with open("2025_contest/14.txt") as f:
    inp = f.read()

lines = inp.splitlines()

crafts = []
for line in lines:
    code, quality, cost, unique_materials = re.match(
        r" *\d+ ([a-zA-Z]+) \| Quality : (\d+), Cost : (\d+), Unique Materials : (\d+)",
        line,
    ).groups()
    crafts.append([code, int(quality), int(cost), int(unique_materials)])

highest = sorted(crafts, key=lambda x: (x[1], x[2]))[-5:]
answer1 = sum(craft[3] for craft in highest)
print(answer1)


# Part 2


@functools.cache
def get_max_quality(i, units):
    if units < 0:
        return float("-inf"), -1
    if i == len(crafts):
        return 0, 0

    discard_quality, discard_mats = get_max_quality(i + 1, units)

    keep_quality, keep_mats = get_max_quality(i + 1, units - crafts[i][2])
    keep_mats += crafts[i][3]
    keep_quality += crafts[i][1]

    return max((discard_quality, discard_mats), (keep_quality, keep_mats))


answer2 = math.prod(get_max_quality(0, 30))
print(answer2)


# Part 3

answer3 = math.prod(get_max_quality(0, 300))
print(answer3)
 