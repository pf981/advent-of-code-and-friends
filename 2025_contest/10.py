import functools


with open("2025_contest/10.txt") as f:
    inp = f.read()


# inp = '''3 3 1 7 8 4 1 3 1 7 7 6 7 8 7 8 2 7 7 1
# 9 9 7 6 3 6 9 4 9 2 6 4 5 7 3 9 3 7 5 6
# 8 9 7 6 7 7 3 2 2 7 8 9 7 1 5 3 1 2 4 4
# 9 2 8 2 3 5 9 2 6 5 7 8 1 6 7 3 6 7 9 6
# 4 1 7 5 2 2 7 6 8 7 2 3 9 2 2 1 6 2 7 5
# 2 9 1 2 9 9 1 2 2 9 3 7 4 5 3 3 7 1 9 4
# 9 9 5 2 6 6 2 3 1 8 3 3 3 6 7 9 8 3 1 5
# 8 4 8 7 2 1 7 9 8 7 3 7 9 1 8 5 2 5 2 8
# 6 8 9 6 6 4 2 2 7 7 7 8 1 2 6 2 6 1 6 7
# 3 8 8 6 9 9 2 7 8 5 4 1 8 8 5 8 3 5 6 6
# 2 8 7 2 6 8 4 7 1 7 6 8 9 4 3 1 2 8 9 8
# 6 2 9 7 7 2 8 7 9 5 6 6 8 2 8 4 4 8 2 2
# 3 1 2 8 8 4 6 8 9 1 4 3 9 1 4 2 2 1 5 4
# 5 2 6 7 2 7 3 9 2 1 7 6 1 2 4 2 1 1 5 9
# 3 6 8 9 4 4 7 7 3 3 4 8 6 1 2 9 7 2 9 6
# 9 4 5 5 7 4 1 7 7 1 3 2 3 8 1 7 6 3 1 9
# 5 3 8 3 1 1 5 3 1 5 9 2 3 6 6 4 4 8 5 3
# 6 3 8 2 9 7 3 6 4 3 2 8 6 9 8 1 2 7 1 5
# 4 1 2 4 8 7 7 1 8 7 4 4 5 7 2 3 3 8 3 3
# 1 5 7 3 3 5 1 5 4 1 1 1 9 2 1 4 6 5 6 3'''

grid = [[int(num) for num in line.split()] for line in inp.splitlines()]

answer1 = min(
    min(sum(row) for row in grid),
    min(sum(col) for col in zip(*grid))
)
print(answer1)


# Part 2

@functools.cache
def get_safest(r, c, target):
    if max(r, c) > target:
        return float('inf')

    if (r, c) == (target, target):
        return grid[r][c]
    
    return grid[r][c] + min(
        get_safest(r + 1, c, target),
        get_safest(r, c + 1, target)
    )

answer2 = get_safest(0, 0, 14)
print(answer2)


# Part 3

answer3 = get_safest(0, 0, len(grid) - 1)
print(answer3)
