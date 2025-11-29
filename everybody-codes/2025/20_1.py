with open("./2025/input/everybody_codes_e2025_q20_p1.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

pairs = 0
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch != "T":
            continue

        if c + 1 < ncols and lines[r][c + 1] == "T":
            pairs += 1

        if c % 2 == r % 2 and r - 1 >= 0 and lines[r - 1][c] == "T":
            pairs += 1

answer = pairs
print(answer)
