with open("./2026/input/everybody_codes_e2026_q14_p1.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

pairs = nrows * 2 + ncols * 2
for r in range(nrows):
    for c in range(ncols):
        ch = lines[r][c]
        pairs += r + 1 < nrows and lines[r + 1][c] != ch
        pairs += c + 1 < ncols and lines[r][c + 1] != ch

answer = pairs
print(answer)
