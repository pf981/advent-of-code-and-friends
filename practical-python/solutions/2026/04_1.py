with open("./input/2026/04/input1.txt") as f:
    text = f.read()

lines = text.splitlines()

nrows = len(lines)
ncols = len(lines[0])

n = nrows + ncols
seen = set()
for i in range(n):
    r = i * nrows // n
    c = i * ncols // n
    seen.add((r, c))

answer = len(seen)
print(answer)
