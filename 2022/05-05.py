import itertools
import math

import downloader


def has_won(cols: list[list[int]], play: int) -> bool:
    player = cols[play][-1]
    y = len(cols[play]) - 1

    # Vertical
    if cols[play][-4:] == [player] * 4:
        return True

    # Horizontal
    streak = 1
    i = play - 1
    while i >= 0 and len(cols[i]) > y and cols[i][y] == player:
        streak += 1
        i -= 1

    i = play + 1
    while i < 7 and len(cols[i]) > y and cols[i][y] == player:
        streak += 1
        i += 1

    if streak >= 4:
        return True

    # Descending Diagonal
    streak = 1
    i = play - 1
    y2 = y + 1
    while i >= 0 and len(cols[i]) > y2 and cols[i][y2] == player:
        streak += 1
        y2 += 1
        i -= 1

    i = play + 1
    y2 = y - 1
    while i < 7 and y2 >= 0 and len(cols[i]) > y2 and cols[i][y2] == player:
        streak += 1
        y2 -= 1
        i += 1

    if streak >= 4:
        return True

    # Ascending Diagonal
    streak = 1
    i = play - 1
    y2 = y - 1
    while i >= 0 and y2 >= 0 and len(cols[i]) > y2 and cols[i][y2] == player:
        streak += 1
        y2 -= 1
        i -= 1

    i = play + 1
    y2 = y + 1
    while i < 7 and len(cols[i]) > y2 and cols[i][y2] == player:
        streak += 1
        y2 += 1
        i += 1

    if streak >= 4:
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
