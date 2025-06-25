import itertools

import downloader

lines = downloader.get_puzzle(13).splitlines()
n = 20

grid = [[int(s) for s in line.split()] for line in lines]
plays = grid[n:]
grid = grid[:n]

grid.reverse()
for i in range(1, n, 2):
    grid[i].reverse()

grid_l = list(itertools.chain.from_iterable(grid))

player1 = player2 = 0
turns = 1
winner = None

for roll1, roll2 in plays:
    player1 += roll1
    while player1 < len(grid_l) and grid_l[player1]:
        player1 += grid_l[player1]

    if player1 >= len(grid_l) - 1:
        winner = 1
        break

    player2 += roll2
    while player2 < len(grid_l) and grid_l[player2]:
        player2 += grid_l[player2]

    if player2 >= len(grid_l) - 1:
        winner = 2
        break

    turns += 1

assert winner

answer = winner * turns
print(answer)
