import heapq

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


x_min = -1
x_max = len(decompress_x)
y_min = -1
y_max = len(decompress_y)

prefix_sums = {}
for y in range(y_min, y_max + 1):
    s = 0
    is_outside = True
    for x in range(x_min, x_max + 1):
        if (x, y) in border and (x - 1, y) not in border:
            is_outside = not is_outside
        s += is_outside
        prefix_sums[(x, y)] = s


def is_valid_rect(x1: int, x2: int, y1: int, y2: int) -> bool:
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for y in range(y1, y2 + 1):
        if prefix_sums[(x2, y)] - prefix_sums[(x1 - 1, y)] != 0:
            return False
    return True


heap = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        X1, Y1 = nums[i]
        X2, Y2 = nums[j]
        w = abs(X2 - X1) + 1
        h = abs(Y2 - Y1) + 1

        x1 = compress_X[X1]
        y1 = compress_Y[Y1]
        x2 = compress_X[X2]
        y2 = compress_Y[Y2]

        heapq.heappush(heap, (-w * h, x1, x2, y1, y2))

answer2 = None
while heap:
    neg_area, x1, x2, y1, y2 = heapq.heappop(heap)
    if is_valid_rect(x1, x2, y1, y2):
        answer2 = -neg_area
        break

assert answer2
submit(answer2, part="b", day=9, year=2025)
