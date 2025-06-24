import downloader


lines = downloader.get_puzzle(7).splitlines()
width, height = 20_000, 100_000

# lines = """66 87 34 13
# 64 67 36 33
# 40 54 58 46
# 51 17 49 45
# 83 15 17 51
# 46 46 51 54
# 20 34 52 52
# 65 21 35 46
# 32 68 49 32
# 13 79 43 21
# 87 81 13 19
# 65 26 35 55
# 46 79 51 21
# 17 53 46 45
# 77 17 23 41
# 4 17 54 47
# 7 28 42 53
# 9 47 45 41
# 40 14 45 44
# 77 61 23 39""".splitlines()
# width, height = 100, 100

# lines = """0 0 5 7
# 7 0 3 9
# 0 6 10 4""".splitlines()
# width, height = 10, 10

col_intervals: list[list[tuple[int, int]]] = [[] for _ in range(height)]
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

# 8154807700 wrong
