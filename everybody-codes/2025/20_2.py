import collections


def get_nei(r: int, c: int) -> list[tuple[int, int]]:
    neis = [(r, c), (r, c + 1), (r, c - 1)]
    if c % 2 == r % 2:
        neis.append((r - 1, c))
    else:
        neis.append((r + 1, c))

    return list(neis)


with open("./2025/input/everybody_codes_e2025_q20_p2.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

q = collections.deque(
    [
        (r, c)
        for r, row in enumerate(lines)
        for c, ch in enumerate("." * r + row.strip("."))
        if ch == "S"
    ]
)
jumps = 0
seen = set(q)
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if lines[r][c] == "E":
            break

        for r2, c2 in get_nei(r, c):
            if (r2, c2) in seen:
                continue

            if not (0 <= r < nrows and 0 <= c < ncols):
                continue

            if lines[r][c] not in "EST":
                continue

            seen.add((r2, c2))
            q.append((r2, c2))
    else:
        jumps += 1
        continue
    break
else:
    raise ValueError("Unable to find solution")

answer = jumps
print(jumps)
