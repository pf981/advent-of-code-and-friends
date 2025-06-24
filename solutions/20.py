import itertools

import downloader

lines = downloader.get_puzzle(20).splitlines()


def is_winner(squares: set[int]) -> bool:
    win_combinations = [
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9},
        {1, 4, 7},
        {2, 5, 8},
        {3, 6, 9},
        {1, 5, 9},
        {3, 5, 7},
    ]
    return any(squares.issuperset(comb) for comb in win_combinations)


x_wins = o_wins = draws = 0
for line in lines:
    moves = [int(s) for s in line.split()]

    x_squares: set[int] = set()
    o_squares: set[int] = set()
    it = itertools.cycle("XO")

    for move in moves:
        player = next(it)

        squares = {"X": x_squares, "O": o_squares}[player]
        squares.add(move)
        if is_winner(squares):
            if player == "X":
                x_wins += 1
            else:
                o_wins += 1
            break
    else:
        draws += 1

answer = x_wins * o_wins * draws
print(answer)
