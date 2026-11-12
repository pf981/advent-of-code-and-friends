import math

with open("./2026/input/everybody_codes_e2026_q13_p1.txt") as f:
    lines = f.read().splitlines()
MULTIPLIER = 1000

ns = list(map(int, lines[0].split()[1].split(":")))
is_cws = [s == "CW" for s in lines[1].split()[1].split(":")]
curs = list(map(int, lines[2].split()[1].split(":")))
max_ts = list(map(int, lines[3].split()[1].split(":")))

prod = math.lcm(*ns) * MULTIPLIER
deltas = [prod // n // MULTIPLIER for n in ns]
max_ts = [max_t * MULTIPLIER for max_t in max_ts]
positions = [delta * cur * MULTIPLIER for delta, cur in zip(deltas, curs)]

n_hands = len(ns)
prev_positions = positions.copy()

meetings = 0
pairs = set()
for t in range(max(max_ts)):
    coverage = [set() for _ in range(n_hands)]

    for i in range(n_hands):
        if t >= max_ts[i]:
            coverage[i].add(positions[i])
            continue

        sign = 1 if is_cws[i] else -1

        for _ in range(deltas[i]):
            positions[i] += sign
            positions[i] %= prod
            coverage[i].add(positions[i])

    for i in range(n_hands):
        for j in range(i + 1, n_hands):
            if (
                coverage[i].intersection(coverage[j])
                and prev_positions[i] != prev_positions[j]
            ):
                pairs.add(frozenset([i, j]))
    if t % 1000 == 0:
        meetings += len(pairs)
        pairs.clear()
        prev_positions = positions.copy()

answer = meetings
print(answer)
