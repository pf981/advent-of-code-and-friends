import collections
import itertools


def rot120(lines: list[str]) -> list[str]:
    result = []
    for row in list(
        itertools.zip_longest(*[line.strip(".") for line in lines], fillvalue=".")
    ):
        result.append("".join(reversed(row)))

    if len(result) % 2:
        result.append("." * len(result[0]))

    # Interleave row pairs
    result2 = []
    for row1, row2 in itertools.batched(result, 2):
        final_row = []
        for a, b in zip(row1, row2):
            if b != ".":
                final_row.append(b)
            if a != ".":
                final_row.append(a)
        result2.append("".join(final_row))

    # Add back "."
    for r, row_str in enumerate(result2):
        result2[r] = "." * r + row_str.strip(".") + "." * r

    return result2


def get_nei(r: int, c: int) -> list[tuple[int, int]]:
    neis = [(r, c), (r, c + 1), (r, c - 1)]
    if c % 2 == r % 2:
        neis.append((r - 1, c))
    else:
        neis.append((r + 1, c))

    return list(neis)


with open("./2025/input/everybody_codes_e2025_q20_p3.txt") as f:
    lines = f.read().splitlines()

q = collections.deque(
    [(r, c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == "S"]
)
nrows = len(lines)
ncols = len(lines[0])

all_lines = [lines, rot120(lines), rot120(rot120(lines))]

jumps = 0
seen = {(*q[0], 0)}  # r, c, rot
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if all_lines[jumps % 3][r][c] == "E":
            break

        for r2, c2 in get_nei(r, c):
            rot2 = (jumps + 1) % 3
            if (r2, c2, rot2) in seen:
                continue
            seen.add((r2, c2, rot2))

            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            if all_lines[rot2][r2][c2] not in "EST":
                continue

            q.append((r2, c2))
    else:
        jumps += 1
        continue
    break
else:
    raise ValueError("Unable to find solution")

answer = jumps
print(answer)
