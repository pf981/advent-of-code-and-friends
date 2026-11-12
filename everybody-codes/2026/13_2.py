import math
from fractions import Fraction

with open("./2026/input/everybody_codes_e2026_q13_p2.txt") as f:
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
# with open("./2026/input/everybody_codes_e2026_q13_p2_eg.txt") as f:
#     text = f.read()
# text = """hands 6:8:12
# direction CW:CCW:CW
# current 2:4:8
# move 9:7:4"""


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

    prod = math.lcm(*ns)
    deltas = [prod // n for n in ns]
    positions = [(delta * cur) % prod for delta, cur in zip(deltas, curs)]

    n_hands = len(ns)
    prev_positions = positions.copy()

    meetings = 0
    for t in range(max(max_ts)):
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

    return meetings


answer = 0
for part in text.split("\n\n"):
    meetings = get_calibration(part.splitlines())
    # print(f"{part=}\n{meetings=}\n")
    answer += meetings
print(answer)
