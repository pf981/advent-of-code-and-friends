with open("./input/6.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    (x, y), (dx, dy) = (map(int, part.split(",")) for part in line.split())

    if x % dx:
        continue
    d = x // dx
    answer += y - d * (dy - 1) == 0

print(answer)
