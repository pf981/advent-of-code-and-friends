from aocd import get_data, submit


inp = get_data(day=5, year=2025)

intervals_str, _ = inp.split("\n\n")
intervals = [[int(x) for x in line.split("-")] for line in intervals_str.splitlines()]

intervals.sort()
start, end = intervals[0]
answer2 = 0
for a, b in intervals:
    if a <= end:
        end = max(end, b)
    else:
        answer2 += end - start + 1
        start = a
        end = b
answer2 += end - start + 1

submit(answer2, part="b", day=5, year=2025)
