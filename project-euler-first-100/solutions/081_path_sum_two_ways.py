from collections.abc import Generator


def iterate_zigzag(
    matrix: list[list[int]],
) -> Generator[tuple[int, int], None, None]:
    for start_column in reversed(range(len(matrix))):
        for row in reversed(range(start_column + 1, len(matrix))):
            yield (row, len(matrix) + start_column - row)

    for start_row in reversed(range(len(matrix))):
        for column in range(start_row + 1):
            yield (start_row - column, column)


def min_of_not_none(a: int | None, b: int | None) -> int:
    if a is None and b is None:
        return 0
    return min(element for element in [a, b] if element is not None)


with open("data/0081_matrix.txt") as f:
    text = f.read()

dp = [[int(s) for s in line.split(",")] for line in text.splitlines()]

for x, y in iterate_zigzag(dp):
    right = dp[x + 1][y] if x + 1 < len(dp) else None
    down = dp[x][y + 1] if y + 1 < len(dp) else None
    dp[x][y] += min_of_not_none(right, down)

answer = dp[0][0]
print(answer)
