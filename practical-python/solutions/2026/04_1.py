with open("./input/2026/04/input1.txt") as f:
    text = f.read()

lines = text.splitlines()

nrows = len(lines)
ncols = len(lines[0])

N = 100_000
seen = set()
for i in range(1, N):
    r = i * nrows // N
    c = i * ncols // N
    seen.add((r, c))

answer = len(seen)
print(answer)
