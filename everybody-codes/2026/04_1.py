import collections
import re

with open("./2026/input/everybody_codes_e2026_q04_p1.txt") as f:
    lines = f.read().splitlines()

participants = collections.Counter()
for line in lines:
    id_, quest, part, time = map(int, re.findall(r"-?\d+", line))
    participants[id_] += time

answer = sum(i * id_ for i, id_ in enumerate(sorted(participants.values()), 1))
print(answer)
