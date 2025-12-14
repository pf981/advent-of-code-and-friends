nrows, ncols = (int(x) for x in input().split())

grid = [list(input()) for _ in range(nrows)]

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if (r + c) % 2 == 0:
            row[c] = "A" if ch != "A" else "B"
        else:
            row[c] = "C" if ch != "C" else "D"
    print("".join(row))
