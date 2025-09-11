with open("./input/27.txt") as f:
    text = f.read()

grid = text.splitlines()
nrows = len(grid)
ncols = len(grid[0])

answer = 0
for r in range(nrows):
    word = ""
    for c in range(ncols):
        if grid[r][c] != " ":
            word += grid[r][c]
        else:
            if len(word) > 1:
                answer += sum(ord(c) - ord("a") + 1 for c in word) * len(word)
            word = ""
    if len(word) > 1:
        answer += sum(ord(c) - ord("a") + 1 for c in word) * len(word)

for c in range(ncols):
    word = ""
    for r in range(nrows):
        if grid[r][c] != " ":
            word += grid[r][c]
        else:
            if len(word) > 1:
                answer += sum(ord(c) - ord("a") + 1 for c in word) * len(word)
            word = ""
    if len(word) > 1:
        answer += sum(ord(c) - ord("a") + 1 for c in word) * len(word)

print(answer)
