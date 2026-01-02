MATRIX_WIDTH = 1001
SPIRAL_DEPTH = MATRIX_WIDTH // 2

diagonals = [1]
i = 1
for depth in range(1, SPIRAL_DEPTH + 1):
    for _ in range(4):
        i += 2 * depth
        diagonals.append(i)

answer = sum(diagonals)
print(answer)
