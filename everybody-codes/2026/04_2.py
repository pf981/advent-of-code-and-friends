import collections
import re

with open("./2026/input/everybody_codes_e2026_q04_p2.txt") as f:
    lines = f.read().splitlines()

parts = collections.defaultdict(set)
times = collections.Counter()
for line in lines:
    id_, quest, part, time = map(int, re.findall(r"-?\d+", line))
    times[id_] += time
    parts[id_].add((quest, part))

order = sorted(times, key=lambda p: (-len(parts[p]), times[p]))

answer = sum(i * times[id_] for i, id_ in enumerate(order, 1))
print(answer)
