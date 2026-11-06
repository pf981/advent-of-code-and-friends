import collections
import itertools
import re

with open("./2026/input/everybody_codes_e2026_q09_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """id=1, growth=3, limit=10
# id=2, growth=5, limit=20
# id=3, growth=7, limit=30""".splitlines()

plants = [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]

answer = 0
for id_, growth, limit in plants:
    tips = 1
    counts = collections.Counter()
    counts[0] = 1

    for seconds in itertools.count():
        counts2 = collections.Counter()
        print(f"{seconds=} {counts=} {tips=}")

        for length, count in counts.items():
            # Grow 1
            # elements += count
            length += 1

            # Split
            # elements += count  # Branching point
            if length == growth:
                m = length // 2
                counts2[m] += 2 * count
                counts2[1] += count  # New branch
                # elements += 1  # FIXME: Not sure if this is right
                tips += count
            else:
                counts2[length] += count

        counts = counts2
        if tips >= limit:
            break

    print(f"{id_=} {growth=} {limit=} {seconds=}\n")
    answer += seconds + 1

print(answer)
# 151
# Your answer length is: correct
# The first character of your answer is: incorrect
