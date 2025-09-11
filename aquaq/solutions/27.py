with open("./input/27.txt") as f:
    text = f.read()

grid = text.splitlines()
nrows = len(grid)
ncols = len(grid[0])

answer = 0
for row in grid:
    answer += sum(
        sum(ord(c) - ord("a") + 1 for c in word) * len(word)
        for word in row.split()
        if len(word) > 1
    )
for col in zip(*grid):
    answer += sum(
        sum(ord(c) - ord("a") + 1 for c in word) * len(word)
        for word in "".join(col).split()
        if len(word) > 1
    )

print(answer)
