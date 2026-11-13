import heapq
import itertools

with open("./2026/input/everybody_codes_e2026_q15_p3.txt") as f:
    lines = f.read().splitlines()
TARGET_SULPHUR = 202620262026
SOFT_TARGET = TARGET_SULPHUR - 1000

nrows = len(lines)
ncols = len(lines[0])
start = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "S")
all_seen = set()  # (r, c, prev_r, prev_c, suphur)

it = itertools.count()

heap2 = []
heap = [
    (0, *start, -1, -1, 0, next(it), {})
]  # [(d, r, c, prev_r, prev_c, sulphur, _, seen), ...]
# seen: (r, c, prev_r, prev_c) -> (d, sulphur)
while heap:
    d, r, c, prev_r, prev_c, sulphur, _, seen = heapq.heappop(heap)

    if sulphur > TARGET_SULPHUR:
        continue

    if (r, c, prev_r, prev_c, sulphur) in all_seen:
        continue
    all_seen.add((r, c, prev_r, prev_c, sulphur))

    if (r, c, prev_r, prev_c) in seen:
        seen_d, seen_sulphur = seen[(r, c, prev_r, prev_c)]
        if seen_sulphur >= sulphur:
            # Skipping wouldn't increase sulphur
            continue

        # Skip forward until SOFT_TARGET
        period_size = d - seen_d
        sulpher_needed = SOFT_TARGET - sulphur
        sulpher_per_period = sulphur - seen_sulphur
        n_periods = sulpher_needed // sulpher_per_period

        d2 = d + n_periods * period_size
        sulphur2 = sulphur + n_periods * sulpher_per_period

        heapq.heappush(heap2, (d2, r, c, prev_r, prev_c, sulphur2))

        continue

    seen = seen.copy()
    seen[(r, c, prev_r, prev_c)] = (d, sulphur)

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if (r2, c2) == (prev_r, prev_c):
            continue

        if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            continue

        if lines[r2][c2] == "#":
            continue

        heapq.heappush(
            heap,
            (d + 1, r2, c2, r, c, sulphur + (lines[r2][c2] == "@"), next(it), seen),
        )

# Use part 2 solution for the rest of the steps

heap = heap2  # [(d, r, c, prev_r, prev_c, sulphur), ...]
seen = {}  # (r, c, prev_r, prev_c) -> suphur
while heap:
    d, r, c, prev_r, prev_c, sulphur = heapq.heappop(heap)

    if (r, c, prev_r, prev_c) in seen and seen[(r, c, prev_r, prev_c)] >= sulphur:
        continue
    seen[(r, c, prev_r, prev_c)] = sulphur

    if lines[r][c] == "E" and sulphur == TARGET_SULPHUR:
        break

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if (r2, c2) == (prev_r, prev_c):
            continue

        if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            continue

        if lines[r2][c2] == "#":
            continue

        heapq.heappush(heap, (d + 1, r2, c2, r, c, sulphur + (lines[r2][c2] == "@")))

assert lines[r][c] == "E"
answer = d
print(answer)
