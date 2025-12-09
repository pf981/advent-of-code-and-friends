import collections

from aocd import get_data, submit


inp = get_data(day=9, year=2025)
lines = inp.splitlines()
nums = [[int(X) for X in line.split(",")] for line in lines]

decompress_x = sorted({X for X, _ in nums})
decompress_y = sorted({Y for _, Y in nums})

compress_X = {X: decompress_x.index(X) for X, _ in nums}
compress_Y = {Y: decompress_y.index(Y) for _, Y in nums}

x = compress_X[nums[0][0]]
y = compress_Y[nums[0][1]]
border = {(x, y)}
for X, Y in nums + [nums[0]]:
    x2 = compress_X[X]
    y2 = compress_Y[Y]
    while (x, y) != (x2, y2):
        x += (x < x2) - (x > x2)
        y += (y < y2) - (y > y2)
        border.add((x, y))

prefix_sums = collections.defaultdict(int)
for y in range(len(decompress_y)):
    is_outside = True
    for x in range(len(decompress_x)):
        if (x, y) in border and (x - 1, y) not in border:
            is_outside = not is_outside

        prefix_sums[(x, y)] = (
            prefix_sums[(x - 1, y)]
            + prefix_sums[(x, y - 1)]
            - prefix_sums[(x - 1, y - 1)]
            + is_outside
        )

answer2 = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        X1, Y1 = nums[i]
        X2, Y2 = nums[j]

        x1 = compress_X[X1]
        y1 = compress_Y[Y1]
        x2 = compress_X[X2]
        y2 = compress_Y[Y2]

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        is_valid_rect = (
            prefix_sums[(x2, y2)]
            - prefix_sums[(x1 - 1, y2)]
            - prefix_sums[(x2, y1 - 1)]
            + prefix_sums[(x1 - 1, y1 - 1)]
        ) == 0

        if is_valid_rect:
            w = abs(X2 - X1) + 1
            h = abs(Y2 - Y1) + 1
            answer2 = max(answer2, w * h)

submit(answer2, part="b", day=9, year=2025)
