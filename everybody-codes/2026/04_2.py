import collections
import re

with open("./2026/input/everybody_codes_e2026_q04_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """id=2 quest=1 part=1 time=100
# id=4 quest=2 part=1 time=150
# id=1 quest=2 part=1 time=140
# id=1 quest=1 part=2 time=180
# id=2 quest=2 part=1 time=130
# id=4 quest=1 part=1 time=110
# id=1 quest=2 part=2 time=210
# id=2 quest=2 part=2 time=240
# id=1 quest=2 part=3 time=330
# id=2 quest=1 part=2 time=170
# id=3 quest=1 part=1 time=90
# id=4 quest=1 part=2 time=175
# id=3 quest=2 part=1 time=120
# id=1 quest=1 part=1 time=120
# id=3 quest=2 part=2 time=220
# id=2 quest=2 part=3 time=350
# id=3 quest=1 part=2 time=160""".splitlines()

parts = collections.defaultdict(set)
times = collections.Counter()
for line in lines:
    id_, quest, part, time = map(int, re.findall(r"-?\d+", line))
    times[id_] += time
    parts[id_].add((quest, part))

l = sorted(times, key=lambda p: (-len(parts[p]), times[p]))

answer = sum(i * times[id_] for i, id_ in enumerate(l, 1))
print(answer)
