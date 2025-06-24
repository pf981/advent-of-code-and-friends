import downloader

lines = downloader.get_puzzle(22).splitlines()

grid = [[False] * 50 for _ in range(10)]

for line in lines:
    c1, r1, w, h = (int(s) for s in line.split())
    for r in range(r1, r1 + h):
        for c in range(c1, c1 + w):
            grid[r][c] = not grid[r][c]

for row in grid:
    print("".join([".", "#"][int(cell)] for cell in row))

answer = "ncc1701"
print(answer)
