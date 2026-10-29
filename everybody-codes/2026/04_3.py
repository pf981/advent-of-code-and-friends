import collections
import re

with open("./2026/input/everybody_codes_e2026_q04_p3.txt") as f:
    lines = f.read().splitlines()

parts = collections.defaultdict(list)  # (quest, part) -> [(t, id_), ...]
points = collections.Counter()
for line in lines:
    id_, quest, part, time = map(int, re.findall(r"-?\d+", line))
    parts[(quest, part)].append((time, id_))

extra_time = collections.Counter()  # (quest, id_) -> t
prev_quest = -1
for quest, part in sorted(parts):
    if quest != prev_quest:
        extra_time = collections.Counter()
    prev_quest = quest

    results = parts[(quest, part)]
    score = 50 * part  # [None, 50, 100, 150][part]
    s = sorted([(t + extra_time[(quest, id_)], id_) for t, id_ in results])  # t + extra

    streak = 1
    prev_t = -1
    score += 1
    for rank, (t, id_) in enumerate(s):
        if t == prev_t:
            streak += 1
        else:
            score -= streak
            streak = 1
        prev_t = t

        points[id_] += max(score, 0)
        extra_time[(quest, id_)] = t


order = sorted(points, key=lambda p: -points[p])

answer = 0
streak = 1
prev_t = -1
score = 0
for id_ in order:
    if points[id_] == prev_t:
        streak += 1
    else:
        score += streak
        streak = 1
    prev_t = points[id_]

    answer += score * points[id_]

print(answer)
