months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

answer = 0
day = 1 + 365
for year in range(1901, 2001):
    for mon in range(12):
        if day % 7 == 0:
            answer += 1

        day += months[mon]
        if mon == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day += 1

print(answer)
