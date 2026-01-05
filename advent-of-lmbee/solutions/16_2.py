with open("data/day16.txt") as f:
    text = f.read()

lessons = [(int(line.split()[6]), int(line.split()[-1])) for line in text.splitlines()]
lessons.sort()

weeks = 0
lessons_completed = [False] * len(lessons)
while any(not completed for completed in lessons_completed):
    cur_end = None
    for i, (start, end) in enumerate(lessons):
        if lessons_completed[i]:
            continue

        if cur_end is not None and start < cur_end:
            continue

        cur_end = end
        lessons_completed[i] = True
    weeks += 1

answer = weeks
print(answer)
