with open("./2026/input/everybody_codes_e2026_q12_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """........#.
# .##.......
# .##..####.
# .##..####.
# .....####.
# .###......""".splitlines()

nrows = len(lines)
ncols = len(lines[0])

answer = 0
seen = set()
for r in range(nrows):
    for c in range(ncols):
        if (r, c) in seen or lines[r][c] != "#":
            continue
        seen.add((r, c))

        for r2 in range(r, nrows):
            seen.add((r2, c))
            print(f"{r2=} {c=}")
            if lines[r2][c] != "#":
                r2 -= 1
                break

        for c2 in range(c, ncols):
            seen.add((r, c2))
            print(f"{r=} {c2=}")
            if lines[r][c2] != "#":
                c2 -= 1
                break

        n_rows = r2 - r + 1
        n_cols = c2 - c + 1

        for r2 in range(r, r2 + 1):
            for c2 in range(c, c2 + 1):
                seen.add((r2, c2))

        print(f"{r=} {c=} {n_rows=} {n_cols=}")
        print(f"{seen=}\n")

        answer += min(n_rows, n_cols)

print(answer)
