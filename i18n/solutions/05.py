with open("./input/05.txt", encoding="utf-8") as f:
    text = f.read()

grid = text.splitlines()
nrows = len(grid)
ncols = len(grid[0])

c = answer = 0
for r in range(nrows):
    answer += grid[r][c] == "💩"
    c = (c + 2) % ncols
print(answer)
