import itertools
import math

import downloader


def has_line(x: int, y: int, dy: int) -> bool:
    player = cols[x][y]
    streak = 1

    x2 = x - 1
    y2 = y - dy
    while x2 >= 0 and y2 >= 0 and len(cols[x2]) > y2 and cols[x2][y2] == player:
        streak += 1
        x2 -= 1
        y2 -= dy

    x2 = x + 1
    y2 = y + dy
    while x2 < 7 and y2 >= 0 and len(cols[x2]) > y2 and cols[x2][y2] == player:
        streak += 1
        x2 += 1
        y2 += dy

    return streak >= 4


def has_won(cols: list[list[int]], play: int) -> bool:
    player = cols[play][-1]
    y = len(cols[play]) - 1

    # Vertical
    if cols[play][-4:] == [player] * 4:
        return True

    # Horizontal
    if has_line(play, y, 0):
        return True

    # Diagonal 1
    if has_line(play, y, 1):
        return True

    # Diagonal 2
    if has_line(play, y, -1):
        return True

    return False


lines = downloader.get_puzzle(4).splitlines()

win_counts = [0, 0, 0]
for game in lines:
    it = itertools.cycle(range(3))
    cols: list[list[int]] = [[] for _ in range(7)]
    for play_str in game:
        player = next(it)
        play = int(play_str) - 1
        cols[play].append(player)

        if has_won(cols, play):
            win_counts[player] += 1
            break

answer = math.prod(win_counts)
print(answer)
