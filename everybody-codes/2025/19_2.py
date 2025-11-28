import collections


with open("./2025/input/everybody_codes_e2025_q19_p2.txt") as f:
    lines = f.read().splitlines()

passages = [[int(s) for s in line.split(",")] for line in lines]
m = collections.defaultdict(set)
for x, y, w in passages:
    for y1 in range(y, y + w):
        m[x].add(y1)

target = passages[-1][0]

get_next_x = {}
xs = sorted(m)
for x, next_x in zip([0] + xs, xs):
    get_next_x[x] = next_x


def flaps_required(dx: int, dy: int) -> int | None:
    if abs(dy) > dx:
        return None
    if (dx + dy) % 2:
        return None
    return (dx + dy) // 2


def get_fewest_flaps(x, y) -> int | None:
    if x == target:
        return 0

    next_x = get_next_x[x]
    dx = next_x - x
    for next_y in m[next_x]:
        dy = next_y - y

        flaps_to_target = flaps_required(dx, dy)
        if flaps_to_target is None:
            continue

        remaining_flaps = get_fewest_flaps(next_x, next_y)
        if remaining_flaps is None:
            continue

        return flaps_to_target + remaining_flaps

    return None


answer = get_fewest_flaps(0, 0)
print(answer)
