import math


def to_angles(deltas, curs) -> list[float]:
    return [round(delta * cur, 8) for delta, cur in zip(deltas, curs)]


with open("./2026/input/everybody_codes_e2026_q13_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """hands 6:8:12
# direction CW:CCW:CW
# current 2:4:8
# move 9:7:4""".splitlines() # 5
# lines = """hands 6:8:12
# direction CW:CCW:CW
# current 1:2:2
# move 10:12:15""".splitlines() # 7
# lines = """hands 6:8:12
# direction CW:CCW:CW
# current 1:2:2
# move 10:12:20""".splitlines()  # 9

## P2 Examples
# lines = """hands 6:8:12
# direction CW:CCW:CW
# current 2:4:8
# move 9:7:4""".splitlines()  # 5

# lines = """hands 6:8:12
# direction CW:CCW:CW
# current 1:2:2
# move 10:12:15""".splitlines()  # 7

# lines = """hands 6:8:12
# direction CW:CCW:CW
# current 1:2:2
# move 10:12:20""".splitlines()  # 9


# with open("./2026/input/everybody_codes_e2026_q13_p2_eg_out.txt") as f:
#     text = f.read()
# parts = text.split("\n\n")
# lines = parts[0].splitlines()[1:-1]  # Should be 1597 but get 1757


# MULTIPLIER = 100_000
# MULTIPLIER = 10_000
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
    # print(f"\n{t=} {positions=} {meetings=}")
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

    # print(f"{coverage=}")

    for i in range(n_hands):
        for j in range(i + 1, n_hands):
            if (
                coverage[i].intersection(coverage[j])
                and prev_positions[i] != prev_positions[j]
            ):
                # meetings += 1
                pairs.add(frozenset([i, j]))
                print(f"  Meeting {i=} {j=} {t=}")

    # prev_positions = positions.copy()  # FIXME: DEBUG: Uncomment
    if t % 1000 == 0:
        meetings += len(pairs)
        pairs.clear()
        prev_positions = positions.copy()  # FIXME: DEBUG: Uncomment
    # prev_positions = [-1 * i for i in range(1, n_hands + 1)]

answer = meetings
print(answer)

# Edge cases: Same direction, same speed
# - Different direction, but travel half the clock at a time. No - I don't think this counts. Actually, I think it does!

# Can just look at order but being careful of doubles?


# Meetings are
# 1. currently overlapping that weren't previously overlapping
# 2. number of hands to the left that weren't previously to the left

# Or you could descretise the positions. The create set representing all the points traversed
# Only count overlaps for pairs previously pointing in diff directions

# 37
# Your answer length is: correct
# The first character of your answer is: incorrect

# 42
# Your answer length is: correct
# The first character of your answer is: incorrect

# Unless it is 29?
# Yes, 29
