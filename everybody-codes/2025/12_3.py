import collections


def get_destroyed(
    m: dict[tuple[int, int], int], starts: list[tuple[int, int]]
) -> set[tuple[int, int]]:
    q = collections.deque(starts)
    destroyed = set()
    while q:
        r, c = q.popleft()
        if (r, c) not in m:
            continue
        if (r, c) in destroyed:
            continue
        destroyed.add((r, c))

        val = m[(r, c)]
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) not in m or (r2, c2) in destroyed:
                continue
            if m[(r2, c2)] > val:
                continue
            q.append((r2, c2))
    return destroyed


def get_best_pos(
    m: dict[tuple[int, int], int],
) -> tuple[tuple[int, int], set[tuple[int, int]]]:
    _, pos, destroyed = max(
        (len(destroyed := get_destroyed(m, [pos])), pos, destroyed) for pos in m
    )
    return pos, destroyed


with open("./2025/input/everybody_codes_e2025_q12_p3.txt") as f:
    lines = f.read().splitlines()

m = {(r, c): int(ch) for r, line in enumerate(lines) for c, ch in enumerate(line)}

nrows = len(lines)
ncols = len(lines[0])

pos1, destroyed1 = get_best_pos(m)

m2 = m.copy()
for r, c in destroyed1:
    del m2[(r, c)]

pos2, destroyed2 = get_best_pos(m2)

m3 = m2.copy()
for r, c in destroyed2:
    if (r, c) in m3:
        del m3[(r, c)]

pos3, destroyed3 = get_best_pos(m3)

final_destroyed = get_destroyed(m, [pos1, pos2, pos3])

answer = len(final_destroyed)
print(answer)
