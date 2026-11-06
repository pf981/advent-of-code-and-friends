import collections
import itertools
import re

with open("./2026/input/everybody_codes_e2026_q09_p2.txt") as f:
    lines = f.read().splitlines()

plants = [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]

answer = 0
for id_, growth, limit in plants:
    tips = 1
    counts = collections.Counter()
    counts[0] = 1

    for seconds in itertools.count():
        counts2 = collections.Counter()
        for length, count in counts.items():
            # Grow 1
            length += 1

            # Split
            if length == growth:
                m = length // 2
                counts2[m] += 2 * count
                counts2[1] += count  # New branch
                tips += count
            else:
                counts2[length] += count

        counts = counts2
        if tips >= limit:
            break

    answer += seconds + 1

print(answer)
