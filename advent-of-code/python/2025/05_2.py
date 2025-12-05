from aocd import get_data, submit


inp = get_data(day=5, year=2025)
# inp = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""

rngs_str, ings = inp.split("\n\n")
intervals = []
for line in rngs_str.splitlines():
    a, b = line.split("-")
    # s = set(range(int(a), int(b)))
    intervals.append((int(a), int(b)))


intervals.sort()
start = intervals[0][0]
end = intervals[0][1]
answer2 = 0
for a, b in intervals:
    if a <= end:
        end = max(end, b)
    else:
        answer2 += end - start + 1
        start = a
        end = b
answer2 += end - start + 1
print(answer2)
# answer2 = len(fresh)
# print(answer2)
submit(answer2, part="b", day=5, year=2025)
# 440382347383112 wrong.
