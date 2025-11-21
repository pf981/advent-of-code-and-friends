with open("./2025/input/everybody_codes_e2025_q14_p2.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])


def sim(active: set[tuple[int, int]]) -> set[tuple[int, int]]:
    result = set()
    for r in range(nrows):
        for c in range(ncols):
            active_diags = 0

            for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                r2 = r + dr
                c2 = c + dc
                active_diags += (r2, c2) in active

            if (r, c) in active:
                if active_diags % 2 == 1:
                    result.add((r, c))
            else:
                if active_diags % 2 == 0:
                    result.add((r, c))

    return result


active = {
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "#"
}

answer = 0
for _ in range(2025):
    active = sim(active.copy())
    answer += len(active)

print(answer)
