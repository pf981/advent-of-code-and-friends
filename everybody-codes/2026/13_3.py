import math
from fractions import Fraction

with open("./2026/input/everybody_codes_e2026_q13_p3.txt") as f:
    text = f.read()
# text = """hands 6:8:12
# direction CW:CCW:CW
# current 2:4:8
# move 9:7:4

# hands 6:8:12
# direction CW:CCW:CW
# current 1:2:2
# move 10:12:15

# hands 6:8:12
# direction CW:CCW:CW
# current 1:2:2
# move 10:12:20"""  # 5+7+9=21
# with open("./2026/input/everybody_codes_e2026_q13_p3_eg.txt") as f:
#     text = f.read()
# text = """hands 6:8:12
# direction CW:CCW:CW
# current 2:4:8
# move 9:7:4"""
# text = """hands 9:11:20
# direction CW:CCW:CW
# current 0:1:17
# move 7224:7352:7518"""  # eg 3: 2972

# text = """hands 8:4:28
# direction CCW:CCW:CCW
# current 6:0:20
# move 11160:10415:10560
# meetings 4650"""  # Clock 005: 4650


def overlaps(i: int, j: int, vi: int, vj: int, prod: int) -> bool:
    if i == j:
        return False

    def check(i: int, j: int, vi: int, vj: int):
        if vj - vi == 0:
            # If they are going the same speed, they can't intersect unless they started from the same position
            return False
        t_intersect = Fraction((i - j), (vj - vi))
        # print(f"{i=} {j=} {vi=} {vj=} {t_intersect=}")
        return 0 < t_intersect <= 1

    for d in range(-5, 5 + 1):
        if check(i - d * prod, j, vi, vj):
            return True
    return False


def get_calibration(lines: list[str]) -> int:
    ns = list(map(int, lines[0].split()[1].split(":")))
    is_cws = [s == "CW" for s in lines[1].split()[1].split(":")]
    curs = list(map(int, lines[2].split()[1].split(":")))
    max_ts = list(map(int, lines[3].split()[1].split(":")))
    remaining_ts = sorted(max_ts, reverse=True)

    prod = math.lcm(*ns)
    deltas = [prod // n for n in ns]
    positions = [(delta * cur) % prod for delta, cur in zip(deltas, curs)]

    n_hands = len(ns)
    prev_positions = positions.copy()

    meetings = 0
    seen = {}  # positions -> (t, meetings)
    t = 0
    # for t in range(max(max_ts)):
    while t < max(max_ts):
        # TODO: Should this be here or after?
        if tuple(positions) in seen:
            # print(f"{positions=} {seen=}")
            t_seen, meetings_seen = seen[tuple(positions)]

            period_size = t - t_seen
            print(f"{period_size=} {t=} {t_seen=}")
            # n_periods = (remaining_ts[-1] - t) // period_size  # FIXME: USE THIS
            n_periods = (remaining_ts[-1] - t - 1) // period_size
            # n_periods = 1  # FIXME: TEST
            # if n_periods < 0:
            # n_periods = 0
            # if t + period_size >= max(max_ts):
            #     n_periods = 0
            assert t + n_periods * period_size < max(max_ts)

            meetings_per_period = meetings - meetings_seen

            t += n_periods * period_size
            meetings += n_periods * meetings_per_period

            # assert n_periods >= 1

            # print(
            #     f"{t=} {positions=} {meetings=} {t_seen=} {meetings_seen=} {max(max_ts)=} {period_size=} {n_periods=} {meetings_per_period=}"
            # )
            seen.clear()  # FIXME: TEST

        # if t:
        else:
            seen[tuple(positions)] = (t, meetings)

        while t >= remaining_ts[-1]:
            remaining_ts.pop()
            seen.clear()

        for i in range(n_hands):
            if t >= max_ts[i]:
                deltas[i] = 0

            sign = 1 if is_cws[i] else -1

            positions[i] += sign * deltas[i]
            positions[i] %= prod

        for i in range(n_hands):
            for j in range(i + 1, n_hands):
                if overlaps(
                    prev_positions[i],
                    prev_positions[j],
                    (1 if is_cws[i] else -1) * deltas[i],
                    (1 if is_cws[j] else -1) * deltas[j],
                    prod,
                ):
                    meetings += 1
                    # print(f"  Meeting {i=} {j=} {t=} {positions=}")

        prev_positions = positions.copy()
        t += 1

    return meetings


answer = 0
for part in text.split("\n\n"):
    meetings = get_calibration(part.splitlines())
    print(f"{part=}\n{meetings=}\n")
    answer += meetings
print(answer)
