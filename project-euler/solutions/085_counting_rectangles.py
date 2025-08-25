MAX_LENGTH = 1000

best = (2_000_000, 0)
for width in range(MAX_LENGTH):
    for height in range(MAX_LENGTH):
        rectangles = width * (width + 1) // 2 * height * (height + 1) // 2
        d = abs(rectangles - 2_000_000)
        best = min(best, (d, width * height))

answer = best[1]
print(answer)
