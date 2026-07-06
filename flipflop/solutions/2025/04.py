with open("./input/2025/04.txt") as f:
    lines = f.read().splitlines()

x, y = (0, 0)
answer1 = 0
for line in lines:
    x2, y2 = (int(x) for x in line.split(","))
    answer1 += abs(x2 - x) + abs(y2 - y)
    x, y = (x2, y2)
print(answer1)


x, y = (0, 0)
answer2 = 0
for line in lines:
    x2, y2 = (int(x) for x in line.split(","))
    while (x, y) != (x2, y2):
        x += (x2 > x) - (x2 < x)
        y += (y2 > y) - (y2 < y)
        answer2 += 1
print(answer2)


x, y = (0, 0)
trash = [[int(x) for x in line.split(",")] for line in lines]
trash.sort(key=sum)
answer2 = 0
for x2, y2 in trash:
    while (x, y) != (x2, y2):
        x += (x2 > x) - (x2 < x)
        y += (y2 > y) - (y2 < y)
        answer2 += 1
print(answer2)
