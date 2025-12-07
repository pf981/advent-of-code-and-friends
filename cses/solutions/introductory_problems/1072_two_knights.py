n = int(input())

result = []
for k in range(1, n + 1):
    if k <= 5:
        result.append([0, 0, 6, 28, 96, 252][k])
        continue

    squares = k * k

    twos = 4
    threes = 8
    fours = 4 + 4 * (k - 4)
    sixes = 4 * (k - 4)
    eights = squares - twos - threes - fours - sixes

    ways = (
        twos * (squares - 3)
        + threes * (squares - 4)
        + fours * (squares - 5)
        + sixes * (squares - 7)
        + eights * (squares - 9)
    )
    result.append(ways // 2)

print(*result, sep="\n")
