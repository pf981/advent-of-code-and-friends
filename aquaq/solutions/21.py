import functools

with open("./input/21.txt") as f:
    text = f.read()

grid = [[int(x) for x in line.split()] for line in text.splitlines()]
nrows = len(grid)
ncols = len(grid[0])
width = 5


@functools.cache
def get_max(r: int, prev_c: int) -> int:
    if r == nrows:
        return 0

    best = sum(grid[r][prev_c : prev_c + width]) + get_max(r + 1, prev_c)
    if prev_c - 1 >= 0:
        best = max(
            best,
            sum(grid[r][prev_c - 1 : prev_c - 1 + width]) + get_max(r + 1, prev_c - 1),
        )
    if prev_c + 1 + width <= ncols:
        best = max(
            best,
            sum(grid[r][prev_c + 1 : prev_c + 1 + width]) + get_max(r + 1, prev_c + 1),
        )
    return best


answer = max(get_max(0, c) for c in range(ncols - width))
print(answer)
