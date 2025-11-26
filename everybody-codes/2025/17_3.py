import heapq
import math
import functools
import itertools

with open("./2025/input/everybody_codes_e2025_q17_p3.txt") as f:
    lines = f.read().splitlines()

grid = {
    (r, c): int(ch) if ch not in "@S" else 0
    for r, row in enumerate(lines)
    for c, ch in enumerate(row)
}
start = next(
    (r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == "S"
)
volcano = next(
    (r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == "@"
)
Yv, Xv = volcano


@functools.cache
def get_lava_radius(r: int, c: int) -> int:
    Xc = c
    Yc = r

    R = math.ceil(math.sqrt((Xv - Xc) * (Xv - Xc) + (Yv - Yc) * (Yv - Yc)))

    return R


def solve(R: int) -> int | None:
    heap = [(0, True, True, True, *start)]
    seen = set()

    while heap:
        el = heapq.heappop(heap)
        t, left_todo, right_todo, bottom_todo, r, c = el

        if (r, c) == start and not left_todo and not right_todo and not bottom_todo:
            return t * (t // 30)

        if el[1:] in seen:
            continue
        seen.add(el[1:])

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc

            if (r2, c2) not in grid:
                continue

            left_todo2 = left_todo
            right_todo2 = right_todo
            bottom_todo2 = bottom_todo

            if r2 == volcano[0] and c2 < volcano[1]:
                left_todo2 = False
            if r2 == volcano[0] and c2 > volcano[1]:
                right_todo2 = False
            if c2 == volcano[1] and r2 > volcano[0]:
                bottom_todo2 = False

            t2 = t + grid[(r2, c2)]
            if get_lava_radius(r2, c2) <= R:
                continue

            if t2 // 30 >= R + 1:
                continue

            heapq.heappush(heap, (t2, left_todo2, right_todo2, bottom_todo2, r2, c2))

    return None


answer = None
for R in itertools.count():
    if result := solve(R):
        answer = result
        break

assert answer is not None
print(answer)
