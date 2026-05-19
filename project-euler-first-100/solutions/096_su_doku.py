def solve(grid: list[list[int]]) -> int:
    todo = [(r, c) for r in range(9) for c in range(9) if grid[r][c] == 0]

    row_masks = [0] * 9
    col_masks = [0] * 9
    grid_masks = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                continue

            mask = 1 << grid[r][c]
            row_masks[r] |= mask
            col_masks[c] |= mask
            grid_masks[r // 3][c // 3] |= mask

    def backtrack(i: int) -> bool:
        if i == len(todo):
            return True

        r, c = todo[i]

        all_mask = row_masks[r] | col_masks[c] | grid_masks[r // 3][c // 3]
        for num in range(1, 10):
            mask = 1 << num
            if all_mask & mask:
                continue

            grid[r][c] = num
            row_masks[r] |= mask
            col_masks[c] |= mask
            grid_masks[r // 3][c // 3] |= mask

            if backtrack(i + 1):
                return True

            grid[r][c] = 0
            row_masks[r] ^= mask
            col_masks[c] ^= mask
            grid_masks[r // 3][c // 3] ^= mask

        return False

    result = backtrack(0)
    assert result
    return 100 * grid[0][0] + 10 * grid[0][1] + grid[0][2]


with open("data/0096_sudoku.txt") as f:
    lines = f.read().splitlines()

grids = []
for i in range(1, len(lines), 10):
    grid = [[int(c) for c in lines[j]] for j in range(i, i + 9)]
    grids.append(grid)

answer = sum(solve(grid) for grid in grids)
print(answer)
