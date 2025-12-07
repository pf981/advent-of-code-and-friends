result = streak = 0
prev = ""
for c in input():
    if c != prev:
        streak = 0
    streak += 1
    prev = c
    result = max(result, streak)

print(result)
