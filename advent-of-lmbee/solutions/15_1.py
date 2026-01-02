import sortedcontainers


with open("data/day15.txt") as f:
    text = f.read()

sl = sortedcontainers.SortedList()
mul = 1
answer = 0
for line in text.splitlines():
    if line == "request":
        median = sl[len(sl) // 2]
        sl.remove(median)
        answer += mul * median
        mul += 1
        continue

    num = int(line.split()[1])
    sl.add(num)

print(answer)
