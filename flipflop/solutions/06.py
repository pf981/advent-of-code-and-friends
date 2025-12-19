with open("./input/06.txt") as f:
    lines = f.read().splitlines()

sky_n = 1000
frame_n = 500
birds = [[int(d) for d in line.split(",")] for line in lines]

lo = (sky_n - frame_n) // 2
hi = sky_n - lo - 1

answer1 = 0
for dx, dy in birds:
    x = (dx * 100) % sky_n
    y = (dy * 100) % sky_n

    answer1 += lo <= x <= hi and lo <= y <= hi
print(answer1)


answer2 = 0
for dx, dy in birds:
    for h in range(1, 1001):
        x = (dx * 3600 * h) % sky_n
        y = (dy * 3600 * h) % sky_n

        answer2 += lo <= x <= hi and lo <= y <= hi
print(answer2)


answer3 = 0
for dx, dy in birds:
    for h in range(1, 1001):
        x = (dx * 31556926 * h) % sky_n
        y = (dy * 31556926 * h) % sky_n

        answer3 += lo <= x <= hi and lo <= y <= hi
print(answer3)
