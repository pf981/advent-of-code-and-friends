import heapq

with open("./2026/input/everybody_codes_e2026_q15_p2.txt") as f:
    lines = f.read().splitlines()
TARGET_SULPHUR = 2026

nrows = len(lines)
ncols = len(lines[0])
start = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "S")
seen = {}  # (r, c, prev_r, prev_c) -> suphur

heap = [(0, *start, -1, -1, 0)]  # [(d, r, c, prev_r, prev_c, sulphur), ...]
while heap:
    d, r, c, prev_r, prev_c, sulphur = heapq.heappop(heap)

    if (r, c, prev_r, prev_c) in seen and seen[(r, c, prev_r, prev_c)] >= sulphur:
        continue
    seen[(r, c, prev_r, prev_c)] = sulphur

    if lines[r][c] == "E" and sulphur >= TARGET_SULPHUR:
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
