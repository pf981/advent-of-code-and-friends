import collections
import re

with open("./2026/input/everybody_codes_e2026_q04_p3.txt") as f:
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
# lines = """id=2 quest=1 part=1 time=90
# id=4 quest=2 part=1 time=150
# id=1 quest=2 part=1 time=130
# id=1 quest=1 part=2 time=180
# id=2 quest=2 part=1 time=130
# id=4 quest=1 part=1 time=110
# id=1 quest=2 part=2 time=210
# id=2 quest=2 part=2 time=220
# id=1 quest=2 part=3 time=330
# id=2 quest=1 part=2 time=170
# id=3 quest=1 part=1 time=90
# id=4 quest=1 part=2 time=170
# id=3 quest=2 part=1 time=120
# id=1 quest=1 part=1 time=120
# id=3 quest=2 part=2 time=220
# id=2 quest=2 part=3 time=350
# id=3 quest=1 part=2 time=170""".splitlines()
# with open("./2026/input/everybody_codes_e2026_q04_p3_ex.txt") as f:
#     lines = f.read().splitlines()

parts = collections.defaultdict(list)  # (quest, part) -> [(t, id_), ...]
points = collections.Counter()
for line in lines:
    id_, quest, part, time = map(int, re.findall(r"-?\d+", line))
    parts[(quest, part)].append((time, id_))

debug = []

extra_time = collections.Counter()  # (quest, id_) -> t
prev_quest = -1
for quest, part in sorted(parts):
    debug.append(f"Quest {quest}, Part {part}:")
    if quest != prev_quest:
        extra_time = collections.Counter()
    prev_quest = quest

    results = parts[(quest, part)]
    score = 50 * part  # [None, 50, 100, 150][part]
    s = sorted([(t + extra_time[(quest, id_)], id_) for t, id_ in results])  # t + extra
    print(s)

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

        if score > 0:
            debug.append(f"id={id_}, time={t}, points={score}")

        points[id_] += max(score, 0)
        extra_time[(quest, id_)] = t
    debug.append("")
    print(f"{points=}")


l = sorted(points, key=lambda p: -points[p])

# answer = sum(i * points[id_] for i, id_ in enumerate(l, 1))

answer = 0
streak = 1
prev_t = -1
score = 0
for id_ in l:
    if points[id_] == prev_t:
        streak += 1
    else:
        score += streak
        streak = 1
    prev_t = points[id_]

    answer += score * points[id_]
    print(f"{score=} {points[id_]=}")

print(answer)

with open("tmp.txt", "w", encoding="utf-8") as f:
    print("\n".join(debug), file=f)

# Dense rank
# 6624904
# Give it another shot!
# Your answer length is: correct
# The first character of your answer is: correct
