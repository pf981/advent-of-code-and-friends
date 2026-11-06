import itertools
import math
import re


def is_tips_gte_limit(growth: int, t: int, limit: int) -> bool:
    tips = 1
    time_to_grow_half_branch = growth // 2 + 1
    time_to_grow_new_branch = growth - 1

    for half_steps in itertools.count():
        if growth + half_steps * time_to_grow_half_branch > t:
            break

        cur_t = growth + half_steps * time_to_grow_half_branch
        max_new_steps = (t - cur_t) // time_to_grow_new_branch
        for new_steps in range(max_new_steps + 1):
            tips += math.comb(half_steps + new_steps, half_steps) * 2**half_steps

    return tips >= limit


with open("./2026/input/everybody_codes_e2026_q09_p3.txt") as f:
    lines = f.read().splitlines()

plants = [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines]

answer = 0
for id_, growth, limit in plants:
    l = 1
    result = r = next(
        1 << k for k in itertools.count() if is_tips_gte_limit(growth, 1 << k, limit)
    )

    while l <= r:
        m = (l + r) // 2
        if is_tips_gte_limit(growth, m, limit):
            result = m
            r = m - 1
        else:
            l = m + 1

    answer += result

print(answer)
