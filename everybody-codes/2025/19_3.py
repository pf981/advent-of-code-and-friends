with open("./2025/input/everybody_codes_e2025_q19_p3.txt") as f:
    lines = f.read().splitlines()
    # text = f.read().strip()

# lines = """7,7,2
# 7,1,3
# 12,0,4
# 15,5,3
# 24,1,6
# 28,5,5
# 40,3,3
# 40,8,2""".splitlines()

import collections

psgs = [[int(s) for s in line.split(",")] for line in lines]
m = collections.defaultdict(set)
for x, y, w in psgs:
    for y1 in range(y, y + w):
        m[x].add(y1)
# m = {x: (y, w) for x, y, w in psgs}
target = psgs[-1][0]


# flaps_required = {}
# for p, (x, y, w) in psgs:
#     for y1 in range(y, y + w):
#         flaps_required[(p, y)] = 0
# # Even, odd

import functools

import sys

sys.setrecursionlimit(1_000_000)


# @functools.cache
# def dfs(target_dx, target_dy) -> int | None:
#     # print(f"{target_dx=} {target_dy=}")
#     if target_dx == 0:
#         return 0 if target_dy == 0 else None

#     if (res := dfs(target_dx - 1, target_dy + 1)) is not None:
#         return res

#     if (res := dfs(target_dx - 1, target_dy - 1)) is not None:
#         return 1 + res
#     return None

"""
up + down = dx
up - down = dy
2up = dx + dy
up = (dx + dy) // 2
"""


def dfs(dx, dy) -> int | None:
    if abs(dy) > dx:
        return None
    if (dx + dy) % 2:
        return None
    return (dx + dy) // 2

    # return ()


# prev_x = 0
# prev_ys = [(0, 0)]  # [(y, flaps), ...]
# for x in m:
#     target_dx = x - prev_x
#     ys = []
#     for y1 in m[x]:
#         for y, flaps in prev_ys:
#             target_dy = y1 - y
#             res = dfs(target_dx, target_dy)
#             # print(f'{x=} {y=} {dx=}')
#             if res is not None:
#                 ys.append((y1, flaps + res))
#     prev_ys = ys
#     prev_x = x
# # prev_ys
# answer = min(flaps for _, flaps in prev_ys)
# print(answer)


next_x = {}
xs = sorted(m)
for x, xnxt in zip([0] + xs, xs):
    next_x[x] = xnxt


def get_fewest_flaps(x, y):
    if x == target:
        return 0

    target_x = next_x[x]
    target_dx = target_x - x
    for target_y in m[target_x]:
        target_dy = target_y - y
        res = dfs(target_dx, target_dy)
        if res is not None:
            remaining_flaps = get_fewest_flaps(target_x, target_y)
            if remaining_flaps is not None:
                return res + remaining_flaps
    return None


answer = get_fewest_flaps(0, 0)  # dfs
print(answer)
