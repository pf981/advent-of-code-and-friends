with open("data/day16.txt") as f:
    text = f.read()

lessons = [(int(line.split()[6]), int(line.split()[-1])) for line in text.splitlines()]
lessons.sort()

answer = 1
cur_end = lessons[0][1]
for start, end in lessons:
    if start < cur_end:
        cur_end = min(cur_end, end)
    else:
        answer += 1
        cur_end = end

print(answer)
