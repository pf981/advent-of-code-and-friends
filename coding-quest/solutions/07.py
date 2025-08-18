import downloader


lines = downloader.get_puzzle(7).splitlines()
width, height = 20_000, 100_000

col_intervals: list[list[tuple[int, int]]] = [[] for _ in range(width)]
for line in lines:
    x, y, w, h = (int(s) for s in line.split())
    for x1 in range(x, x + w):
        col_intervals[x1].append((y, y + h))

answer = 0
for intervals in col_intervals:
    intervals.sort()
    intervals.append((height, height))
    end = 0

    for a, b in intervals:
        if a > end:
            answer += a - end
        end = max(end, b)

print(answer)
