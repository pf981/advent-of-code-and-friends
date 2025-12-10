n = int(input())

moves = []


def move(from_: int, to: int, other: int, n: int) -> None:
    if not n:
        return

    if n == 1:
        moves.append((from_, to))
        return

    move(from_, other, to, n - 1)
    moves.append((from_, to))
    move(other, to, from_, n - 1)


move(1, 3, 2, n)
print(len(moves))
for move in moves:
    print(*move)
