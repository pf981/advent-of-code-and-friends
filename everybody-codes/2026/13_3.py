import math
from fractions import Fraction

with open("./2026/input/everybody_codes_e2026_q13_p3.txt") as f:
    text = f.read()


def overlaps(i: int, j: int, vi: int, vj: int, prod: int) -> bool:
    """
    d_t = d_0 + v * t

    i_t = i + vi * t
    j_t = j + vj * t

    i_t = j_t   I.e. they intersect
    => i + vi * t = j + vj * t
    => t = (i - j) / (vj - vi)

    If 0 < t <= 1 then they will intersect in the next second
    """
    if i == j or vj - vi == 0:
        return False

    def check(i: int):
        t_intersect = Fraction((i - j), (vj - vi))
        return 0 < t_intersect <= 1

    return check(i - prod) or check(i) or check(i + prod)


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
    while t < max(max_ts):
        if tuple(positions) in seen:
            t_seen, meetings_seen = seen[tuple(positions)]

            period_size = t - t_seen
            n_periods = (remaining_ts[-1] - t - 1) // period_size
            assert t + n_periods * period_size < max(max_ts)

            meetings_per_period = meetings - meetings_seen

            t += n_periods * period_size
            meetings += n_periods * meetings_per_period

            seen.clear()
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

        prev_positions = positions.copy()
        t += 1

    return meetings


answer = 0
for part in text.split("\n\n"):
    meetings = get_calibration(part.splitlines())
    answer += meetings
print(answer)
