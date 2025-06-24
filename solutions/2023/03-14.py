import collections

import downloader

lines = downloader.get_puzzle(24).splitlines()
n = 20

fruits = []
for part in lines[1].split():
    x, y = (int(s) for s in part.split(","))
    fruits.append((x, y))
fruits.reverse()
moves = lines[3]

snake = collections.deque([(0, 0)])
snake_len = 1
fruit = fruits.pop()
score = 0
for move in moves:
    x, y = snake[-1]
    x += (move == "R") - (move == "L")
    y += (move == "D") - (move == "U")

    if not (0 <= x < n and 0 <= y < n):
        break

    if (x, y) in snake:
        break

    if (x, y) == fruit:
        score += 100
        snake_len += 1
        if fruits:
            fruit = fruits.pop()

    snake.append((x, y))
    if len(snake) > snake_len:
        snake.popleft()

    score += 1

answer = score
print(answer)
